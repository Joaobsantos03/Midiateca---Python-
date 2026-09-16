from modelos.midia import Midia

class Jogos(Midia):

    def __init__(self, titulo, ano, genero, desenvolvedora):
         super().__init__(titulo, ano)
         self.genero = genero
         self.desenvolvedora = desenvolvedora

    def __str__(self):
        return super().__str__() + f'{self.genero.ljust(35)} | {self.desenvolvedora.ljust(35)}  | {self.disponivel}'

    @classmethod
    def listar_jogos(cls):
        cabecalho = f'{'titulo'.ljust(35)} | {'Ano'.ljust(35)} | {'Gênero'.ljust(35)} | {'Desenvolvedora'.ljust(35)} | {'Disponivel'}'

        print(cabecalho)
        print('-' * len(cabecalho))

        for jogos in cls.acervo_de_midia:
            if isinstance(jogos,Jogos):
                print(jogos)

