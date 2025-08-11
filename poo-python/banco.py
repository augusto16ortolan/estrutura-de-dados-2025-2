from conta_bancaria import ContaBancaria

class Banco:

    def __init__(self, nome):
        if not nome.strip():
            raise ValueError("Nome do banco deve ser um texto não vazio.")
        self.nome = nome.strip()
        self.lista_contas = []

    def criar_conta(self, titular):
        conta = ContaBancaria(titular)
        self.lista_contas.append(conta)
        print(f"Conta criada: {conta}")
        return conta

    def encontrar_conta_por_numero(self, numero):
        for conta in self.lista_contas:
            if conta.numero == numero:
                return conta
        return None

    def exibir_contas(self):
        if not self.lista_contas:
            print("Nenhuma conta cadastrada no banco.")
            return
        print(f"Lista de contas do banco '{self.nome}':")
        for conta in self.lista_contas:
            print(f"- {conta}")

    def total_contas(self):
        return len(self.lista_contas)

    def total_valor_em_contas(self):
        return float(sum(conta.saldo for conta in self.lista_contas))

    def transferir(self, numero_origem, numero_destino, valor):
        if valor is None or valor <= 0:
            print("Valor de transferência inválido. Informe um valor positivo.")
            return False

        conta_origem = self.encontrar_conta_por_numero(numero_origem)
        conta_destino = self.encontrar_conta_por_numero(numero_destino)

        if conta_origem is None:
            print(f"Conta de origem {numero_origem} não encontrada.")
            return False
        if conta_destino is None:
            print(f"Conta de destino {numero_destino} não encontrada.")
            return False
        if conta_origem.numero == conta_destino.numero:
            print("Contas de origem e destino devem ser diferentes.")
            return False

        if not conta_origem.sacar(valor):
            return False
        if not conta_destino.depositar(valor):
            print("Falha ao depositar na conta de destino. Estornando saque...")
            conta_origem.depositar(valor)
            return False

        print(
            f"Transferência de R$ {valor:.2f} realizada da conta {numero_origem} para a conta {numero_destino}."
        )
        return True


