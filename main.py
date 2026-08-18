import os
def limpar_tela():
    input('pressione uma tecla para continuar: ')
    os.system('cls')

class Jogos:

    acervo_de_jogos = []

    def __init__(self, titulo, gênero, ano, desenvolvedora):

        self.titulo = titulo.title()
        self.gênero = gênero.upper()
        self.ano = ano
        self.desenvolvedora = desenvolvedora.title
        self._disponivel = True
        Jogos.acervo_de_jogos.append(self)

    @property
    def disponivel(self):
            return '✓' if self._disponivel else '☓'

    def __str__(self):
        return f'{self.titulo.ljust(25)} | {self.gênero.ljust(25)} | {str(self.ano).ljust(25)} | {self.gênero.ljust(25)} | {self.disponivel}'

    @classmethod
    def listar_jogos(cls):
        cabecalho = f'{'titulo'.ljust(25)} | {'Gênero'.ljust(25)} | {'Ano'.ljust(25)} | {'Desenvolvedora'.ljust(25)} | {'Disponivel'}'

        print(cabecalho)
        print('-' * len(cabecalho))
        for jogos in cls.acervo_de_jogos:
            print(jogos)

class Livros:

    acervo_de_livros = []

    def __init__(self, titulo, autor, ano):

        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self._disponivel = True
        Livros.acervo_de_livros.append(self)

    @property
    def disponivel(self):
        return '✓' if self._disponivel else '☓'

    def __str__(self):
        return f'{self.titulo.ljust(25)} | {self.autor.ljust(25)} | {str(self.ano).ljust(25)} | {self.disponivel}'

    @classmethod
    def listar_livros(cls):
        cabecalho = f'{'Titulo'.ljust(25)} | {'Autor'.ljust(25)} | {'Ano'.ljust(25)} | {'Disponivel'}'

        print(cabecalho)
        print('-' * len(cabecalho))

        for livro in cls.acervo_de_livros:
            print(livro)
    
rock = Livros('fred', 'john', 1967)
pop = Livros('michael', 'tom', 1982)

mario = Jogos('Super mario', 'Plataforma', 1985, 'nintendo')
zelda = Jogos('The legend of zelda', 'rpg', 1998, 'nintendo')
def menu():
    print('''       Menu da MIDIATECA
    
    Escolha uma opção:
    1 - Cadastrar item
    2 - Listar catálogo de livros
    3 - Listar catálogo de jogos
    4 - Devolver item
    5 - Sair
    ''')

def listar_produto(escolha):
    if escolha == 1:
        os.system('cls')
        print('LISTA DE LIVROS')
        Livros.listar_livros()
        print()
    elif escolha == 2:
        os.system('cls')
        print('LISTA DE JOGOS')
        Jogos.listar_jogos()
        print()
    input('clique para retornar ao menu')
    os.system('cls')


def iniciar_programa():
    while True:
        menu()

        opção_escolhida = int(input('Escolha uma opção: '))

        if opção_escolhida == 1:
            cadastrar_item()
        elif opção_escolhida == 2:
            listar_produto(1)
        elif opção_escolhida == 3:
            listar_produto(2)
        elif opção_escolhida == 4:
            devolver_item()
        elif opção_escolhida == 5:
            break

iniciar_programa()
