# Plano de Testes

## Objetivo

Verificar o funcionamento das principais funcionalidades implementadas no Sistema de Controle de Chamados de Suporte Técnico.

## Escopo

Os testes contemplam:

- autenticação de usuário;
- cadastro de usuário;
- abertura de chamado;
- consulta de chamados;
- atualização de chamado;
- registro de solução.

## Ambiente de Testes

| Item | Configuração |
|---|---|
| Sistema operacional | Windows |
| Linguagem | Python |
| Framework | Flask |
| Banco de dados | SQLite |
| Navegador | Navegador web |
| Testes automatizados | unittest |

## Critério de Aprovação

Um teste será considerado aprovado quando o comportamento obtido pelo sistema estiver de acordo com o resultado esperado definido no caso de teste.

## Execução

Os testes automatizados foram executados utilizando o comando:

```text
python -m unittest discover -s tests -v