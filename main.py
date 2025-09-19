from funcoes.vans import cadastrar_van, listar_vans, atualizar_van, remover_van
from funcoes.viagens import cadastrar_viagem, listar_viagens
from funcoes.passageiros import cadastrar_passageiro, listar_passageiros
from funcoes.utilitarios import carregar_dados, salvar_dados

# Submenu de Vans
def menu_vans():
    while True:
        print("\n=== Gerenciamento de Vans ===")
        print("1 - Cadastrar Van")
        print("2 - Listar Vans")
        print("3 - Atualizar Van")
        print("4 - Remover Van")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_van()
        elif opcao == "2":
            listar_vans()
        elif opcao == "3":
            atualizar_van()
        elif opcao == "4":
            remover_van()
        elif opcao == "0":
            break
        else:
            print("Opção inválida! Tente novamente.")

# Submenu de Viagens
def menu_viagens():
    while True:
        print("\n=== Gerenciamento de Viagens ===")
        print("1 - Cadastrar Viagem")
        print("2 - Listar Viagens")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_viagem()
        elif opcao == "2":
            listar_viagens()
        elif opcao == "0":
            break
        else:
            print("Opção inválida! Tente novamente.")

# Submenu de Passageiros
def menu_passageiros():
    while True:
        print("\n=== Gerenciamento de Passageiros ===")
        print("1 - Cadastrar Passageiro")
        print("2 - Listar Passageiros")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_passageiro()
        elif opcao == "2":
            listar_passageiros()
        elif opcao == "0":
            break
        else:
            print("Opção inválida! Tente novamente.")

# Menu Principal
def menu():
    while True:
        print('\n==== SISTEMA DE CONTROLE ====\n')
        print('1 - Gerenciamento de Vans')
        print('2 - Gerenciamento de Viagens')
        print('3 - Gerenciamento de Passageiros')
        print('4 - Salvar Dados')
        print('5 - Carregar Dados')
        print('0 - Sair')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            menu_vans()
        elif opcao == '2':
            menu_viagens()
        elif opcao == '3':
            menu_passageiros()
        elif opcao == '4':
            salvar_dados()
            print("Dados salvos com sucesso!")
        elif opcao == '5': 
            carregar_dados()
            print("Dados carregados com sucesso!")
        elif opcao == '0':
            print('Encerrando o sistema...')
            break
        else:
            print('Opção inválida. Tente novamente.')

# Executa o menu se for o arquivo principal
if __name__ == "__main__":
    menu()
