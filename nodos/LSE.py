from Nodo import Nodo

class LSE:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def __str__(self):
        elementos = []
        atual = self.inicio
        while atual is not None:
            elementos.append(atual.dado)
            print(atual.dado)
            atual = atual.proximo
        return str(elementos)
    
    def adicionar(self, dado):
        novo_nodo = Nodo(dado)
        if self.inicio is None:
            self.inicio = novo_nodo
            self.fim = novo_nodo
        else:
            self.fim.proximo = novo_nodo
            self.fim = novo_nodo