DROP TABLE  IF EXISTS administra, bairro, cidade, cliente, cliente_compra, compra, compra_pagamento, compra_produto, endereco, entregador, funcionario, pagamento, pessoa, produto, tipo_logradouro, tipo_pagamento, tipo_produto cascade; 

CREATE TABLE PRODUTO (
    codigo serial PRIMARY KEY,
    nome varchar(80),
    descricao varchar(255),
    valor float,
    FK_tipo_produto_tipo_produto_PK integer
);

CREATE TABLE PAGAMENTO (
    codigo serial PRIMARY KEY,
    FK_tipo_pagamento_tipo_pagamento_PK integer,
    valor float
);

CREATE TABLE PESSOA (
    username varchar(25) PRIMARY KEY,
    nome varchar(250),
    telefone varchar(20),
    cpf varchar(14),
    senha varchar(25),
    fk_endereco_codigo integer
);

CREATE TABLE FUNCIONARIO (
    codigo serial,
    salario float,
    chave_acesso varchar(30),
    FK_PESSOA_username varchar(25),
    PRIMARY KEY (codigo)
);

CREATE TABLE COMPRA (
    codigo serial PRIMARY KEY,
    data_hora timestamp,
    estado varchar(15),
    FK_ENTREGADOR_codigo integer
);

CREATE TABLE CLIENTE (
    codigo serial,
    cupom varchar(10),
    FK_PESSOA_username varchar(25),
    PRIMARY KEY (codigo)
);

CREATE TABLE ENTREGADOR (
    codigo serial,
    salario float,
    FK_PESSOA_username varchar(25),
    PRIMARY KEY (codigo)
);

CREATE TABLE tipo_produto (
    descricao varchar(80),
    tipo_produto_PK serial PRIMARY KEY
);

CREATE TABLE tipo_pagamento (
    tipo_pagamento_PK integer NOT NULL PRIMARY KEY,
    tipo_pagamento integer
);

CREATE TABLE endereco (
    codigo serial PRIMARY KEY,
    cep char(9),
    logradouro varchar(100),
    numero integer,
    bairro integer,
    cidade integer,
    tipo_logradouro integer,
    complemento varchar(100)
);

CREATE TABLE COMPRA_PAGAMENTO (
    fk_COMPRA_codigo integer,
    fk_PAGAMENTO_codigo integer
);

CREATE TABLE CLIENTE_COMPRA (
    fk_COMPRA_codigo integer,
    fk_CLIENTE_codigo integer
);

CREATE TABLE Compra_produto (
    fk_COMPRA_codigo integer,
    qtd integer,
    fk_PRODUTO_codigo integer
);

CREATE TABLE administra (
    fk_FUNCIONARIO_codigo integer,
    fk_PRODUTO_codigo integer
);

CREATE TABLE BAIRRO (
    codigo serial PRIMARY KEY,
    descricao varchar(80)
);

CREATE TABLE CIDADE (
    codigo serial PRIMARY KEY,
    descricao varchar(80)
);

CREATE TABLE TIPO_LOGRADOURO (
    codigo serial PRIMARY KEY,
    descricao varchar(80)
);
 
ALTER TABLE PRODUTO ADD CONSTRAINT FK_PRODUTO_TIPO_PRODUTO
    FOREIGN KEY (FK_tipo_produto_tipo_produto_PK)
    REFERENCES tipo_produto (tipo_produto_PK);
 
ALTER TABLE PAGAMENTO ADD CONSTRAINT FK_PAGAMENTO_TIPO_PAGAMENTO
    FOREIGN KEY (FK_tipo_pagamento_tipo_pagamento_PK)
    REFERENCES tipo_pagamento (tipo_pagamento_PK);
 
ALTER TABLE PESSOA ADD CONSTRAINT FK_PESSOA_ENDERECO
    FOREIGN KEY (fk_endereco_codigo)
    REFERENCES endereco (codigo);
 
ALTER TABLE FUNCIONARIO ADD CONSTRAINT FK_FUNCIONARIO_PESSOA
    FOREIGN KEY (FK_PESSOA_username)
    REFERENCES PESSOA (username);
 
ALTER TABLE COMPRA ADD CONSTRAINT FK_COMPRA_ENTREGADOR
    FOREIGN KEY (FK_ENTREGADOR_codigo)
    REFERENCES ENTREGADOR (codigo);
 
ALTER TABLE CLIENTE ADD CONSTRAINT FK_CLIENTE_PESSOA
    FOREIGN KEY (FK_PESSOA_username)
    REFERENCES PESSOA (username);

ALTER TABLE ENTREGADOR ADD CONSTRAINT FK_ENTREGADOR_PESSOA
    FOREIGN KEY (FK_PESSOA_username)
    REFERENCES PESSOA (username);
 
ALTER TABLE endereco ADD CONSTRAINT FK_endereco_BAIRRO
    FOREIGN KEY (bairro)
    REFERENCES BAIRRO (codigo);

ALTER TABLE endereco ADD CONSTRAINT FK_endereco_CIDADE
    FOREIGN KEY (cidade)
    REFERENCES CIDADE (codigo);

ALTER TABLE endereco ADD CONSTRAINT FK_endereco_TIPO_LOGRADOURO
    FOREIGN KEY (tipo_logradouro)
    REFERENCES TIPO_LOGRADOURO (codigo);
 
ALTER TABLE COMPRA_PAGAMENTO ADD CONSTRAINT FK_COMPRA_PAGAMENTO_PAGAMENTO
    FOREIGN KEY (fk_PAGAMENTO_codigo)
    REFERENCES PAGAMENTO (codigo);
 
ALTER TABLE COMPRA_PAGAMENTO ADD CONSTRAINT FK_COMPRA_PAGAMENTO_COMPRA
    FOREIGN KEY (fk_COMPRA_codigo)
    REFERENCES COMPRA (codigo);
 
ALTER TABLE CLIENTE_COMPRA ADD CONSTRAINT FK_CLIENTE_COMPRA_COMPRA
    FOREIGN KEY (fk_COMPRA_codigo)
    REFERENCES COMPRA (codigo);
 
ALTER TABLE CLIENTE_COMPRA ADD CONSTRAINT FK_CLIENTE_COMPRA_CLIENTE
    FOREIGN KEY (fk_CLIENTE_codigo)
    REFERENCES CLIENTE (codigo);
 
ALTER TABLE Compra_produto ADD CONSTRAINT FK_Compra_produto_PRODUTO
    FOREIGN KEY (fk_PRODUTO_codigo)
    REFERENCES PRODUTO (codigo);
 
ALTER TABLE Compra_produto ADD CONSTRAINT FK_Compra_produto_COMPRA
    FOREIGN KEY (fk_COMPRA_codigo)
    REFERENCES COMPRA (codigo);
 
ALTER TABLE administra ADD CONSTRAINT FK_administra_FUNCIONARIO
    FOREIGN KEY (fk_FUNCIONARIO_codigo)
    REFERENCES FUNCIONARIO (codigo);
 
ALTER TABLE administra ADD CONSTRAINT FK_administra_PRODUTO
    FOREIGN KEY (fk_PRODUTO_codigo)
    REFERENCES PRODUTO (codigo);
