from funcoes.vans import cadastrar_van, listar_vans, atualizar_van, remover_van
from funcoes.viagens import cadastrar_viagem, listar_viagens, atualizar_viagem_status
from funcoes.passageiros import cadastrar_passageiro, listar_passageiros_viagem, remover_passageiro
from funcoes.utilitarios import carregar_dados, salvar_dados, consultar_viagem_detalhes

# --- SUBMENUS ---

def menu_vans():
    """Gerencia as opções relacionadas às vans."""
    while True:
        print('\n--- Gerenciamento de Vans ---')
        print('1 - Cadastrar Nova Van')
        print('2 - Listar Todas as Vans')
        print('3 - Atualizar Dados de uma Van')
        print('4 - Remover uma Van')
        print('0 - Voltar ao Menu Principal')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            cadastrar_van()
        elif opcao == '2':
            listar_vans()
        elif opcao == '3':
            atualizar_van()
        elif opcao == '4':
            remover_van()
        elif opcao == '0':
            break
        else:
            print('Opção inválida! Tente novamente.')

def menu_viagens():
    """Gerencia as opções relacionadas às viagens."""
    while True:
        print('\n--- Gerenciamento de Viagens ---')
        print('1 - Cadastrar Nova Viagem')
        print('2 - Listar Todas as Viagens')
        print('3 - Atualizar Status de uma Viagem')
        print('0 - Voltar ao Menu Principal')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            cadastrar_viagem()
        elif opcao == '2':
            listar_viagens()
        elif opcao == '3':
            atualizar_viagem_status()
        elif opcao == '0':
            break
        else:
            print('Opção inválida! Tente novamente.')

def menu_passageiros():
    """Gerencia as opções relacionadas aos passageiros."""
    while True:
        print('\n--- Gerenciamento de Passageiros ---')
        print('1 - Adicionar Passageiro a uma Viagem')
        print('2 - Listar Passageiros de uma Viagem')
        print('3 - Remover Passageiro de uma Viagem')
        print('0 - Voltar ao Menu Principal')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            cadastrar_passageiro()
        elif opcao == '2':
            listar_passageiros_viagem()
        elif opcao == '3':
            remover_passageiro()
        elif opcao == '0':
            break
        else:
            print('Opção inválida! Tente novamente.')

# --- MENU PRINCIPAL ---

def menu_principal():
    """Menu principal que orquestra todo o sistema."""
    
    # Carrega os dados salvos assim que o programa inicia
    carregar_dados()

    while True:
        print('\n==== SISTEMA DE CONTROLE DE TRANSPORTE ====')
        print('1 - Gerenciamento de Vans')
        print('2 - Gerenciamento de Viagens')
        print('3 - Gerenciamento de Passageiros')
        print('4 - Consultar Detalhes de uma Viagem')
        print('0 - Salvar e Sair')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            menu_vans()
        elif opcao == '2':
            menu_viagens()
        elif opcao == '3':
            menu_passageiros()
        elif opcao == '4':
            consultar_viagem_detalhes()
        elif opcao == '0':
            # Salva os dados automaticamente antes de encerrar
            salvar_dados()
            print('Encerrando o sistema...')
            break
        else:
            print('Opção inválida. Tente novamente.')

# --- PONTO DE ENTRADA DO PROGRAMA ---
if __name__ == "__main__":
    menu_principal()
