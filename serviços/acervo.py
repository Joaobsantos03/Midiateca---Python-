import json
from modelos.Livros import Livros
from modelos.Jogos import Jogos
from modelos.Filmes import Filmes
from modelos.midia import Midia

def carregar_acervo():
    with open('dados/acervo.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)

    for item in dados:
        tipo_de_midia = item['tipo']

        if tipo_de_midia == 'livro':
            livro = Livros(item['titulo'], item['ano'], item['autor'])
            livro._disponivel = item['disponivel']

        elif tipo_de_midia == 'jogo':
            jogo = Jogos(item['titulo'], item['ano'], item['genero'], item['desenvolvedora'])
            jogo._disponivel = item['disponivel']  

        elif tipo_de_midia == 'filme':
            filme = Filmes(item['titulo'], item['ano'], item['genero'], item['duracao'])
            filme._disponivel = item['disponivel']
            

def salvar_acervo():
    dados_do_acervo = []

    for item in Midia.acervo_de_midia:
        if isinstance(item,Livros):
            dados_do_acervo.append({
                "tipo": "livro",
                "titulo": item.titulo,
                "ano": item.ano,
                "autor": item.autor,
                "disponivel": item._disponivel
            })
        elif isinstance(item,Jogos):
            dados_do_acervo.append({
                "tipo": "jogo",
                "titulo": item.titulo,
                "ano": item.ano,
                "genero": item.genero,
                "desenvolvedora": item.desenvolvedora,
                "disponivel": item._disponivel
            })
        elif isinstance(item,Filmes):
            dados_do_acervo.append({
                "tipo": "filme",
                "titulo": item.titulo,
                "ano": item.ano,
                "genero": item.genero,
                "duracao": item.duracao,
                "disponivel": item._disponivel
            })
                

    with open('dados/acervo.json', 'w', encoding='utf-8') as arquivo:
         json.dump(dados_do_acervo,arquivo,indent=4,ensure_ascii=False)


