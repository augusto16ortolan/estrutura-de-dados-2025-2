#LDE = Lista Duplamente Encadeada
from DNodo import DNodo

class LDE:

    def __init__(self):
        self.header = DNodo()
        self.trailer = DNodo()
        self.tamanho = 0

    def _inserir_primeiro(self, novo):
        self.header.proximo = novo
        self.trailer.anterior = novo
        novo.proximo = self.trailer
        novo.anterior = self.header
        self.tamanho += 1

    def inserir_inicio(self, novo):
        if self.tamanho == 0:
            self._inserir_primeiro(novo)
            return
        
        atual_primeiro = self.header.proximo
        atual_primeiro.anterior = novo
        novo.proximo = atual_primeiro
        novo.anterior = self.header
        self.header.proximo = novo
        self.tamanho += 1

    def inserir_fim(self, novo):
        if self.tamanho == 0:
            self._inserir_primeiro(novo)
            return

        atual_ultimo = self.trailer.anterior
        atual_ultimo.proximo = novo
        self.trailer.anterior = novo
        novo.anterior = atual_ultimo
        novo.proximo = self.trailer
        self.tamanho += 1

    def _remover_unico(self):
        if self.tamanho == 0:
                print("A lista já está vazia")
                return None
        
        if self.tamanho == 1:
            removido = self.header.proximo
            self.header.proximo = None
            self.trailer.anterior = None
            removido.anterior = None
            removido.proximo = None
            self.tamanho -= 1
            return removido

    def remover_inicio(self):
        if self.tamanho <= 1:
            return self._remover_unico()
        
        removido = self.header.proximo
        novo_header = removido.proximo

        removido.proximo = None
        removido.anterior = None

        novo_header.anterior = self.header
        self.header.proximo = novo_header

        self.tamanho -= 1
        
        return removido

    def remover_fim(self):
        if self.tamanho <= 1:
            return self._remover_unico()
        
        removido = self.trailer.anterior
        novo_trailer = removido.anterior

        removido.proximo = None
        removido.anterior = None

        novo_trailer.proximo = self.trailer
        self.trailer.anterior = novo_trailer

        self.tamanho -= 1

        return removido
        
    def imprimir(self):
        if self.tamanho == 0:
            print("A lista está vazia")
            return
        
        item = self.header.proximo
        while item != self.trailer:
            print(item)
            item = item.proximo

    def imprimir_lado_a_lado(self):
        if self.tamanho == 0:
            print("A lista está vazia")
            return
        
        item = self.header.proximo

        valor_a_imprimir = ""
        while item != self.trailer:
            if item == self.header.proximo:
                valor_a_imprimir = f"[HEADER] => [{item}]"
            else:
                valor_a_imprimir += f" => [{item}]"

            item = item.proximo
        
        valor_a_imprimir += " <= [TRAILER]"

        print(valor_a_imprimir)

    def primeiro(self):
        if self.tamanho == 0:
            print("A lista está vazia")
            return
        
        return self.header.proximo

    def ultimo(self):
        if self.tamanho == 0:
            print("A lista está vazia")
            return
        
        return self.trailer.anterior

    def remover_especifico(self, dado_a_ser_removido):
        if self.tamanho == 0:
            print("A lista está vazia")
            return
        
        item = self.header.proximo

        contem_o_dado = False
        
        while item != self.trailer:
            if item.dado == dado_a_ser_removido:
                proximo_atual = item.proximo
                proximo_anterior = item.anterior

                item.proximo = None
                item.anterior = None

                proximo_anterior.proximo = proximo_atual
                proximo_atual.anterior = proximo_anterior
                contem_o_dado = True
                self.tamanho -= 1
                break

            item = item.proximo

        if contem_o_dado is False:
            print("Dado não encontrado na lista")
        else:
            print("Dado deletado com sucesso")

### Testes ###
lista = LDE()
lista.inserir_inicio(DNodo("A"))
lista.inserir_fim(DNodo("B"))
lista.inserir_fim(DNodo("C"))
lista.imprimir_lado_a_lado()
lista.remover_especifico("B")
lista.imprimir_lado_a_lado()