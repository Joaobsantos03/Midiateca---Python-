from modelos.midia import Midia

class Jogos(Midia):

    def __init__(self, titulo, ano, genero, desenvolvedora):
         super().__init__(titulo, ano)
         self.genero = genero
         self.desenvolvedora = desenvolvedora

    def __str__(self):
        return super().__str__() + f'{self.genero.ljust(25)} | {self.desenvolvedora.ljust(25)}  | {self.disponivel}'

    @classmethod
    def listar_jogos(cls):
        cabecalho = f'{'titulo'.ljust(25)} | {'Ano'.ljust(25)} | {'Gênero'.ljust(25)} | {'Desenvolvedora'.ljust(25)} | {'Disponivel'}'

        print(cabecalho)
        print('-' * len(cabecalho))

        for jogos in cls.acervo_de_midia:
            if isinstance(jogos,Jogos):
                print(jogos)

