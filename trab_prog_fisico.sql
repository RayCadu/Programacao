/* trab_prog_logico: */

CREATE TABLE CLIENTE (
    codigo serial PRIMARY KEY,
    FK_PESSOA_codigo integer
);

CREATE TABLE PRODUTO (
    codigo serial PRIMARY KEY,
    nome varchar(80),
    descricao varchar(255),
    valor float,
    FK_tipo_produto_tipo_produto_PK integer
);

CREATE TABLE MEIO_PAGAMENTO (
    codigo serial PRIMARY KEY,
    valor float,
    FK_tipo_pagamento_tipo_pagamento_PK integer,
    FK_COMPRA_codigo integer,
    numero_cartao bigint,
    data_validade_cartao char(5),
    cvv_cartao char(3),
    apelido_cartao varchar(25)
);

CREATE TABLE PESSOA (
    codigo serial PRIMARY KEY,
    nome varchar(250),
    telefone varchar(20),
    cpf varchar(14),
    FK_endereco_endereco_PK integer
);

CREATE TABLE ENTREGADOR (
    codigo serial PRIMARY KEY,
    FK_PESSOA_codigo integer
);

CREATE TABLE COMPRA (
    codigo serial PRIMARY KEY,
    FK_ENTREGADOR_codigo integer,
    FK_ENTREGADOR_FK_PESSOA_codigo integer
);

CREATE TABLE tipo_produto (
    descricao varchar(255),
    tipo_produto_PK serial PRIMARY KEY
);

CREATE TABLE tipo_pagamento (
    tipo_pagamento_PK serial NOT NULL PRIMARY KEY,
    descricao varchar(80)
);

CREATE TABLE endereco (
    cep bigint,
    logradouro varchar(255),
    numero integer,
    bairro integer,
    cidade integer,
    tipo_logradouro integer,
    endereco_PK serial PRIMARY KEY
);

CREATE TABLE Realiza (
    fk_COMPRA_codigo integer,
    fk_CLIENTE_codigo integer
);

CREATE TABLE Compra_produto (
    qtd integer,
    data_hora timestamp,
    fk_PRODUTO_codigo integer,
    fk_COMPRA_codigo integer
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
 
ALTER TABLE CLIENTE ADD CONSTRAINT FK_CLIENTE_PESSOA
    FOREIGN KEY (FK_PESSOA_codigo)
    REFERENCES pessoa (codigo);
 
ALTER TABLE PRODUTO ADD CONSTRAINT FK_PRODUTO_TIPO_PRODUTO
    FOREIGN KEY (FK_tipo_produto_tipo_produto_PK)
    REFERENCES tipo_produto (tipo_produto);
 
ALTER TABLE MEIO_PAGAMENTO ADD CONSTRAINT FK_MEIO_PAGAMENTO_TIPO_PAGAMENTO
    FOREIGN KEY (FK_tipo_pagamento_tipo_pagamento_PK)
    REFERENCES tipo_pagamento (tipo_pagamento_PK);
 
ALTER TABLE MEIO_PAGAMENTO ADD CONSTRAINT FK_MEIO_PAGAMENTO_COMPRA
    FOREIGN KEY (FK_COMPRA_codigo)
    REFERENCES compra (codigo);
 
ALTER TABLE PESSOA ADD CONSTRAINT FK_PESSOA_ENDERECO
    FOREIGN KEY (FK_endereco_endereco_PK)
    REFERENCES endereco (endereco_pk);
 
ALTER TABLE ENTREGADOR ADD CONSTRAINT FK_ENTREGADOR_PESSOA
    FOREIGN KEY (FK_PESSOA_codigo)
    REFERENCES PESSOA (codigo);
 
ALTER TABLE COMPRA ADD CONSTRAINT FK_COMPRA_ENTREGADOR
    FOREIGN KEY (fk_entregador_codigo)
    REFERENCES ENTREGADOR (codigo);
 
ALTER TABLE COMPRA ADD CONSTRAINT FK_COMPRA_PESSOA
    FOREIGN KEY (FK_ENTREGADOR_FK_PESSOA_codigo)
    REFERENCES CLIENTE (codigo);
 
ALTER TABLE endereco ADD CONSTRAINT FK_endereco_bairro
    FOREIGN KEY (bairro)
    REFERENCES BAIRRO (codigo);

ALTER TABLE endereco ADD CONSTRAINT FK_endereco_cidade
    FOREIGN KEY (cidade)
    REFERENCES CIDADE (codigo);

ALTER TABLE endereco ADD CONSTRAINT FK_endereco_tipo_logradouro
    FOREIGN KEY (tipo_logradouro)
    REFERENCES TIPO_LOGRADOURO (codigo);
 
ALTER TABLE Realiza ADD CONSTRAINT FK_Realiza_CLIENTE
    FOREIGN KEY (fk_CLIENTE_codigo)
    REFERENCES CLIENTE (codigo);
 
ALTER TABLE Realiza ADD CONSTRAINT FK_Realiza_COMPRA
    FOREIGN KEY (fk_COMPRA_codigo)
    REFERENCES COMPRA (codigo);
 
ALTER TABLE Compra_produto ADD CONSTRAINT FK_Compra_produto_PRODUTO
    FOREIGN KEY (fk_PRODUTO_codigo)
    REFERENCES PRODUTO (codigo);
 
ALTER TABLE Compra_produto ADD CONSTRAINT FK_Compra_produto_COMPRA
    FOREIGN KEY (fk_COMPRA_codigo)
    REFERENCES COMPRA (codigo);