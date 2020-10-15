# PROJETO PYTHON: Gerador de Senhas

> Um sistema que cria uma senha para o usuário e armazena em um Banco de Dados.

   O programa deve mostrar um menu de Criar Login ou Logar, se a escolha for Criar um Login, o usuário deve 
inserir um nome e o sistema irá gerar a senha validando caso já exista o nome e senha cadastrados 
anteriormente no Banco de Dados, se a escolha for Logar, ele deve pedir o nome e senha e também efetuar a 
validação, estando correto, retorná uma mensagem de Bem vindo, caso contrário, uma mensagem de erro.

# Tecnologias Utilizadas
* **_PyCharm;_**
* **_Python 3;_**
* **_MySQL;_**
* **_WampServer;_**

# Exemplo de Uso
### Classe
```
class GeradorSenha:
    def __init__(self):
        # Cria a conexão com o Banco de Dados.
        self.mybd = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='login_python'
        )
        # Cria um cursor.
        self.my_cursor = self.mybd.cursor()
        self.senha = ''
```
![Classe](https://github.com/ThiagoLozano/Gerador-de-Senha/blob/master/Screenshot/Classe.PNG)

### Função Gerar Senha
```
    def Gerar_senha(self):
        valores = 'ABCDEFGHIJKLMOPQHRSTUVWYZ1234567890'
        tamanho_senha = 8
        self.senha = ''
        for c in range(tamanho_senha):
            self.senha += choice(valores)
        print("Senha Gerada: {}".format(self.senha))
```
![Gerar Senha](https://github.com/ThiagoLozano/Gerador-de-Senha/blob/master/Screenshot/Gerar_Senha.PNG)

### Banco de Dados
```
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
```
![Banco de Dados](https://github.com/ThiagoLozano/Gerador-de-Senha/blob/master/Screenshot/BD.PNG)

# Bibliotecas e Configurações

### Biblioteca Python Utilizada

```
import mysql.connector
from random import choice
from time import sleep
```
![Biblioteca](https://github.com/ThiagoLozano/Gerador-de-Senha/blob/master/Screenshot/Bibliotecas.PNG)
