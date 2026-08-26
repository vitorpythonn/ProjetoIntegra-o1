# Evidências dos Testes

## 1. Objetivo

As evidências têm como objetivo demonstrar a execução dos testes automatizados e a persistência dos dados utilizados pela aplicação no banco de dados SQLite. A validação funcional do sistema foi realizada principalmente por meio dos testes automatizados utilizando o framework `unittest`, enquanto as consultas diretas ao banco SQLite foram utilizadas como evidência complementar para verificar a persistência dos dados.

## 2. Ambiente de Testes

| Item                | Configuração           |
| ------------------- | ---------------------- |
| Sistema operacional | Windows                |
| Linguagem           | Python                 |
| Framework web       | Flask 3.1.3            |
| Banco de dados      | SQLite                 |
| Framework de testes | unittest               |
| Banco utilizado     | `database/chamados.db` |

## 3. Execução dos Testes Automatizados

Os testes foram executados a partir da pasta `sistema-chamados` utilizando o comando:

```text
python -m unittest discover -s tests -v
```

O resultado obtido durante a execução foi:

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

Foram executados cinco testes automatizados, abrangendo login, cadastro de usuário, abertura de chamado, consulta de chamados e atualização com registro de solução. Todos os testes foram aprovados, sem ocorrências de falha, resultando em 100% de aprovação na execução realizada, com tempo total de 0.956 segundos.


Dessa forma, os cinco testes foram executados com sucesso, sem testes reprovados, resultando em 100% de aprovação na execução realizada.

## 4. Evidência de Persistência dos Usuários

A persistência dos dados foi verificada diretamente no banco SQLite utilizando o comando:

```text
C:\sqllite3\sqlite3.exe .\database\chamados.db "SELECT id, nome, email, perfil FROM usuario;"
```

O resultado validado apresentou os usuários cadastrados:

```text
1 | Usuário Teste | usuario@teste.com | usuario
2 | Analista Teste | analista@teste.com | analista
3 | Vg | vg@teste.com | usuario
```

Essa consulta demonstra que os registros de usuários utilizados durante a validação foram persistidos na tabela `usuario`.

## 5. Evidência de Persistência dos Chamados

A persistência dos chamados também foi verificada diretamente no banco SQLite utilizando:

```text
C:\sqllite3\sqlite3.exe .\database\chamados.db "SELECT id, titulo, prioridade, status, usuario_id, categoria_id FROM chamado;"
```

O resultado validado apresentou:

```text
1 | Computador não liga | Alta | Aberto | 1 | 1
2 | Sistema lento | Media | Em andamento | 1 | 2
3 | Pc morreu | Critica | Aberto | 3 | 1
```

A consulta demonstra que os chamados foram armazenados no banco de dados juntamente com suas informações de prioridade, status, usuário responsável pelo registro e categoria relacionada.

## 6. Categorias Cadastradas

O banco de dados também possui categorias utilizadas na classificação dos chamados:

```text
Hardware
Software
Rede
Acesso
Impressão
```

Essas categorias são utilizadas durante a abertura dos chamados para permitir sua classificação.

## 7. Evidências Visuais

As imagens presentes no diretório `documentação/prototipo/` representam as principais telas da aplicação e servem como evidências visuais da interface desenvolvida.

Estão disponíveis as imagens referentes às telas de login, cadastro, abertura de chamado e consulta de chamados.

As imagens das telas não são utilizadas como comprovação isolada da execução dos testes. A validação funcional foi realizada por meio da execução real da aplicação, dos testes automatizados e das consultas ao banco de dados.

## 8. Resultado Final

A execução dos testes automatizados confirmou o funcionamento das principais operações avaliadas no projeto. Foram realizados cinco testes, todos aprovados, abrangendo login, cadastro de usuário, abertura de chamado, consulta de chamados e atualização com registro de solução.

As consultas realizadas diretamente no banco SQLite complementaram a validação ao demonstrar a persistência dos registros de usuários e chamados.

Dessa forma, as evidências registradas neste documento correspondem aos testes automatizados e às verificações realizadas durante a validação do sistema.
