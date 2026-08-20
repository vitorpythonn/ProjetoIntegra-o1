
### 2. `casos-de-teste.md`

Coloque:

```markdown
# Casos de Teste

## CT01 — Login válido

**Objetivo:** Verificar se um usuário cadastrado consegue realizar login.

**Entrada:** E-mail e senha de um usuário existente.

**Resultado esperado:** O sistema deve autenticar o usuário e permitir o acesso à aplicação.

**Resultado obtido:** Teste aprovado.

**Status:** APROVADO

---

## CT02 — Cadastro de usuário

**Objetivo:** Verificar se um novo usuário pode ser cadastrado.

**Entrada:** Nome, e-mail e senha válidos.

**Resultado esperado:** O sistema deve cadastrar o usuário no banco de dados.

**Resultado obtido:** Teste aprovado.

**Status:** APROVADO

---

## CT03 — Abertura de chamado

**Objetivo:** Verificar se um usuário autenticado consegue registrar um chamado.

**Entrada:** Título, descrição, categoria e prioridade.

**Resultado esperado:** O sistema deve registrar o chamado no banco de dados e associá-lo ao usuário.

**Resultado obtido:** Teste aprovado.

**Status:** APROVADO

---

## CT04 — Consulta de chamados

**Objetivo:** Verificar se os chamados cadastrados podem ser consultados.

**Entrada:** Acesso à tela de consulta de chamados.

**Resultado esperado:** O sistema deve consultar o banco de dados e apresentar os chamados registrados.

**Resultado obtido:** Teste aprovado.

**Status:** APROVADO

---

## CT05 — Atualização e registro de solução

**Objetivo:** Verificar se um analista consegue atualizar o status de um chamado e registrar uma solução.

**Entrada:** Chamado existente, novo status e descrição da solução.

**Resultado esperado:** O sistema deve atualizar o status e registrar a solução vinculada ao chamado.

**Resultado obtido:** Teste aprovado.

**Status:** APROVADO

---

## Resumo dos resultados

| Teste | Descrição | Resultado |
|---|---|---|
| CT01 | Login válido | APROVADO |
| CT02 | Cadastro de usuário | APROVADO |
| CT03 | Abertura de chamado | APROVADO |
| CT04 | Consulta de chamados | APROVADO |
| CT05 | Atualização e registro de solução | APROVADO |

**Total de testes:** 5

**Testes aprovados:** 5

**Testes reprovados:** 0