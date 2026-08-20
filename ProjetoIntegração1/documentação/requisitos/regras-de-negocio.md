# Regras de Negócio

## RN01 — Perfil do usuário

Cada usuário deve possuir um perfil, podendo ser usuário comum ou analista.

## RN02 — Abertura de chamados

Somente usuários autenticados podem registrar novos chamados.

## RN03 — Associação do chamado

Cada chamado deve estar associado a um usuário e a uma categoria.

## RN04 — Status do chamado

Um chamado pode possuir os seguintes status:

- Aberto
- Em andamento
- Resolvido
- Fechado

## RN05 — Prioridade

Um chamado deve possuir uma das seguintes prioridades:

- Baixa
- Média
- Alta
- Crítica

## RN06 — Acesso administrativo

Somente usuários com perfil de analista podem atualizar o status dos chamados e registrar soluções.

## RN07 — Solução

Uma solução deve estar vinculada a um chamado existente.