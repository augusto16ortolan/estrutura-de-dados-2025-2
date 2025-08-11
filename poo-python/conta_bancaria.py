class ContaBancaria:
    _ultimo_numero_atribuido = 0

    def __init__(self, titular):
        if not titular.strip():
            raise ValueError("Titular deve ser um texto não vazio.")

        type(self)._ultimo_numero_atribuido += 1
        self.titular = titular.strip()
        self.numero = type(self)._ultimo_numero_atribuido
        self.saldo = 0.0

    def depositar(self, valor):
        if valor is None or valor <= 0:
            print("Valor de depósito inválido. Informe um valor positivo.")
            return False
        self.saldo += float(valor)
        print(f"Depósito de R$ {valor:.2f} realizado na conta {self.numero}.")
        return True

    def sacar(self, valor):
        if valor is None or valor <= 0:
            print("Valor de saque inválido. Informe um valor positivo.")
            return False
        if valor > self.saldo:
            print(
                f"Saldo insuficiente para saque de R$ {valor:.2f} na conta {self.numero}. "
                f"Saldo disponível: R$ {self.saldo:.2f}."
            )
            
            return False
        self.saldo -= float(valor)
        print(f"Saque de R$ {valor:.2f} realizado na conta {self.numero}.")
        return True

    def exibir_saldo(self):
        print(f"Conta {self.numero} | Titular: {self.titular} | Saldo: R$ {self.saldo:.2f}")

    def __str__(self):
        return f"Conta {self.numero} | Titular: {self.titular} | Saldo: R$ {self.saldo:.2f}"
