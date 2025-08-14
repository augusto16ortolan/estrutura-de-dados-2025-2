class Nodo:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
    
    def __str__(self):
        return str(self.dado)
    
    def mostrarProximo(self):
        print(self.proximo)

    def listarTodos(self):
        elementos = []
        atual = self
        while atual is not None:
            elementos.append(atual.dado)
            atual = atual.proximo
        return elementos