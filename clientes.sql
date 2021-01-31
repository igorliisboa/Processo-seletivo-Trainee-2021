CREATE DATABASE loja;
USE loja;

CREATE TABLE cliente (
codigo char(10) NOT NULL PRIMARY KEY,
nome varchar(30) NOT NULL, 
razao_social varchar(30) NOT NULL,
cnpj char(10) NOT NULL,
data_inclusao datetime NOT NULL
);

describe cliente;