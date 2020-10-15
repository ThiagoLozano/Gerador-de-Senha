-- Cria o Banco de Dados.
CREATE DATABASE IF NOT EXISTS login_python;
USE login_python;

-- Cria a Tabela 'usuarios'.
CREATE TABLE IF NOT EXISTS usuarios(
id INT AUTO_INCREMENT,
nome CHAR(10) NOT NULL,
senha CHAR(8) NOT NULL,
PRIMARY KEY(id)
);

-- Insere um valor de exemplo.
INSERT INTO usuarios VALUES(DEFAULT, 'ADM', '12345678');

-- Retorna todos os registros da tabela 'usuarios';
SELECT * FROM usuarios;

-- Apaga todos os registros da tabela (se necessário).
DELETE FROM usuarios;
