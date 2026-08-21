class Livros:

    acervo_de_livros = []

    def __init__(self, titulo, autor, ano):

        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self._disponivel = True
        Livros.acervo_de_livros.append(self)

    @property
    def disponivel(self):
        return '✓' if self._disponivel else '☓'

    def __str__(self):
        return f'{self.titulo.ljust(25)} | {self.autor.ljust(25)} | {str(self.ano).ljust(25)} | {self.disponivel}'

    @classmethod
    def listar_livros(cls):
        cabecalho = f'{'Titulo'.ljust(25)} | {'Autor'.ljust(25)} | {'Ano'.ljust(25)} | {'Disponivel'}'

        print(cabecalho)
        print('-' * len(cabecalho))

        for livro in cls.acervo_de_livros:
            print(livro)

    def emprestar_livro(self):
        self._disponivel = False

    def devolver_livro(self):
        self._disponivel = True