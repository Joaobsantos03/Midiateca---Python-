import json
from modelos.Livros import Livros
from modelos.Jogos import Jogos
from modelos.Filmes import Filmes

def carregar_acervo():
    with open('dados/acervo.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)

    for item in dados:
        tipo_de_midia = item['tipo']

        if tipo_de_midia == 'livro':
            item = Livros(item['titulo'], item['ano'], item['autor'])

        elif tipo_de_midia == 'jogo':
            item = Jogos(item['titulo'], item['ano'], item['genero'], item['desenvolvedora'])

        elif tipo_de_midia == 'filme':
            item = Filmes(item['titulo'], item['ano'], item['genero'], item['duracao'])

