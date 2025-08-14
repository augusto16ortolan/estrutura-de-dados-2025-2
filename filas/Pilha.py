class Pilha:

    def __init__(self):
        self._items = []

    #push
    def push(self, item):
        self._items.append(item) #adicionando um valor no final

    #pop
    def pop(self):
        #retorna um erro quando a lista estiver vazia
        if self.is_empty():
            raise IndexError("Pilha vazia")

        return self._items.pop()

    #peek
    def peek(self):
        #retorna um erro quando a lista estiver vazia
        if self.is_empty():
            raise IndexError("Pilha vazia")

        return self._items[-1]

    #is_empty
    def is_empty(self):
        return len(self._items) == 0

    #size
    def size(self):
        return len(self._items)
    
    #to_string
    def __str__(self):
        return str(self._items)
    
    #clear
    def clear(self):
        self._items = []