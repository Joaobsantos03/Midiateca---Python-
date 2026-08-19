class Jogos:

    acervo_de_jogos = []

    def __init__(self, titulo, gênero, ano, desenvolvedora):

        self.titulo = titulo.title()
        self.gênero = gênero.upper()
        self.ano = ano
        self.desenvolvedora = desenvolvedora.title()
        self._disponivel = True
        Jogos.acervo_de_jogos.append(self)

    @property
    def disponivel(self):
            return '✓' if self._disponivel else '☓'

    def __str__(self):
        return f'{self.titulo.ljust(25)} | {self.gênero.ljust(25)} | {str(self.ano).ljust(25)} | {self.desenvolvedora.ljust(25)} | {self.disponivel}'

    @classmethod
    def listar_jogos(cls):
        cabecalho = f'{'titulo'.ljust(25)} | {'Gênero'.ljust(25)} | {'Ano'.ljust(25)} | {'Desenvolvedora'.ljust(25)} | {'Disponivel'}'

        print(cabecalho)
        print('-' * len(cabecalho))
        for jogos in cls.acervo_de_jogos:
            print(jogos)

    def emprestar_jogo(self):
        self._disponivel = False