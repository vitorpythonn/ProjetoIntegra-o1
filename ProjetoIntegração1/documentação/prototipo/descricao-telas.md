# Descrição das Telas

## Tela 01 — Login

A tela de login permite que usuários cadastrados acessem o sistema.

### Elementos

- Campo de e-mail;
- Campo de senha;
- Botão de acesso;
- Link para cadastro de novo usuário.

### Funcionalidade

O sistema valida as credenciais informadas e, quando válidas, permite o acesso às funcionalidades disponíveis para o perfil do usuário.

---

## Tela 02 — Cadastro de Usuário

A tela de cadastro permite a criação de novos usuários.

### Elementos

- Campo de nome;
- Campo de e-mail;
- Campo de senha;
- Botão de cadastro;
- Opção para retornar ao login.

### Funcionalidade

O sistema valida os dados informados e registra o novo usuário no banco de dados.

---

## Tela 03 — Abertura de Chamado

A tela de abertura permite que um usuário registre uma nova solicitação de suporte.

### Elementos

- Campo de título;
- Campo de descrição;
- Seleção de categoria;
- Seleção de prioridade;
- Botão para abrir o chamado;
- Botão para cancelar.

### Funcionalidade

Após o envio, o sistema valida os dados e registra o chamado no banco SQLite, associando-o ao usuário autenticado.

---

## Tela 04 — Consulta de Chamados

A tela de consulta apresenta os chamados registrados no sistema.

### Elementos

- Identificador do chamado;
- Título;
- Categoria;
- Prioridade;
- Status;
- Usuário;
- Data de abertura;
- Acesso aos detalhes do chamado;
- Opção para abrir um novo chamado;
- Opção para sair do sistema.

### Funcionalidade

O sistema consulta os chamados armazenados no banco de dados e apresenta as informações em formato de lista.

Usuários podem consultar seus chamados, enquanto analistas possuem acesso aos chamados destinados ao atendimento.