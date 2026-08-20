# Dicionário de Dados

## Tabela USUARIO

Armazena os usuários cadastrados no sistema.

| Campo | Tipo | Restrição | Descrição |
|---|---|---|---|
| id | INTEGER | PK, AUTOINCREMENT | Identificador único do usuário |
| nome | TEXT | NOT NULL | Nome do usuário |
| email | TEXT | NOT NULL, UNIQUE | E-mail utilizado para acesso |
| senha | TEXT | NOT NULL | Senha do usuário |
| perfil | TEXT | NOT NULL | Perfil de acesso do usuário |

Valores possíveis para `perfil`:

- usuario
- analista

---

## Tabela CATEGORIA

Armazena as categorias utilizadas na classificação dos chamados.

| Campo | Tipo | Restrição | Descrição |
|---|---|---|---|
| id | INTEGER | PK, AUTOINCREMENT | Identificador único da categoria |
| nome | TEXT | NOT NULL, UNIQUE | Nome da categoria |

Categorias utilizadas no sistema:

- Hardware
- Software
- Rede
- Acesso
- Impressão

---

## Tabela CHAMADO

Armazena os chamados registrados pelos usuários.

| Campo | Tipo | Restrição | Descrição |
|---|---|---|---|
| id | INTEGER | PK, AUTOINCREMENT | Identificador único do chamado |
| titulo | TEXT | NOT NULL | Título do chamado |
| descricao | TEXT | NOT NULL | Descrição do problema |
| prioridade | TEXT | NOT NULL | Prioridade do chamado |
| status | TEXT | NOT NULL | Status atual do chamado |
| data_abertura | TEXT | NOT NULL | Data e hora de abertura |
| data_fechamento | TEXT | NULL | Data e hora de fechamento |
| usuario_id | INTEGER | FK, NOT NULL | Usuário responsável pelo chamado |
| categoria_id | INTEGER | FK, NOT NULL | Categoria do chamado |

Valores possíveis para `prioridade`:

- Baixa
- Media
- Alta
- Critica

Valores possíveis para `status`:

- Aberto
- Em andamento
- Resolvido
- Fechado

---

## Tabela SOLUCAO

Armazena as soluções registradas pelos analistas.

| Campo | Tipo | Restrição | Descrição |
|---|---|---|---|
| id | INTEGER | PK, AUTOINCREMENT | Identificador único da solução |
| descricao | TEXT | NOT NULL | Descrição da solução aplicada |
| data_registro | TEXT | NOT NULL | Data e hora do registro |
| chamado_id | INTEGER | FK, NOT NULL | Chamado relacionado à solução |

---

## Relacionamentos

### USUARIO → CHAMADO

Um usuário pode possuir vários chamados.

```text
USUARIO 1 : N CHAMADO