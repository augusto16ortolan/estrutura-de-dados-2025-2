#Cadastro de contas bancarias
#Criar um menu de opções
#1 - Criar uma conta
#2 - Listar contas
#3 - Depositar
#4 - Sacar
#5 - Sair

lista_contas = []

def encontrar_conta(numero):
    for conta in lista_contas:
        if conta['numero'] == numero:
            return conta
    return None

def criar_conta():
    numero_conta = int(input("Digite o número da conta: "))
    titular = input("Digite o nome do titular: ")
    conta = {'numero': numero_conta, 'titular': titular, 'saldo': 0.0}
    lista_contas.append(conta)
    print("Conta criada com sucesso!")

def listar_contas():
    for conta in lista_contas:
        print(f"Número: {conta['numero']} | Titular: {conta['titular']} | Saldo: R${conta['saldo']:.2f}")

def depositar():
    numero_conta = int(input("Digite o número da conta para depósito: "))
    conta = encontrar_conta(numero_conta)
    valor = float(input("Digite o valor para depositar: "))
    conta['saldo'] += valor
    print(f"Depósito de R${valor:.2f} realizado com sucesso!")

def sacar():
    numero_conta = int(input("Digite o número da conta para saque: "))
    conta = encontrar_conta(numero_conta)
    valor = float(input("Digite o valor para sacar: "))
    conta['saldo'] -= valor
    print(f"Saque de R${valor:.2f} realizado com sucesso!")

def menu():
    while True:
        print("\n--- MENU ---")
        print("1 - Criar uma conta")
        print("2 - Listar contas")
        print("3 - Depositar")
        print("4 - Sacar")
        print("5 - Sair")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            criar_conta()
        elif opcao == 2:
            listar_contas()
        elif opcao == 3:
            depositar()
        elif opcao == 4:
            sacar()
        elif opcao == 5:
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()