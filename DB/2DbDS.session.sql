/*
DDL - Definição - Estrutura - CREATE, DROP, ALTER
DML - Maninpulação dos dados - Criação dos resgistros das tabelas, INSERT, DELETE, UPDATE
DQL - Query - Dados - SELECT - 32 Variações

Select coluna1, coluna2;
From Tabela1,Tabela2;
Where ID = 1 

*/

USE U275872813_controle_gasto;

CREATE TABLE TB_USUARIO_DOMIENSE(
    ID INT PRIMARY KEY AUTO_INCREMENT,
    NOME VARCHAR(120) NOT NULL,
    EMAIL VARCHAR (120) UNIQUE,
    SENHA VARCHAR 255
);

INSERT into TB_USUARIO_PEDRO_DOMIENSE(NOME, EMAIL, SENHA) VALUES('Pedro Domiense dos Santos', 'pedrodomiense0505@gmail.com', 'senha321')

SELECT NOME, EMAIL, SENHA
FROM TB_USUARIO_DOMIENSE;
