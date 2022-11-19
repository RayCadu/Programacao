INSERT INTO BAIRRO (descricao)
  VALUES('Praia do Canto'),
  ('Centro '),
  ('Jardim Camburi'),
  ('Parque Moscoso'),
  ('Jardim da Penha'),
  ('Enseada do Suá'),
  ('Hungralândia'),
  ('Ferrero'),
  ('Vila Nova'),
  ('Altos');
  
INSERT INTO CIDADE (descricao)
  VALUES('Vidente'),
  ('Vila Boa'),
  ('Goiabada'),
  ('Pequena Brasília'),
  ('Bairro Grande'),
  ('Terra Seca'),
  ('Capivara'),
  ('Praia Grande'),
  ('Praia Pequena'),
  ('Prainha');
  
INSERT INTO TIPO_LOGRADOURO (descricao)
  VALUES('aeroporto'),
  ('alameda'),
  ('área'),
  ('avenida'),
  ('chácara'),
  ('ladeira'),
  ('morro'),
  ('condomínio'),
  ('parque'),
  ('rodovia');
  
INSERT INTO endereco (cep,logradouro,numero,bairro,cidade,tipo_logradouro,complemento)
  VALUES(18278,'Quero-Quero',23,3,6,6,'casa'),
  (17643,'Presidente Médici',78,3,6,6,'casa'),
  (23425,'Siriema',10,3,6,6,'casa'),
  (27592,'Pé de moleque',55,7,3,7,'apartamento'),
  (38163,'Queixada',90,4,5,5,'casa'),
  (10924,'Canarinho',27,6,7,1,'casa'),
  (13536,'João Neiva',85,8,4,10,'apartamento'),
  (13576,'Arnaldo Neves',24,1,2,3,'casa'),
  (18936,'Papagaio',37,9,9,6,'casa'),
  (19735,'Sol da manhã',62,10,10,8,'casa'),
  (29483,'Vista Linda',14,1,3,5,'casa'),
  (28423,'Paisagem',38,4,3,6,'apartamento'),
  (26132,'Canarinho',10,5,7,10,'apartamento'),
  (20222,'Parquinho',48,6,4,8,'casa');
  
INSERT INTO PESSOA (nome,username,telefone,cpf,senha,fk_endereco_codigo)
  VALUES('admin_cliente','admin_cliente','99824-2421','111.111.111-00','senha1234',1),
  ('admin_entregador','admin_entregador','99824-2321','222.222.222-00','senha1234',2),
  ('admin_funcionario','admin_funcionario','99824-2322','333.333.333-00','senha1234',3),
  ('Roberto','Robertinho','94285-5256','444.444.444-00','rober123',4),
  ('Carlos Eduardo','Carlitos','91424-2412','555.555.555-00','car123',5),
  ('Luiz Herinque','Lewis','91842-1324','636.636.636-00','Lewis123',6),
  ('Eduardo','Eduzin','91825-0245','777.777.777-00','Edu123',7),
  ('Fernando','Fenan','92535-2535','888.888.888-00','Fenan123',8),
  ('Lucas Oliveira','Luquinhas','91248-3024','999.999.999-00','Luc123',9),
  ('Matheus','Math','92742-0253','101.101.101-00','Math123',10),
  ('Juliano','Jul','98252-2532','202.202.202-00','Jul123',11),
  ('Carlos Herinque','Carhen','92754-2452','303.303.303-00','carh123',12),
  ('Alberto','Albertinho','91382-0422','404.404.404-00','alb123',13),
  ('Francisco','Fran','92453-2435','505.505.505-00','Fran123',14);
  
  
INSERT INTO CLIENTE(FK_PESSOA_username)
  VALUES('admin_cliente'),
  ('Robertinho'),
  ('Carlitos'),
  ('Lewis'),
  ('Eduzin'),
  ('Fenan'),
  ('Luquinhas'),
  ('Math');
  
INSERT INTO ENTREGADOR(salario,FK_PESSOA_username)
  VALUES(1500,'admin_entregador'),
  (1800,'Jul'),
  (1640,'Carhen');
  
INSERT INTO FUNCIONARIO(salario,chave_acesso,FK_PESSOA_username)
  VALUES(2300,'func1','admin_funcionario'),
  (2400,'func2','Albertinho'),
  (2500,'func3','Fran');

INSERT INTO TIPO_PRODUTO(descricao)
  VALUES('Lanche'),
  ('Porção'),
  ('Bebida');

INSERT INTO PRODUTO (nome,descricao,valor,FK_tipo_produto_tipo_produto_pk)
  VALUES('X-burguer','2 hambúrgueres - pão - maionese - queijo - batata palha',17,1),
  ('X-bacon','2 hambúrgures - pão - maionese - ketchup - queijo - bacon',20,1),
  ('X-tudo','2 hambúrgueres - pão - maionese - salada - batata palha - bacon - ovo',28,1),
  ('Batata frita','porção de batata de 300g',15,2),
  ('X-gourmet','3 hambúrgures - pão - maionese - ketchup - 2 queijos - bacon - salada - 2 presuntos',33,1),
  ('Refrigerante','temos refrigerante de todos os sabores, mas todos são latinha',7,3),
  ('Onion rings','porção de anéis de cebola de 150g',10,2);

INSERT INTO TIPO_PAGAMENTO(tipo_pagamento_pk)
  VALUES('Dinheiro'),
  ('Pix'),
  ('Cartão de Crédito'),
  ('Cartão de Débito');
