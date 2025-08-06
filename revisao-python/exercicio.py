#Cadastro de contas bancarias
#Criar um menu de opções
#1 - Criar uma conta
#2 - Listar contas
#3 - Depositar
#4 - Sacar
#5 - Sair

lista_contas = []

while True:
    print("1 - Criar uma conta")
    print("2 - Listar contas")
    print("3 - Depositar")
    print("4 - Sacar")
    print("5 - Sair")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        numero_conta = int(input("Digiteo numero da conta: "))
        lista_contas.append(numero_conta)
        print("Conta criada com sucesso")
    elif opcao == 2:
        for conta in lista_contas:
            print(conta)
        print("Listar contas")
    elif opcao == 3:
        print("Depositar")
    elif opcao == 4:
        print("Sacar")
    elif opcao == 5:
        print("Sair")
        break