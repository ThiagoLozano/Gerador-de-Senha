DROP DATABASE IF EXISTS login_python;
CREATE DATABASE login_python;
USE login_python;

CREATE TABLE IF NOT EXISTS usuario(
`id_login` INT NOT NULL AUTO_INCREMENT, 
`login` VARCHAR(10),
`password` CHAR(8),
PRIMARY KEY(`id_login`)
);

INSERT INTO usuario VALUES(DEFAULT, 'ADM','12345678');

SELECT * FROM usuario;
