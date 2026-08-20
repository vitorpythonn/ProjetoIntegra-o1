import sqlite3
import tempfile
import unittest
from pathlib import Path

import app


class SistemaChamadosTestCase(unittest.TestCase):

    def setUp(self):
        self.database_file = tempfile.NamedTemporaryFile(
            suffix=".db",
            delete=False
        )

        self.database_path = Path(self.database_file.name)

        self.database_file.close()

        connection = sqlite3.connect(self.database_path)

        connection.execute("PRAGMA foreign_keys = ON")

        connection.executescript("""
            CREATE TABLE usuario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                senha TEXT NOT NULL,
                perfil TEXT NOT NULL DEFAULT 'usuario'
            );

            CREATE TABLE categoria (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL UNIQUE
            );

            CREATE TABLE chamado (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descricao TEXT NOT NULL,
                prioridade TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'Aberto',
                data_abertura TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                data_fechamento TEXT,
                usuario_id INTEGER NOT NULL,
                categoria_id INTEGER NOT NULL,
                FOREIGN KEY (usuario_id) REFERENCES usuario(id),
                FOREIGN KEY (categoria_id) REFERENCES categoria(id)
            );

            CREATE TABLE solucao (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL,
                data_registro TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                chamado_id INTEGER NOT NULL,
                FOREIGN KEY (chamado_id) REFERENCES chamado(id)
            );

            INSERT INTO categoria (nome)
            VALUES ('Hardware');

            INSERT INTO categoria (nome)
            VALUES ('Software');

            INSERT INTO usuario
            (nome, email, senha, perfil)
            VALUES
            ('Usuario Teste', 'usuario@teste.com', '123456', 'usuario');

            INSERT INTO usuario
            (nome, email, senha, perfil)
            VALUES
            ('Analista Teste', 'analista@teste.com', '123456', 'analista');
        """)

        connection.commit()
        connection.close()

        self.original_database = app.get_db_connection

        def test_database_connection():
            connection = sqlite3.connect(self.database_path)
            connection.row_factory = sqlite3.Row
            connection.execute("PRAGMA foreign_keys = ON")
            return connection

        app.get_db_connection = test_database_connection

        app.app.config["TESTING"] = True

        self.client = app.app.test_client()

    def tearDown(self):
        app.get_db_connection = self.original_database

        if self.database_path.exists():
            self.database_path.unlink()

    def login(self, email, senha):
        return self.client.post(
            "/login",
            data={
                "email": email,
                "senha": senha
            },
            follow_redirects=True
        )

    def test_01_login_valido(self):
        response = self.login(
            "usuario@teste.com",
            "123456"
        )

        self.assertEqual(response.status_code, 200)

        self.assertIn(
            b"Chamados",
            response.data
        )

    def test_02_cadastro_usuario(self):
        response = self.client.post(
            "/cadastro",
            data={
                "nome": "Novo Usuario",
                "email": "novo@teste.com",
                "senha": "123456"
            },
            follow_redirects=True
        )

        self.assertEqual(response.status_code, 200)

        connection = app.get_db_connection()

        usuario = connection.execute(
            """
            SELECT *
            FROM usuario
            WHERE email = ?
            """,
            ("novo@teste.com",)
        ).fetchone()

        connection.close()

        self.assertIsNotNone(usuario)

    def test_03_abertura_chamado(self):
        self.login(
            "usuario@teste.com",
            "123456"
        )

        response = self.client.post(
            "/chamado",
            data={
                "titulo": "Computador com problema",
                "descricao": "Computador não liga.",
                "prioridade": "Alta",
                "categoria_id": "1"
            },
            follow_redirects=True
        )

        self.assertEqual(response.status_code, 200)

        connection = app.get_db_connection()

        chamado = connection.execute(
            """
            SELECT *
            FROM chamado
            WHERE titulo = ?
            """,
            ("Computador com problema",)
        ).fetchone()

        connection.close()

        self.assertIsNotNone(chamado)

        self.assertEqual(
            chamado["usuario_id"],
            1
        )

        self.assertEqual(
            chamado["categoria_id"],
            1
        )

    def test_04_consulta_chamados(self):
        self.login(
            "usuario@teste.com",
            "123456"
        )

        connection = app.get_db_connection()

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
                "Chamado para consulta",
                "Chamado utilizado no teste.",
                "Media",
                1,
                1
            )
        )

        connection.commit()
        connection.close()

        response = self.client.get("/chamados")

        self.assertEqual(
            response.status_code,
            200
        )

        self.assertIn(
            b"Chamado para consulta",
            response.data
        )

    def test_05_atualizacao_e_solucao(self):
        connection = app.get_db_connection()

        cursor = connection.execute(
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
                "Chamado do teste final",
                "Problema utilizado no teste.",
                "Alta",
                1,
                1
            )
        )

        chamado_id = cursor.lastrowid

        connection.commit()
        connection.close()

        self.login(
            "analista@teste.com",
            "123456"
        )

        response = self.client.post(
            f"/chamado/{chamado_id}/atualizar",
            data={
                "status": "Resolvido"
            },
            follow_redirects=True
        )

        self.assertEqual(
            response.status_code,
            200
        )

        response = self.client.post(
            f"/chamado/{chamado_id}/solucao",
            data={
                "descricao": "Problema solucionado durante o teste."
            },
            follow_redirects=True
        )

        self.assertEqual(
            response.status_code,
            200
        )

        connection = app.get_db_connection()

        chamado = connection.execute(
            """
            SELECT status
            FROM chamado
            WHERE id = ?
            """,
            (chamado_id,)
        ).fetchone()

        solucao = connection.execute(
            """
            SELECT descricao
            FROM solucao
            WHERE chamado_id = ?
            """,
            (chamado_id,)
        ).fetchone()

        connection.close()

        self.assertEqual(
            chamado["status"],
            "Resolvido"
        )

        self.assertIsNotNone(solucao)

        self.assertEqual(
            solucao["descricao"],
            "Problema solucionado durante o teste."
        )


if __name__ == "__main__":
    unittest.main()