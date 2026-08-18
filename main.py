import os
def limpar_tela():
    input('pressione uma tecla para continuar: ')
    os.system('cls')

class Livros:
    acervo_de_livros = []

    def __init__(self, título, autor, ano):

        self.título = título
        self.autor = autor
        self.ano = ano
        self._disponivel = True
        Livros.acervo_de_livros.append(self)

    @property
    def disponivel(self):
        return '✓' if self._disponivel else '☓'

    def __str__(self):
        return f'{self.título.ljust(25)} | {self.autor.ljust(25)} | {str(self.ano).ljust(25)} | {self.disponivel}'

    @classmethod
    def listar_livros(cls):
        cabecalho = f'{'Titulo'.ljust(25)} | {'Autor'.ljust(25)} | {'Ano'.ljust(25)} | {'Disponivel'}'

        print(cabecalho)
        print('-' * len(cabecalho))

        for livro in cls.acervo_de_livros:
            print(livro)
    
rock = Livros('fred', 'john', 1967)
pop = Livros('michael', 'tom', 1982)

def menu():
    print('''       Menu da MIDIATECA
    
    Escolha uma opção:
    1 - Cadastrar item
    2 - Listar catálogo de livros
    3 - Alugar item
    4 - Devolver item
    5 - Sair
    ''')

def listar_catálogo_de_livros():
    os.system('cls')
    print('LISTA DE LIVROS')
    Livros.listar_livros()
    print()
    input('Clique para voltar ao menu')
    os.system('cls')

def iniciar_programa():
    while True:
        menu()

        opção_escolhida = int(input('Escolha uma opção: '))

        if opção_escolhida == 1:
            cadastrar_item()
        elif opção_escolhida == 2:
            listar_catálogo_de_livros()
        elif opção_escolhida == 3:
            alugar_item()
        elif opção_escolhida == 4:
            devolver_item()
        elif opção_escolhida == 5:
            break

iniciar_programa()
