# Descrição dos Casos de Uso

## Atores

### Usuário

Responsável por realizar seu cadastro, abrir chamados e consultar os chamados registrados.

### Analista

Responsável por consultar chamados, atualizar seus status e registrar as soluções aplicadas.

---

## UC01 — Cadastrar usuário

**Ator principal:** Usuário

**Objetivo:** Permitir que uma pessoa crie uma conta no sistema.

**Pré-condição:** O usuário não possui cadastro com o e-mail informado.

**Fluxo principal:**

1. O usuário acessa a tela de cadastro.
2. O sistema solicita nome, e-mail e senha.
3. O usuário informa os dados.
4. O sistema valida os campos.
5. O sistema verifica se o e-mail já está cadastrado.
6. O sistema registra o usuário no banco de dados.
7. O sistema redireciona o usuário para a tela de login.

**Fluxo alternativo:**

- Caso o e-mail já esteja cadastrado, o sistema informa que já existe um usuário com o e-mail informado.
- Caso algum campo obrigatório não seja preenchido, o sistema solicita o preenchimento.

---

## UC02 — Abrir chamado

**Ator principal:** Usuário

**Objetivo:** Registrar uma solicitação de suporte técnico.

**Pré-condição:** O usuário deve estar autenticado.

**Fluxo principal:**

1. O usuário acessa a opção de novo chamado.
2. O sistema apresenta o formulário.
3. O usuário informa título, descrição, categoria e prioridade.
4. O sistema valida os dados informados.
5. O sistema registra o chamado no banco de dados.
6. O sistema associa o chamado ao usuário autenticado.
7. O sistema apresenta a lista de chamados.

**Fluxo alternativo:**

- Caso algum campo obrigatório não seja preenchido, o sistema informa o erro e solicita a correção.

---

## UC03 — Consultar chamados

**Ator principal:** Usuário / Analista

**Objetivo:** Permitir a visualização dos chamados registrados.

**Pré-condição:** O usuário deve estar autenticado.

**Fluxo principal:**

1. O usuário acessa a tela de chamados.
2. O sistema consulta os registros no banco de dados.
3. O sistema apresenta os chamados disponíveis.
4. O usuário pode selecionar um chamado para visualizar seus detalhes.

**Regra de acesso:**

- Usuários comuns visualizam seus próprios chamados.
- Analistas podem consultar os chamados registrados no sistema.

---

## UC04 — Atualizar chamado

**Ator principal:** Analista

**Objetivo:** Atualizar o status de um chamado.

**Pré-condição:** O analista deve estar autenticado e possuir perfil de analista.

**Fluxo principal:**

1. O analista acessa a lista de chamados.
2. O analista seleciona um chamado.
3. O sistema apresenta os detalhes do chamado.
4. O analista seleciona um novo status.
5. O sistema valida o status informado.
6. O sistema atualiza o chamado no banco de dados.
7. O sistema apresenta o chamado com o novo status.

**Status disponíveis:**

- Aberto
- Em andamento
- Resolvido
- Fechado

---

## UC05 — Encerrar/registrar solução do chamado

**Ator principal:** Analista

**Objetivo:** Registrar a solução aplicada a um chamado.

**Pré-condição:** O analista deve estar autenticado e possuir perfil de analista.

**Fluxo principal:**

1. O analista acessa os detalhes do chamado.
2. O sistema apresenta o campo para registro da solução.
3. O analista informa a solução aplicada.
4. O sistema valida a descrição.
5. O sistema registra a solução no banco de dados.
6. A solução fica vinculada ao chamado.
7. O sistema apresenta o histórico de soluções registradas.

**Fluxo alternativo:**

- Caso a descrição da solução esteja vazia, o sistema não registra a solução.