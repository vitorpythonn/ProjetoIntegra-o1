from flask import Flask, render_template, request, redirect, url_for, session
from database import get_db_connection
from functools import wraps

app = Flask(__name__)

app.secret_key = "chave-projeto-chamados"


def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if "usuario_id" not in session:
            return redirect(url_for("login"))

        return view(*args, **kwargs)

    return wrapped_view


@app.route("/")
def index():
    if "usuario_id" not in session:
        return redirect(url_for("login"))

    return redirect(url_for("chamados"))


# LOGIN
@app.route("/login", methods=("GET", "POST"))
def login():

    if request.method == "POST":

        email = request.form["email"].strip()
        senha = request.form["senha"]

        connection = get_db_connection()

        usuario = connection.execute(
            """
            SELECT id, nome, email, senha, perfil
            FROM usuario
            WHERE email = ?
            """,
            (email,)
        ).fetchone()

        connection.close()

        if usuario is None or usuario["senha"] != senha:

            return render_template(
                "login.html",
                erro="E-mail ou senha inválidos."
            )

        session.clear()

        session["usuario_id"] = usuario["id"]
        session["usuario_nome"] = usuario["nome"]
        session["usuario_perfil"] = usuario["perfil"]

        return redirect(url_for("chamados"))

    return render_template("login.html")


# LOGOUT
@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))


# CADASTRO
@app.route("/cadastro", methods=("GET", "POST"))
def cadastro():

    if request.method == "POST":

        nome = request.form["nome"].strip()
        email = request.form["email"].strip()
        senha = request.form["senha"]

        if not nome or not email or not senha:

            return render_template(
                "cadastro.html",
                erro="Todos os campos são obrigatórios."
            )

        connection = get_db_connection()

        usuario_existente = connection.execute(
            "SELECT id FROM usuario WHERE email = ?",
            (email,)
        ).fetchone()

        if usuario_existente:

            connection.close()

            return render_template(
                "cadastro.html",
                erro="Já existe um usuário cadastrado com este e-mail."
            )

        connection.execute(
            """
            INSERT INTO usuario
            (nome, email, senha, perfil)
            VALUES (?, ?, ?, 'usuario')
            """,
            (nome, email, senha)
        )

        connection.commit()
        connection.close()

        return redirect(
            url_for("login", cadastro="sucesso")
        )

    return render_template("cadastro.html")


