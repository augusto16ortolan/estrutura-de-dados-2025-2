from Pilha import Pilha
from Historico import Historico

class Navegador:

    def __init__(self):
        self._pilha_anteriores = Pilha()
        self._pilha_proximas = Pilha()
        self._historico_completo = []
        self._pagina_atual = None

    def navegar_para(self, pagina):
        if pagina == self._pagina_atual:
            print(f"Continuando na página {pagina}")
            return

        #verificar se paginal atual é None, quer dizer que todas as listas estao vazias
        if self._pagina_atual is not None:
            self._pilha_anteriores.push(self._pagina_atual)  

        self._historico_completo.append(Historico(pagina))
        self._pagina_atual = pagina
        print(f"Navegando para {pagina}")

    def avancar(self):
        #verificar se existem elementos na pilha de proximas
        if self._pilha_proximas.is_empty():
            print("Nao é possivel avancar")
            return
        
        #adicionar a pagina no historico
        proxima_pagina = self._pilha_proximas.pop()
        self._historico_completo.append(Historico(proxima_pagina))
        self._pilha_anteriores.push(self._pagina_atual)
        self._pagina_atual = proxima_pagina
        print(f"Voltando para {self._pagina_atual}")

    def voltar(self):
        #verificar se existem elementos na pilha de anteriores
        if self._pilha_anteriores.is_empty():
            print("Nao é possivel voltar")
            return
        
        #adicionar a pagina no historico
        pagina_anterior = self._pilha_anteriores.pop()
        self._historico_completo.append(Historico(pagina_anterior))
        self._pilha_proximas.push(self._pagina_atual)
        self._pagina_atual = pagina_anterior
        print(f"Voltando para {self._pagina_atual}")

    def pagina_atual(self):
        return self._pagina_atual
    
    def historico_completo(self):
        for historico in self._historico_completo:
            print(historico)

    def imprimir(self):
        print(f"Pilha de anteriores: {self._pilha_anteriores}")
        print(f"Pilha de proximas: {self._pilha_proximas}")
        print(f"Histórico completo: ")
        self.historico_completo()
        print(f"Página atual: {self._pagina_atual}")