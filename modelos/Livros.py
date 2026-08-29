from modelos.midia import Midia

class Livros(Midia):

    def __init__(self, titulo, ano, autor):
        super().__init__(titulo, ano)
        self.autor = autor

    def __str__(self):
        return super().__str__() + f'{self.autor.ljust(25)} | {self.disponivel}'

    @classmethod
    def listar_livros(cls):
        cabecalho = f'{'Titulo'.ljust(25)} | {'Ano'.ljust(25)} | {'Autor'.ljust(25)} | {'Disponivel'}'

        print(cabecalho)
        print('-' * len(cabecalho))

        for livro in cls.acervo_de_midia:
            if isinstance(livro, Livros):
                print(livro)
