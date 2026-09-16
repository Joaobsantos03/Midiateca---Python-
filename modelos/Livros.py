from modelos.midia import Midia

class Livros(Midia):

    def __init__(self, titulo, ano, autor):
        super().__init__(titulo, ano)
        self.autor = autor

    def __str__(self):
        return super().__str__() + f'{self.autor.ljust(35)} | {self.disponivel}'

    @classmethod
    def listar_livros(cls):
        cabecalho = f'{'Titulo'.ljust(35)} | {'Ano'.ljust(35)} | {'Autor'.ljust(35)} | {'Disponivel'}'

        print(cabecalho)
        print('-' * len(cabecalho))

        for livro in cls.acervo_de_midia:
            if isinstance(livro, Livros):
                print(livro)
