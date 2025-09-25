#Nícolas Lúcio
# funcoes/vans.py
# Lista principal onde todas as vans cadastradas serão armazenadas
vans = []
# Função para cadastrar uma nova van
def cadastrar_van():
    """
    Solicita os dados da van ao usuário e adiciona na lista global 'vans'.
    """
    placa = input('Placa: ').upper().strip()
    modelo = input('Modelo da van: ')

    # Validação: capacidade e km precisam ser numéricos
    try:
        capacidade = int(input('Capacidade máxima da van: '))
        km_inicial = float(input('KM inicial da van: '))
    except ValueError:
        print("ERRO: Digite apenas números válidos para capacidade e KM.")
        return

    # Validação: impedir placas duplicadas
    for van in vans:
        if van["placa"] == placa:
            print("ERRO: Já existe uma van cadastrada com essa placa.")
            return

    # Cria um dicionário com os dados da van
    van = {
        "placa": placa,
        "modelo": modelo,
        "capacidade": capacidade,
        "km_inicial": km_inicial
    }

    vans.append(van)  # adiciona à lista
    print('\nSua van foi cadastrada!\n')

# Função para listar todas as vans cadastradas
def listar_vans():
    """
    Exibe todas as vans cadastradas em formato organizado.
    """
    if not vans:
        print('\nNenhuma van foi cadastrada ainda.\n')
        return

    print('\n==== LISTA DE VANS ====\n')
    for i, van in enumerate(vans, start=1):  # enumera cada van com índice
        print(f"{i}. Placa: {van['placa']} | Modelo: {van['modelo']} | "
              f"Capacidade: {van['capacidade']} | KM: {van['km_inicial']}")
    print()

# Função para atualizar os dados de uma van
def atualizar_van():
    """
    Permite alterar modelo, capacidade e KM de uma van já cadastrada.
    """
    listar_vans()
    if not vans:
        return

    try:
        indice = int(input('Digite o número da van que deseja atualizar: ')) - 1
    except ValueError:
        print("ERRO: Digite um número válido.")
        return

    if 0 <= indice < len(vans):
        van = vans[indice]  # pega a van escolhida
        print(f"\nAtualizando van {van['placa']}...")

        novo_modelo = input('Novo modelo (ou Enter para manter): ')
        if novo_modelo:
            van['modelo'] = novo_modelo

        nova_capacidade = input('Nova capacidade (ou Enter para manter): ')
        if nova_capacidade:
            van['capacidade'] = int(nova_capacidade)

        novo_km = input('Novo KM (ou Enter para manter): ')
        if novo_km:
            van['km_inicial'] = float(novo_km)

        print('Van atualizada com sucesso!\n')
    else:
        print('Van não encontrada.\n')

# Função para remover uma van
def remover_van():
    """
    Remove uma van da lista a partir do índice informado.
    """
    listar_vans()
    if not vans:
        return

    try:
        indice = int(input('Digite o número da van que você deseja remover: ')) - 1
    except ValueError:
        print("ERRO: Digite um número válido.")
        return

    if 0 <= indice < len(vans):
        van_removida = vans.pop(indice)
        print(f"Van {van_removida['placa']} removida com sucesso!\n")
    else:
        print('Van não encontrada.\n')
