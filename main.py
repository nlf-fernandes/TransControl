from funcoes.vans import cadastrar_van, listar_vans
from funcoes.viagens import cadastrar_viagem, listar_viagens
from funcoes.passageiros import cadastrar_passageiro 
from funcoes.utilitarios import carregar_dados,salvar_dados

#menu inicial - o usuario navegará a partir daqui 
def menu():
    while True:
        print('/n==== Sistema TransControl====')
        print('Digite 1 - Gerenciamento de Vans')
        print('Digite 2 - Gerenciamento de Viagens')
        print('Digite 3 - Gerenciamneto de Passageiros')
        print('Digite 4 - Salvar Dados')
        print('Digite 5 - Carregar Dados')
        print('Digite 0 - Sair')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            cadastrar_van()
        elif opcao == '2':
            cadastrar_viagem()
        elif opcao == '3':
            cadastrar_passageiro()
        elif opcao == '4':
            salvar_dados()
        elif opcao == '5': 
            carregar_dados()
        elif opcao == '0':
            print('Encerrando o sistema...')
            break
        else:
            print('Opção invalida tente novamente.')
