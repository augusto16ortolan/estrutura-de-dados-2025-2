#Duplo nodo com dois ponteiros
class DNodo:

    def __init__(self, dado=None):
        self.dado = dado
        self.proximo = None
        self.anterior = None

    def __str__(self):
        return str(self.dado)
