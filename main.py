import os

class Livros:
    acervo_de_livros = []
    def __init__(self, título, autor, ano):

        self.título = título
        self.autor = autor
        self.ano = ano
        self.disponivel = True
        Livros.acervo_de_livros.append(self)



def menu():
    print('''       Menu da MIDIATECA
    
    Escolha uma opção:
    1 - Cadastrar item
    2 - Listar catálogo
    3 - Alugar item
    4 - Devolver item
    5 - Sair
    ''')

def iniciar_programa():
    while True:
        menu()

        opção_escolhida = int(input('Escolha uma opção: '))

        if opção_escolhida == 1:
            cadastrar_item()
        elif opção_escolhida == 2:
            listar_catálogo()
        elif opção_escolhida == 3:
            alugar_item()
        elif opção_escolhida == 4:
            devolver_item()
        elif opção_escolhida == 5:
            break

iniciar_programa()

