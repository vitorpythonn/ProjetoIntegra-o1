PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS solucao;
DROP TABLE IF EXISTS chamado;
DROP TABLE IF EXISTS categoria;
DROP TABLE IF EXISTS usuario;

CREATE TABLE usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL,
    perfil TEXT NOT NULL DEFAULT 'usuario'
        CHECK (perfil IN ('usuario', 'analista'))
);

CREATE TABLE categoria (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE
);

CREATE TABLE chamado (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    descricao TEXT NOT NULL,
    prioridade TEXT NOT NULL
        CHECK (prioridade IN ('Baixa', 'Media', 'Alta', 'Critica')),
    status TEXT NOT NULL DEFAULT 'Aberto'
        CHECK (status IN ('Aberto', 'Em andamento', 'Resolvido', 'Fechado')),
    data_abertura TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    data_fechamento TEXT,
    usuario_id INTEGER NOT NULL,
    categoria_id INTEGER NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuario(id),
    FOREIGN KEY (categoria_id) REFERENCES categoria(id)
);

CREATE TABLE solucao (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL,
    data_registro TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    chamado_id INTEGER NOT NULL,
    FOREIGN KEY (chamado_id) REFERENCES chamado(id) ON DELETE CASCADE
);

CREATE INDEX idx_chamado_usuario ON chamado(usuario_id);
CREATE INDEX idx_chamado_categoria ON chamado(categoria_id);
CREATE INDEX idx_chamado_status ON chamado(status);
CREATE INDEX idx_solucao_chamado ON solucao(chamado_id);

INSERT INTO categoria (nome) VALUES
('Hardware'),
('Software'),
('Rede'),
('Acesso'),
('Impressão');

INSERT INTO usuario (nome, email, senha, perfil) VALUES
('Usuário Teste', 'usuario@teste.com', '123456', 'usuario'),
('Analista Teste', 'analista@teste.com', '123456', 'analista');

INSERT INTO chamado
(titulo, descricao, prioridade, status, usuario_id, categoria_id)
VALUES
('Computador não liga',
 'O computador do setor não apresenta sinal de energia.',
 'Alta',
 'Aberto',
 1,
 1);

INSERT INTO chamado
(titulo, descricao, prioridade, status, usuario_id, categoria_id)
VALUES
('Sistema lento',
 'O sistema apresenta lentidão durante o atendimento.',
 'Media',
 'Em andamento',
 1,
 2);

INSERT INTO solucao (descricao, chamado_id)
VALUES
('Chamado registrado para análise do equipamento.', 1);
