import mysql.connector
from random import choice
from time import sleep


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

    # Gerador de senhas.
    def Gerar_senha(self):
        valores = 'ABCDEFGHIJKLMOPQHRSTUVWYZ1234567890'
        tamanho_senha = 8
        self.senha = ''
        for c in range(tamanho_senha):
            self.senha += choice(valores)
        print("Senha Gerada: {}".format(self.senha))

    # Logar.
    def Logar(self):
        print('=' * 30)
        print('{:^28}'.format('LOGAR'))
        print('=' * 30)
        # Pergunta para o usuário.
        nome_usuario = str(input('Digite seu nome: '))
        senha_usuario = str(input('Digite sua senha: '))
        sleep(1)

        # Valida a entrada no Banco de Dados.
        self.my_cursor.execute("SELECT * FROM usuarios")
        select = self.my_cursor.fetchall()
        for c in select:
            if nome_usuario in c[1] and senha_usuario in c[2]:
                print("\nLogin efetuado com sucesso!")
                print('Bem vindo: {}'.format(nome_usuario))
                break
        else:
            print("\n\033[31mErro: Nome ou Senha estão incorretos\033[m\n")
            sleep(2)
            self.Menu()

    # Criar Login.
    def Criar_Login(self):
        print('=' * 30)
        print('{:^28}'.format('CRIAR LOGIN'))
        print('=' * 30)
        # Pergunta para o usuário.
        nome_usuario = str(input('Digite seu nome: '))
        # Valida a quantidade de caracteres suportado no Banco de Dados.
        while len(nome_usuario) > 10:
            print("\033[31mErro: Máximo de Caracteres deve ser 10\033[m\n")
            nome_usuario = str(input('Digite seu nome: '))
        self.Gerar_senha()
        sleep(2)

        # Valida a entrada do Banco de Dados.
        self.my_cursor.execute("SELECT * FROM usuarios")
        select = self.my_cursor.fetchall()
        for c in select:
            if c[1] == nome_usuario and c[2] == self.senha:
                print("\n\033[31mErro: Login já registrado no sistema.\033[m")
                self.Criar_Login()
        else:
            self.my_cursor.execute("INSERT INTO usuarios VALUES(DEFAULT,'{}','{}')".format(nome_usuario, self.senha))
            print("\nLogin criado com sucesso!\n")
            sleep(2)
            self.Menu()

    # Menu.
    def Menu(self):
        print('='*30)
        print('{:^28}'.format('MENU'))
        print('='*30)
        print("""1) Logar
2) Criar Login
3) Sair""")
        # Valida a opção do usuário.
        while True:
            try:
                opcao = int(input("\nEscolha sua opção: "))
                if opcao == 1:
                    self.Logar()
                    break
                elif opcao == 2:
                    self.Criar_Login()
                    break
                elif opcao == 3:
                    break
                else:
                    print("\033[31mErro: Escolha inválida, tente novamente\033[m")
            except ValueError:
                print("\033[31mErro: Entrada inválida, tente novamente\033[m")


usuario = GeradorSenha()
usuario.Menu()
