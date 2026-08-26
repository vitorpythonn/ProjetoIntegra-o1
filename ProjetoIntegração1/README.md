# Sistema de Controle de Chamados de Suporte Técnico

Projeto desenvolvido para a disciplina de Projeto Integrado Interdisciplinar do curso de Análise e Desenvolvimento de Sistemas.

## Objetivo

Desenvolver um sistema web para registro, consulta e acompanhamento de chamados de suporte técnico.

## Tecnologias

* Python
* Flask 3.1.3
* SQLite
* HTML5
* CSS3
* JavaScript
* unittest
* Git e GitHub

## Funcionalidades

* Cadastro de usuários;
* Login e autenticação;
* Controle de acesso por perfil;
* Abertura de chamados;
* Classificação por categoria;
* Definição de prioridade;
* Consulta de chamados;
* Visualização dos detalhes;
* Atualização do status;
* Registro de soluções;
* Persistência dos dados em SQLite.

## Estrutura

```text
ProjetoIntegração1/

├── documentação/
│   ├── casos-de-uso/
│   ├── introducao/
│   ├── modelagem/
│   ├── prototipo/
│   ├── requisitos/
│   └── testes/
│
├── git/
│   └── comandos-utilizados.md
│
├── relatorio-final/
│
├── sistema-chamados/
│   ├── database/
│   │   ├── chamados.db
│   │   └── schema.sql
│   │
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   │
│   ├── templates/
│   │
│   ├── tests/
│   │   └── test_app.py
│   │
│   ├── app.py
│   ├── database.py
│   └── requirements.txt
│
└── README.md
```

## Banco de dados

O sistema utiliza SQLite para armazenamento dos dados. O banco está localizado em `sistema-chamados/database/chamados.db` e sua estrutura é definida no arquivo `sistema-chamados/database/schema.sql`.

O banco possui as tabelas `usuario`, `categoria`, `chamado` e `solucao`, relacionadas por chaves estrangeiras.

## Instalação

É necessário possuir Python instalado no computador.

Acesse o diretório da aplicação:

```powershell
cd C:\facul\ProjetoIntegração1\sistema-chamados
```

Instale as dependências:

```powershell
pip install -r requirements.txt
```

## Execução

Para iniciar a aplicação:

```powershell
python .\app.py
```

Após a inicialização, acesse:

```text
http://127.0.0.1:5000
```

## Testes

O projeto possui testes automatizados utilizando `unittest`.

Para executar os testes:

```powershell
python -m unittest discover -s tests -v
```

Na validação realizada, foram executados cinco testes, todos aprovados, sem falhas.

## Documentação

A documentação acadêmica está organizada no diretório `documentação/`, contendo informações sobre introdução, requisitos, casos de uso, modelagem, protótipos e testes.

Também estão disponíveis os diagramas do sistema, o Modelo Entidade-Relacionamento (MER), o dicionário de dados, o plano de testes, os casos de teste e as evidências da validação.

## Controle de versão

O projeto utiliza Git para controle de versão e GitHub para armazenamento do repositório remoto.

Os principais comandos utilizados durante o desenvolvimento estão documentados em:

```text
git/comandos-utilizados.md
```

## Objetivo acadêmico

O projeto foi desenvolvido para aplicar, de forma prática, conceitos de desenvolvimento de sistemas, banco de dados, desenvolvimento web, testes de software, modelagem de sistemas, documentação e controle de versão.
