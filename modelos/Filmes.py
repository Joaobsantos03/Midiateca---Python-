class Filmes:

    acervo_de_filmes = []

    def __init__(self, titulo, genero, ano, duracao):

        self.titulo = titulo.title()
        self.genero = genero.upper()
        self.ano = ano
        self.duracao = duracao
        self._disponivel = True
        Filmes.acervo_de_filmes.append(self)

    @property
    def disponivel(self):
        return '✓' if self._disponivel else '☓'

    def __str__(self):
            return f'{self.titulo.ljust(25)} | {self.genero.ljust(25)} | {str(self.ano).ljust(25)} | {self.duracao.ljust(25)} | {self.disponivel}'

    @classmethod
    def listar_filmes(cls):
        cabecalho = f'{'Titulo'.ljust(25)} | {'Gênero'.ljust(25)} | {'Ano'.ljust(25)} | {'Duração'.ljust(25)} | {'Disponivel'}'
    
        print(cabecalho)
        print('-' * len(cabecalho))
        for filmes in cls.acervo_de_filmes:
            print(filmes)

    def emprestar_filme(self):
        self._disponivel = False

    def devolver_filme(self):
        self._disponivel = True