from banco import Banco
import os

def ler_inteiro(mensagem):
    while True:
        valor = input(mensagem).strip()
        try:
            return int(valor)
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def ler_float_positivo(mensagem):
    
    while True:
        valor = input(mensagem).strip().replace(",", ".")
        try:
            v = float(valor)
            if v > 0:
                return v
            print("Valor deve ser positivo.")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def pausar():
    input("Pressione Enter para continuar...")
    limpar_tela()


if __name__ == "__main__":
    banco = Banco("Banco Python")

    while True:
        print()
        print("1 - Criar conta")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Exibir saldo de uma conta")
        print("5 - Listar contas")
        print("6 - Totais do banco")
        print("7 - Transferir entre contas")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            titular = input("Titular: ").strip()
            try:
                conta = banco.criar_conta(titular)
            except Exception as e:
                print(f"Erro: {e}")
            pausar()

        elif opcao == "2":
            numero = ler_inteiro("Número da conta: ")
            valor = ler_float_positivo("Valor do depósito: ")
            conta = banco.encontrar_conta_por_numero(numero)
            if conta is None:
                print("Conta não encontrada.")
            else:
                conta.depositar(valor)
            pausar()

        elif opcao == "3":
            numero = ler_inteiro("Número da conta: ")
            valor = ler_float_positivo("Valor do saque: ")
            conta = banco.encontrar_conta_por_numero(numero)
            if conta is None:
                print("Conta não encontrada.")
            else:
                conta.sacar(valor)
            pausar()

        elif opcao == "4":
            numero = ler_inteiro("Número da conta: ")
            conta = banco.encontrar_conta_por_numero(numero)
            if conta is None:
                print("Conta não encontrada.")
            else:
                conta.exibir_saldo()
            pausar()

        elif opcao == "5":
            banco.exibir_contas()
            pausar()

        elif opcao == "6":
            print(f"Total de contas: {banco.total_contas()}")
            print(f"Valor total em contas: R$ {banco.total_valor_em_contas():.2f}")
            pausar()

        elif opcao == "7":
            origem = ler_inteiro("Número da conta de origem: ")
            destino = ler_inteiro("Número da conta de destino: ")
            valor = ler_float_positivo("Valor da transferência: ")
            banco.transferir(origem, destino, valor)
            pausar()

        elif opcao == "0":
            print("Saindo...")
            limpar_tela()
            break

        else:
            print("Opção inválida.")
            pausar()

