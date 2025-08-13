from Fila import Fila  

class Hospital:

    def __init__(self):
        self.fila_de_prioridade = Fila()
        self.fila_normal = Fila()

    def cadastrar_paciente(self, nome_paciente, tipo_prioridade = 0):
        if tipo_prioridade != 0 and tipo_prioridade != 1:
            raise ValueError("Tipo de prioridade inválido")

        if tipo_prioridade == 0:
            self.fila_normal.enqueue(nome_paciente)
            print("Paciente cadastrado na fila normal")
            return
        
        self.fila_de_prioridade.enqueue(nome_paciente)
        print("Paciente cadastrado na fila de prioridade")


    def atender_paciente(self):
        if self.fila_normal.is_empty() and self.fila_de_prioridade.is_empty():
            raise IndexError("Fila vazia")

        if self.fila_de_prioridade.is_empty():
            return self.fila_normal.dequeue()
        
        return self.fila_de_prioridade.dequeue()

    
    def exibir_order_atendimento(self):
        lista_geral = []
        
        for paciente in self.fila_de_prioridade.get_items():
            lista_geral.append(paciente)
        
        for paciente in self.fila_normal.get_items():
            lista_geral.append(paciente)
        
        for paciente in lista_geral:
            print(paciente)

    
    def exibir_quantidade_em_fila(self):
        print(f"Quantidade de pacientes na fila de prioridade: {self.fila_de_prioridade.size()}")
        print(f"Quantidade de pacientes na fila normal: {self.fila_normal.size()}")