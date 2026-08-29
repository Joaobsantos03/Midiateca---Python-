from modelos.midia import Midia

class Filmes(Midia):

    def __init__(self, titulo, ano, genero, duracao):
         super().__init__(titulo, ano)
         self.genero = genero
         self.duracao = duracao

    def __str__(self):
        return super().__str__() + f'{self.genero.ljust(25)} | {str(self.duracao).ljust(25)} | {self.disponivel}' 

    @classmethod
    def listar_filmes(cls):
        cabecalho = f'{'Titulo'.ljust(25)} | {'Ano'.ljust(25)} | {'Gênero'.ljust(25)} | {'Duração'.ljust(25)} | {'Disponivel'}'
    
        print(cabecalho)
        print('-' * len(cabecalho))

        for filmes in cls.acervo_de_midia:
            if isinstance(filmes,Filmes):
                print(filmes)
