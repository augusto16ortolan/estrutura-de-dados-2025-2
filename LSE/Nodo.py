class Nodo:

    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

    def __str__(self):
        return str(self.dado)