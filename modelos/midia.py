class Midia:
    acervo_de_midia = []

    def __init__(self, titulo, ano):
        self.titulo = titulo
        self.ano = ano
        self._disponivel = True
        Midia.acervo_de_midia.append(self)

    @property
    def disponivel(self):
        return '✓' if self._disponivel else '☓'

    def __str__(self):
        titulo = self.titulo if len(self.titulo) <= 30 else self.titulo[:27] + '...'
        return f'{titulo.ljust(35)} | {str(self.ano).ljust(35)} |'

    def emprestar_midia(self):
        self._disponivel = False
    
    def devolver_midia(self):
        self._disponivel = True
    