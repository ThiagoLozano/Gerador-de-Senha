# PROJETO PYTHON: Gerador de Senhas

> Um sistema que cria uma senha para o usuário e armazena em um Banco de Dados.

   O programa deve mostrar um menu de Criar Login ou Logar, se a escolha for Criar um Login, o usuário deve 
inserir um nome e o sistema irá gerar a senha validando caso já exista o nome e senha cadastrados 
anteriormente no Banco de Dados, se a escolha for Logar, ele deve pedir o nome e senha e também efetuar a 
validação, estando correto, retorná uma mensagem de Bem vindo, caso contrário, uma mensagem de erro.

# Tecnologias Utilizadas
* **_PyCharm;_**
* **_Python 3;_**

# Exemplo de Uso
### Classe
```
class GeradorSenha:
    def __init__(self):
        # Cria a conexão com o BD.
        self.myBD = mysql.connector.connect(host="localhost",
                                            user="root",
                                            password="",
                                            database="login_python")

        # Cria um Cursor.
        self.cursor = self.myBD.cursor()
        self.cursor.execute('USE login_python')
```
![Classe]()

### Função Menu
```
    def Menu(self):
        # Mostra o Menu.
        print('=' * 30)
        print('''Bem Vindo ao Login Python
1) Logar
2) Criar Login
3) Sair''')
        print('=' * 30)
        # Valida a entrada de escolha.
        while True:
            try:
                escolha = int(input('Escolha: '))
                if escolha == 1:
                    self.Logar()
                    break
                elif escolha == 2:
                    self.Criar_Login()
                    break
                elif escolha == 3:
                    break
                else:
                    print("Entrada Inválida. Tente Novamente")
            except ValueError:
                print('Tipo de Dado Inválido. Tente Novamente\n')
```
![Menu]()

# Bibliotecas e Configurações

### Biblioteca Python Utilizada

```
import mysql.connector
from random import choice
from time import sleep
```
![Biblioteca]()

### Configurações

```
```
