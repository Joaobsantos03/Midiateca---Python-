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
                os.system('cls')
                Livros.listar_livros()
                livro_escolhido = input('escreva o nome do livro que deseja emprestar:')
                for livro in Livros.acervo_de_livros:
                    if livro.titulo.lower() == livro_escolhido.lower():
                        if livro._disponivel:
                            livro.emprestar_livro()
                            print('LIVRO EMPRESTADO COM SUCESSO')
                            input('Pressione ENTER para voltar ao menu ')
                            os.system('cls')
                            break
                else:
                    os.system('cls')
                    print('este livro não pode ser emprestado ou não pode ser encontrado')
                    input('Pressione ENTER tentar novamente ')
                    os.system('cls')

            elif escolha_do_cliente == 2:
                os.system('cls')
                Jogos.listar_jogos()
                jogo_escolhido = input('escreva o nome do jogo que deseja emprestar:')
                for jogo in Jogos.acervo_de_jogos:
                    if jogo.titulo.lower() == jogo_escolhido.lower():
                        if jogo._disponivel:
                            jogo.emprestar_jogo()
                            print('JOGO EMPRESTADO COM SUCESSO')
                            input('Pressione ENTER para voltar ao menu ')
                            os.system('cls')
                            break
                else:
                    os.system('cls')
                    print('este jogo não pode ser emprestado ou não pode ser encontrado')
                    input('Pressione ENTER tentar novamente ')
                    os.system('cls')
            elif escolha_do_cliente == 3:
                os.system('cls')
                Filmes.listar_filmes()
                filme_escolhido = input('escreva o nome do filme que deseja emprestar:')
                for filme in Filmes.acervo_de_filmes:
                    if filme.titulo.lower() == filme_escolhido.lower():
                        if filme._disponivel:
                            filme.emprestar_filme()
                            print('FILME EMPRESTADO COM SUCESSO')
                            input('Pressione ENTER para voltar ao menu ')
                            os.system('cls')
                            break
                else:
                    os.system('cls')
                    print('este Filme não pôde ser emprestado ou não pôde ser encontrado')
                    input('Pressione ENTER tentar novamente ')
                    os.system('cls')

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
