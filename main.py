from modelos.Livros import Livros
from modelos.Filmes import Filmes
from modelos.Jogos import Jogos
from serviços.acervo import carregar_acervo, salvar_acervo

import os
largura = os.get_terminal_size().columns

def limpar_tela():
    input('pressione uma tecla para continuar: ')
    os.system('cls')


def menu():
    os.system('cls')
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
    5 - Menu de empréstimo de itens
    6 - Sair
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
    input('clique para ENTER retornar ao menu')
    os.system('cls')

def cadastro_de_itens(tipo_de_midia):
    os.system('cls')
    if tipo_de_midia == 1:
        titulo_do_livro_usuario = input('Qual o titulo do seu livro? ')
        print('|')
        autor_do_livro_usuario = input('Qual o autor do seu livro? ')
        print('|')
        ano_do_livro_usuario = (input('Qual ano seu livro foi publicado? '))
        print('|')
        livro_do_usuario = Livros(titulo_do_livro_usuario, autor_do_livro_usuario, ano_do_livro_usuario)
        print(f'Seu livro "{livro_do_usuario.titulo}" foi cadastrado com sucesso no sistema')
        input('Pressione ENTER para voltar ao menu')
    elif tipo_de_midia == 2:
        titulo_do_jogo_do_usuario = input('Qual o titulo do seu jogo? ')
        print('|')
        genero_do_jogo_do_usuario = input('Qual o genero do seu jogo? ')
        print('|')
        ano_do_jogo_do_usuario = (input('Qual o ano que seu jogo foi lançado? '))
        print('|')
        desenvolvedora_do_jogo_do_usuario = input('Qual a desenvolvedora do seu jogo? ')
        print('|')
        jogo_do_usuario = Jogos(titulo_do_jogo_do_usuario, genero_do_jogo_do_usuario, ano_do_jogo_do_usuario, desenvolvedora_do_jogo_do_usuario)
        print(f'Seu jogo "{jogo_do_usuario.titulo}" foi cadastrado com sucesso no sistema')
        input('Pressione ENTER para voltar ao menu')
    elif tipo_de_midia == 3:
        titulo_do_filme_do_usuario = input('Qual o titulo do seu filme? ')
        print('|')
        genero_do_filme_do_usuario = input('Qual o genero do seu filme? ')
        print('|')
        ano_do_filme_do_usuario = input('Qual o ano que seu filme foi lançado? ')
        print('|')
        durucao_do_filme_do_usuario = input('Qual a duração do seu filme? ')
        print('|')
        filme_do_usuario = Filmes(titulo_do_filme_do_usuario, genero_do_filme_do_usuario, ano_do_filme_do_usuario, durucao_do_filme_do_usuario)
        print(f'Seu filme "{filme_do_usuario.titulo}" foi cadastrado com sucesso no sistema')
        input('Pressione ENTER para voltar ao menu')
    os.system('cls')
def menu_de_cadastro_de_itens():

    os.system('cls')
    while True:
        print('MENU DE CADASTRO DE ITENS'.center(largura, '-'))
        print('''ESCOLHA UMA OPÇÃO DE CADASTRO:
        1) CADASTRAR LIVROS
        2) CADASTRAR JOGOS
        3) CADASTRAR FILMES
        4) SAIR
        ''')

        escolha_de_opção = int(input('Digite o numero da opção desejada '))

        if escolha_de_opção == 1:
            cadastro_de_itens(1)
        elif escolha_de_opção == 2:
            cadastro_de_itens(2)
        elif escolha_de_opção == 3:
            cadastro_de_itens(3)
        elif escolha_de_opção == 4:
            os.system('cls')
            break
        else:
            print('opção invalida')
            input('Aperte ENTER para voltar ao menu')
            os.system('cls')


