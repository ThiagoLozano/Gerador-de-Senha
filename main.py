import mysql.connector
from random import choice
from time import sleep


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

    def Criar_Login(self):
        print('=' * 30)
        print("{:^30}".format("CRIAR LOGIN"))
        nome = str(input('Nome: '))
        # Cria uma senha com base nos caracteres selecionados.
        valores = "ABCDEFGHIJKLMNOPQRTUVWXYZ1234567890"
        tamanho = 8
        senha = ''
        for c in range(tamanho):
            senha += choice(valores)
        print('Senha:', senha)

        # Valida se já existe esse Login e senha no banco de Dados.
        self.cursor.execute("""SELECT login, password 
                            FROM usuario
                            WHERE login = '{}' AND password = '{}'""".format(nome, senha))

        select = self.cursor.fetchall()
        for c in select:
            # Caso já exista no Banco de Dados.
            print("Login e Senha já cadastrado no sistema")
            self.Criar_Login()
        else:
            # Insere no Banco de Dados.
            self.cursor.execute("INSERT INTO usuario VALUES(DEFAULT, '{}', '{}')".format(nome, senha))
            sleep(2)
            print("\nCadastrado com sucesso!")
            sleep(2)
            self.Menu()

    def Logar(self):
        # Inserir nome + senha.
        # Validar entrada.
        # Emitir Mensagem.
        print('=' * 30)
        print("{:^30}".format("LOGAR"))
        nome = str(input("Nome: "))
        senha = str(input("Senha: "))
        print('=' * 30)

        self.cursor.execute("""SELECT login, password 
                                    FROM usuario
                                    WHERE login = '{}' AND password = '{}'""".format(nome, senha))

        select = self.cursor.fetchall()

        for c in select:
            # Caso já exista no Banco de Dados.
            print("Bem Vindo {}".format(nome))
        else:
            # Insere no Banco de Dados.
            print('Login ou senha inválido. Tente Novamente')
            self.Logar()

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


usuario = GeradorSenha()
usuario.Menu()
