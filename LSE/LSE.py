#Lista Simplesmente Encadeada
from Nodo import Nodo

class LSE:

    def __init__(self):
        self.head = None #cabeça/inicio
        self.tail = None #cauda/fim
        self.tamanho = 0

    def is_empty(self):
        if (self.head is None and self.tail is None) or self.tamanho == 0:
            return True
        
        #if (self.head is None and self.tail is None) or self.tamanho == 0:
            #return True
        
        #if self.tamanho == 0
        #   return True

        return False

    def inserirInicio(self, novo):
        self.tamanho += 1

        if self.is_empty():
            self.head = novo
            self.tail = novo
            return
        
        novo.proximo = self.head
        self.head = novo


    def removerInicio(self):
        if self.is_empty():
            print("A lista está vazia")
            return

        self.tamanho -= 1

        if(self.head == self.tail):
            removido = self.head
            self.head = None
            self.tail = None
            return removido
        
        removido = self.head
        self.head = removido.proximo
        removido.proximo = None

        return removido

    def inserirFim(self, novo):

        self.tamanho += 1

        if self.is_empty():
            self.head = novo
            self.tail = novo
            return
        
        ultimo = self.tail
        ultimo.proximo = novo
        self.tail = novo

    def removerFim(self):
        if self.is_empty():
            print("A lista está vazia")
            return

        removido = None
        item = self.head
        while (item != None):
            if (self.head == item and self.tail == item):
                self.head = None
                self.tail = None
                self.tamanho -= 1
                return item

            if (item.proximo != None and item.proximo == self.tail):
                removido =  self.tail
                self.tail = item
                item.proximo = None
                self.tamanho  -= 1
                return removido

            item = item.proximo

    def imprimir(self):
        if self.is_empty():
            print("A lista está vazia")
            return
        
        item = self.head
        while(item != None):
            print(item)
            item = item.proximo

    def imprimirLadoALado(self):
        if self.is_empty(): 
            print("A lista está vazia")
            return

        valorImprimir = ""

        item = self.head
        while(item != None):
            if (item == self.head):
                valorImprimir += f"[{item}]"
            else:
                valorImprimir += f"=> [{item}]"
            
            item = item.proximo
        
        print(valorImprimir)

### Testes ###
lista = LSE()
lista.inserirInicio(Nodo("A"))
lista.inserirFim(Nodo("B"))
lista.inserirInicio(Nodo("C"))
lista.removerInicio()
lista.inserirInicio(Nodo("1"))
lista.inserirFim(Nodo("2"))
lista.inserirInicio(Nodo("3"))
lista.inserirFim(Nodo("4"))
lista.inserirInicio(Nodo("5"))
lista.removerFim()

lista.imprimirLadoALado()

#[5]=> [3]=> [1]=> [A]=> [B]=> [2]