def processar_movimentacao(acervo, tipo_de_midia, listar_itens, nome_midia, devolver):
    os.system('cls')

    listar_itens()

    item_escolhido = input(f'Escreva o nome do {nome_midia} que deseja emprestar ou devolver: ')
    if not devolver:
        for item in acervo:
            if isinstance(item,tipo_de_midia):
                if item.titulo.lower() == item_escolhido.lower():

                    if item._disponivel:
                        item.emprestar_midia()
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

    elif devolver:
        for item in acervo:
                if isinstance(item,tipo_de_midia):
                    if item.titulo.lower() == item_escolhido.lower():
            
                        if not item._disponivel:
                            item.devolver_midia()
                            print(f'{nome_midia.upper()} DEVOLVIDO COM SUCESSO')
                            input('Pressione ENTER para continuar ')
                            os.system('cls')
                        else:
                            print(f'Este {nome_midia} não está emprestado')
                            input('pressione ENTER para tentar novamente')
                        break
        else:
            print(f'{nome_midia.capitalize()} não encontrado')
            input('Pressione ENTER para tentar novamente ')
            os.system('cls')

def emprestar_item():
    os.system('cls')
    while True:
        print('''MENU DE EMPRÉSTIMOS:
1) EMPRESTAR ITEM
2) DEVOLVER ITEM
3) VOLTAR AO MENU
        ''')
        try:
            escolha_do_cliente = int(input('Qual opção você deseja: '))

            if escolha_do_cliente == 1:
                while True:
                    os.system('cls')
                    print('''Midias disponiveis para empréstimo:
1) Livros
2) Jogos
3) Filmes
4) Voltar ao menu
                            ''')
                    try:
                        escolha_de_emprestimo = int(input('Qual midia você quer emprestar?'))
                        if escolha_de_emprestimo == 1:
                            processar_movimentacao(Livros.acervo_de_midia, Livros, Livros.listar_livros, 'Livro', False)
            
                        elif escolha_de_emprestimo == 2:
                            processar_movimentacao(Jogos.acervo_de_midia, Jogos, Jogos.listar_jogos, 'Jogo', False)
            
                        elif escolha_de_emprestimo == 3:
                            processar_movimentacao(Filmes.acervo_de_midia, Filmes, Filmes.listar_filmes, 'Filme', False)
            
                        elif escolha_de_emprestimo == 4:
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
            elif escolha_do_cliente == 2:
                while True:
                    os.system('cls')
                    print('''Midias disponiveis para devolução:
    1) Livros
    2) Jogos
    3) Filmes
    4) Voltar ao menu
                            ''')
                    try:
                        escolha_de_devolucao = int(input('Qual midia você quer devolver?'))
                        if escolha_de_devolucao == 1:
                            processar_movimentacao(Livros.acervo_de_midia, Livros, Livros.listar_livros, 'Livro', True)
            
                        elif escolha_de_devolucao == 2:
                            processar_movimentacao(Jogos.acervo_de_midia, Jogos, Jogos.listar_jogos, 'jogo', True)
            
                        elif escolha_de_devolucao == 3:
                            processar_movimentacao(Filmes.acervo_de_midia, Filmes, Filmes.listar_filmes, 'filme', True)
            
                        elif escolha_de_devolucao == 4:
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
            elif escolha_do_cliente == 3:
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
                menu_de_cadastro_de_itens()
            elif opção_escolhida == 2:
                listar_produto(1)
            elif opção_escolhida == 3:
                listar_produto(2)
            elif opção_escolhida == 4:
                listar_produto(3)
            elif opção_escolhida == 5:
                emprestar_item()
            elif opção_escolhida == 6:
                os.system('cls')
                salvar_acervo()
                print('Até mais...')
                break
            else:
                print('Digite o número de uma das opções')
                input('Pressione ENTER para voltar ao menu')
                os.system('cls')
        except ValueError:
            print('Digite o número de uma das opções')
            input('Pressione ENTER para voltar ao menu')
            os.system('cls')
carregar_acervo()
iniciar_programa()


