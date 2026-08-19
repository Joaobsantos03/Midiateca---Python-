from modelos.Livros import Livros
from modelos.Filmes import Filmes
from modelos.Jogos import Jogos
import os

def limpar_tela():
    input('pressione uma tecla para continuar: ')
    os.system('cls')

Harry_Potter = Livros('Harry Potter', 'J. K. Rowling', 1997)
senhor = Livros('O Senhor dos Aneis', 'J. R. R. Tolkien', 1954)

mario = Jogos('Super mario', 'Plataforma', 1985, 'nintendo')
zelda = Jogos('The legend of zelda', 'rpg', 1998, 'nintendo')

homem_de_ferro = Filmes('homem de ferro', 'ação/ficção científica', 2008, '2h 6m')
shrek_2 = Filmes('shrek 2', 'comédia/fantasia', 2001, '1h 29m')

def menu():
    print('''       
            ███╗   ███╗██╗██████╗ ██╗ █████╗ ████████╗███████╗ ██████╗ █████╗ 
            ████╗ ████║██║██╔══██╗██║██╔══██╗╚══██╔══╝██╔════╝██╔════╝██╔══██╗
            ██╔████╔██║██║██║  ██║██║███████║   ██║   █████╗  ██║     ███████║
            ██║╚██╔╝██║██║██║  ██║██║██╔══██║   ██║   ██╔══╝  ██║     ██╔══██║
            ██║ ╚═╝ ██║██║██████╔╝██║██║  ██║   ██║   ███████╗╚██████╗██║  ██║
            ╚═╝     ╚═╝╚═╝╚═════╝ ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝
                                                                  
    
    Escolha uma opção:
    1 - Cadastrar item
    2 - Listar catálogo de livros
    3 - Listar catálogo de jogos
    4 - Listar catálogo de filmes
    5 - Emprestar item
    6 - Devolver item
    7 - Sair
    ''')

def listar_produto(escolha):
    os.system('cls')
    if escolha == 1:
        print('LISTA DE LIVROS')
        Livros.listar_livros()
    elif escolha == 2:
        print('LISTA DE JOGOS')
        Jogos.listar_jogos()
    elif escolha == 3:
        print('LISTA DE FILMES')
        Filmes.listar_filmes()
    print()
    input('clique para retornar ao menu')
    os.system('cls')


def processar_emprestimo(acervo, listar_itens, metodo_emprestar, nome_midia):
    os.system('cls')

    listar_itens()

    item_escolhido = input(f'Escreva o nome do {nome_midia} que deseja emprestar: ')

    for item in acervo:
        if item.titulo.lower() == item_escolhido.lower():

            if item._disponivel:
                metodo_emprestar(item)
                print(f'{nome_midia.upper()} EMPRESTADO COM SUCESSO')
                input('Pressione ENTER para continuar ')
                os.system('cls')
            else:
                print(f'Este {nome_midia} já está emprestado')
                input('Pressione ENTER para tentar novamente ')
            break

    else:
        print(f'{nome_midia.capitalize()} não encontrado')
        input('Pressione ENTER para tentar novamente ')
        os.system('cls')
    

def emprestar_item():
    os.system('cls')
    while True:
        print('''Midias disponiveis:
        1) Livros
        2) Jogos
        3) Filmes
        4) Voltar ao menu
        ''')
        try:
            escolha_do_cliente = int(input('Qual midia você quer emprestar?'))
            if escolha_do_cliente == 1:
                processar_emprestimo(Livros.acervo_de_livros, Livros.listar_livros, Livros.emprestar_livro,'Livro')

            elif escolha_do_cliente == 2:
                processar_emprestimo(Jogos.acervo_de_jogos, Jogos.listar_jogos, Jogos.emprestar_jogo, 'jogo')

            elif escolha_do_cliente == 3:
                processar_emprestimo(Filmes.acervo_de_filmes, Filmes.listar_filmes, Filmes.emprestar_filme, 'filme')

            elif escolha_do_cliente == 4:
                os.system('cls')
                break
            else:
                print('Essa não é uma opção valida')
                input('Pressione ENTER para tentar novamente ')
                os.system('cls')
        except ValueError:
            print('Essa não é uma opção valida')
            input('Pressione ENTER para tentar novamente ')
            os.system('cls')

def iniciar_programa():
    while True:

        try:
            menu()
            opção_escolhida = int(input('Escolha uma opção: '))

            if opção_escolhida == 1:
                cadastrar_item()
            elif opção_escolhida == 2:
                listar_produto(1)
            elif opção_escolhida == 3:
                listar_produto(2)
            elif opção_escolhida == 4:
                listar_produto(3)
            elif opção_escolhida == 5:
                emprestar_item()
            elif opção_escolhida == 6:
                devolver_item()
            elif opção_escolhida == 7:
                break
            else:
                print('Digite o número de uma das opções')
                input('Pressione ENTER para voltar ao menu')
                os.system('cls')
        except ValueError:
            print('Digite o número de uma das opções')
            input('Pressione ENTER para voltar ao menu')
            os.system('cls')
iniciar_programa()
