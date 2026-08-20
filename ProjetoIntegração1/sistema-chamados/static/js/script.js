document.addEventListener("DOMContentLoaded", function () {

    const chamadoForm = document.getElementById("chamado-form");

    if (chamadoForm) {
        chamadoForm.addEventListener("submit", function (event) {

            const titulo = document.getElementById("titulo").value.trim();
            const descricao = document.getElementById("descricao").value.trim();
            const categoria = document.getElementById("categoria_id").value;
            const prioridade = document.getElementById("prioridade").value;

            if (!titulo || !descricao || !categoria || !prioridade) {
                event.preventDefault();

                alert("Preencha todos os campos obrigatórios.");
            }
        });
    }

});