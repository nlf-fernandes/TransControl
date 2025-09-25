from funcoes.passageiros import (
    cadastrar_passageiro,
    listar_passageiros,
    editar_passageiro,
    remover_passageiro,
    contar_passageiros
)

# Submenu de Passageiros
def menu_passageiros():
    while True:
        print("\n=== Gerenciamento de Passageiros ===")
        print("1 - Cadastrar Passageiro")
        print("2 - Listar Passageiros")
        print("3 - Editar Passageiro")
        print("4 - Remover Passageiro")
        print("5 - Contar Passageiros por Viagem")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_passageiro()
        elif opcao == "2":
            listar_passageiros()
        elif opcao == "3":
            editar_passageiro()
        elif opcao == "4":
            remover_passageiro()
        elif opcao == "5":
            contar_passageiros()
        elif opcao == "0":
            break
        else:
            print("Opção inválida! Tente novamente.")
