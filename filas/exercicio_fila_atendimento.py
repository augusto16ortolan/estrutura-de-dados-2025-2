from Hospital import Hospital

hospital = Hospital()

while True:
    print("\n--- MENU ---")
    print("1 - Cadastrar paciente")
    print("2 - Atender paciente")
    print("3 - Exibir ordem de atendimento")
    print("4 - Exibir quantidade em fila")
    print("5 - Sair")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        nome_paciente = input("Digite o nome do paciente: ")
        tipo_prioridade = int(input("Digite o tipo de prioridade (0 - Normal, 1 - Prioridade): "))
        hospital.cadastrar_paciente(nome_paciente, tipo_prioridade)
    elif opcao == 2:
        paciente_atendido = hospital.atender_paciente()
        print(f"Paciente atendido: {paciente_atendido}")
    elif opcao == 3:
        hospital.exibir_order_atendimento()
    elif opcao == 4:
        hospital.exibir_quantidade_em_fila()
    elif opcao == 5:
        print("Saindo do sistema. Até logo!")