# ABERTURA DE CHAMADO
@app.route("/chamado", methods=("GET", "POST"))
@login_required
def chamado():

    connection = get_db_connection()

    if request.method == "POST":

        titulo = request.form["titulo"].strip()
        descricao = request.form["descricao"].strip()
        prioridade = request.form["prioridade"]
        categoria_id = request.form["categoria_id"]

        if not titulo or not descricao or not categoria_id or not prioridade:

            categorias = connection.execute(
                """
                SELECT id, nome
                FROM categoria
                ORDER BY nome
                """
            ).fetchall()

            connection.close()

            return render_template(
                "chamado.html",
                categorias=categorias,
                erro="Preencha todos os campos obrigatórios."
            )

        connection.execute(
            """
            INSERT INTO chamado
            (
                titulo,
                descricao,
                prioridade,
                usuario_id,
                categoria_id
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                titulo,
                descricao,
                prioridade,
                session["usuario_id"],
                categoria_id
            )
        )

        connection.commit()
        connection.close()

        return redirect(url_for("chamados"))

    categorias = connection.execute(
        """
        SELECT id, nome
        FROM categoria
        ORDER BY nome
        """
    ).fetchall()

    connection.close()

    return render_template(
        "chamado.html",
        categorias=categorias
    )


# CONSULTA DE CHAMADOS
@app.route("/chamados")
@login_required
def chamados():

    connection = get_db_connection()

    if session["usuario_perfil"] == "analista":

        chamados = connection.execute(
            """
            SELECT
                chamado.id,
                chamado.titulo,
                chamado.descricao,
                chamado.prioridade,
                chamado.status,
                chamado.data_abertura,
                usuario.nome AS usuario,
                categoria.nome AS categoria
            FROM chamado

            INNER JOIN usuario
                ON chamado.usuario_id = usuario.id

            INNER JOIN categoria
                ON chamado.categoria_id = categoria.id

            ORDER BY chamado.id DESC
            """
        ).fetchall()

    else:

        chamados = connection.execute(
            """
            SELECT
                chamado.id,
                chamado.titulo,
                chamado.descricao,
                chamado.prioridade,
                chamado.status,
                chamado.data_abertura,
                usuario.nome AS usuario,
                categoria.nome AS categoria
            FROM chamado

            INNER JOIN usuario
                ON chamado.usuario_id = usuario.id

            INNER JOIN categoria
                ON chamado.categoria_id = categoria.id

            WHERE chamado.usuario_id = ?

            ORDER BY chamado.id DESC
            """,
            (session["usuario_id"],)
        ).fetchall()

    connection.close()

    return render_template(
        "chamados.html",
        chamados=chamados
    )


# DETALHES DO CHAMADO
@app.route("/chamado/<int:chamado_id>")
@login_required
def detalhes_chamado(chamado_id):

    connection = get_db_connection()

    chamado = connection.execute(
        """
        SELECT
            chamado.id,
            chamado.titulo,
            chamado.descricao,
            chamado.prioridade,
            chamado.status,
            chamado.data_abertura,
            chamado.data_fechamento,
            usuario.nome AS usuario,
            categoria.nome AS categoria
        FROM chamado

        INNER JOIN usuario
            ON chamado.usuario_id = usuario.id

        INNER JOIN categoria
            ON chamado.categoria_id = categoria.id

        WHERE chamado.id = ?
        """,
        (chamado_id,)
    ).fetchone()

    if chamado is None:

        connection.close()

        return "Chamado não encontrado.", 404

    # Usuário comum só pode visualizar os próprios chamados.
    if (
        session["usuario_perfil"] != "analista"
        and chamado["usuario"] != session["usuario_nome"]
    ):

        connection.close()

        return "Acesso não autorizado.", 403

    solucoes = connection.execute(
        """
        SELECT
            id,
            descricao,
            data_registro
        FROM solucao

        WHERE chamado_id = ?

        ORDER BY id DESC
        """,
        (chamado_id,)
    ).fetchall()

    connection.close()

    return render_template(
        "detalhes_chamado.html",
        chamado=chamado,
        solucoes=solucoes
    )


# ATUALIZAÇÃO DE STATUS
@app.route(
    "/chamado/<int:chamado_id>/atualizar",
    methods=("POST",)
)
@login_required
def atualizar_chamado(chamado_id):

    if session["usuario_perfil"] != "analista":

        return "Acesso não autorizado.", 403

    status = request.form["status"]

    status_validos = [
        "Aberto",
        "Em andamento",
        "Resolvido",
        "Fechado"
    ]

    if status not in status_validos:

        return "Status inválido.", 400

    connection = get_db_connection()

    if status == "Fechado":

        connection.execute(
            """
            UPDATE chamado

            SET
                status = ?,
                data_fechamento = CURRENT_TIMESTAMP

            WHERE id = ?
            """,
            (status, chamado_id)
        )

    else:

        connection.execute(
            """
            UPDATE chamado

            SET
                status = ?,
                data_fechamento = NULL

            WHERE id = ?
            """,
            (status, chamado_id)
        )

    connection.commit()
    connection.close()

    return redirect(
        url_for(
            "detalhes_chamado",
            chamado_id=chamado_id
        )
    )


# REGISTRO DE SOLUÇÃO
@app.route(
    "/chamado/<int:chamado_id>/solucao",
    methods=("POST",)
)
@login_required
def registrar_solucao(chamado_id):

    if session["usuario_perfil"] != "analista":

        return "Acesso não autorizado.", 403

    descricao = request.form["descricao"].strip()

    if not descricao:

        return redirect(
            url_for(
                "detalhes_chamado",
                chamado_id=chamado_id
            )
        )

    connection = get_db_connection()

    chamado = connection.execute(
        """
        SELECT id
        FROM chamado
        WHERE id = ?
        """,
        (chamado_id,)
    ).fetchone()

    if chamado is None:

        connection.close()

        return "Chamado não encontrado.", 404

    connection.execute(
        """
        INSERT INTO solucao
        (
            descricao,
            chamado_id
        )
        VALUES (?, ?)
        """,
        (
            descricao,
            chamado_id
        )
    )

    connection.commit()
    connection.close()

    return redirect(
        url_for(
            "detalhes_chamado",
            chamado_id=chamado_id
        )
    )


if __name__ == "__main__":
    app.run(debug=True)