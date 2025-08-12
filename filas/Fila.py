class Fila:

    def __init__(self):
        self._items = []
        print("Fila criada")

    def enqueue(self, item): #Enfileirar (adiciona um dado no início da lista)
        if item == None:
            raise ValueError("Item nao pode ser None")
        
        if item in self._items:
            raise ValueError("Item ja esta na fila")

        self._items.insert(0, item)

    def dequeue(self): #Desenfileirar (remove o ultimo dado da lista)
        if self.is_empty():
            raise IndexError("Fila está vazia")
        
        return self._items.pop()

    def front(self): #Primeiro da Fila (ultimo dado da lista)
        if self.is_empty():
            raise IndexError("Fila está vazia")
        
        return self._items[-1]
    
    def is_empty(self): #Verifica se a Fila esta vazia
        return len(self._items) == 0
    
    def size(self): #Retorna o tamanho da Fila
        return len(self._items)
    
    def __str__(self):
        return str(self._items)
    

if __name__ == "__main__":

    try:
        fila = Fila()
        fila.enqueue("Augusto")
        print(fila)
        fila.enqueue("Joao")
        print(fila)
        fila.enqueue("Maria")
        print(fila)
        fila.dequeue()
        print(fila)
        print(fila.front())
        fila.dequeue()
        fila.dequeue()
    except Exception as e:
        print(e)
    finally:
        print("Fim do programa")
