# Plano de Testes

## 1. Objetivo

Verificar o funcionamento das principais funcionalidades implementadas no Sistema de Controle de Chamados de Suporte Técnico.

O plano tem como finalidade definir os procedimentos, critérios e ambiente utilizados para validação do sistema.

## 2. Escopo

Os testes contemplam as seguintes funcionalidades:

* autenticação de usuário;
* cadastro de usuário;
* abertura de chamado;
* consulta de chamados;
* atualização de chamado;
* registro de solução.

## 3. Ambiente de Testes

| Item                 | Configuração  |
| -------------------- | ------------- |
| Sistema operacional  | Windows       |
| Linguagem            | Python        |
| Framework            | Flask 3.1.3   |
| Banco de dados       | SQLite        |
| Interface            | Aplicação web |
| Testes automatizados | unittest      |

## 4. Estratégia de Testes

A validação foi realizada por meio de testes automatizados utilizando o framework `unittest`.

Os testes foram executados diretamente na aplicação e utilizaram o banco de dados SQLite para validar as operações implementadas.

Além dos testes automatizados, foram realizadas consultas ao banco de dados como evidência complementar para verificar a persistência dos dados.

## 5. Casos de Teste

Foram definidos cinco casos de teste:

| Código | Teste                             |
| ------ | --------------------------------- |
| CT01   | Login válido                      |
| CT02   | Cadastro de usuário               |
| CT03   | Abertura de chamado               |
| CT04   | Consulta de chamados              |
| CT05   | Atualização e registro de solução |

## 6. Critério de Aprovação

Um teste é considerado aprovado quando o comportamento obtido pelo sistema está de acordo com o resultado esperado definido no respectivo caso de teste.

Um teste é considerado reprovado quando o sistema apresenta comportamento diferente do resultado esperado ou ocorre um erro que impede a execução da funcionalidade.

## 7. Execução

Os testes automatizados foram executados a partir da pasta `sistema-chamados` utilizando o comando:

```text
python -m unittest discover -s tests -v
```

A execução apresentou o seguinte resultado:

```text
test_01_login_valido (test_app.SistemaChamadosTestCase.test_01_login_valido) ... ok
test_02_cadastro_usuario (test_app.SistemaChamadosTestCase.test_02_cadastro_usuario) ... ok
test_03_abertura_chamado (test_app.SistemaChamadosTestCase.test_03_abertura_chamado) ... ok
test_04_consulta_chamados (test_app.SistemaChamadosTestCase.test_04_consulta_chamados) ... ok
test_05_atualizacao_e_solucao (test_app.SistemaChamadosTestCase.test_05_atualizacao_e_solucao) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.956s

OK
```

## 8. Resultado

Os cinco casos de teste foram executados com sucesso.

Foram obtidos os seguintes resultados:

* 5 testes executados;
* 5 testes aprovados;
* 0 testes reprovados;
* 100% de aprovação;
* tempo de execução de 0.956 segundos.

As consultas realizadas diretamente no banco SQLite foram utilizadas como evidência complementar para verificar a persistência dos registros gerados durante a utilização do sistema.

## 9. Evidências

As evidências dos testes estão documentadas no arquivo `evidencias.md`, localizado no diretório `documentação/testes/`.

O documento apresenta o resultado da execução dos testes automatizados, consultas realizadas no banco SQLite e as evidências visuais relacionadas às telas da aplicação.

As imagens das telas são consideradas evidências visuais da interface e não substituem a validação funcional realizada pelos testes automatizados e pelas consultas ao banco de dados.
