# Nícolas Lúcio
vans = []

def cadastrar_van():
    """Solicita os dados da van e a adiciona na lista global 'vans'."""
    print("\n--- Cadastro de Nova Van ---")
    placa = input('Placa: ').upper().strip()
    modelo = input('Modelo da van: ')

    # Validação para impedir placas duplicadas
    for van in vans:
        if van["placa"] == placa:
            print("ERRO: Já existe uma van cadastrada com essa placa.")
            return

    try:
        capacidade = int(input('Capacidade máxima de passageiros: '))
        consumo = float(input('Consumo médio de combustível (Km/L): '))
        if capacidade <= 0 or consumo <= 0:
            print("ERRO: Capacidade e consumo devem ser números positivos.")
            return
    except ValueError:
        print("ERRO: Digite apenas números válidos para capacidade e consumo.")
        return

    van = {
        "placa": placa,
        "modelo": modelo,
        "capacidade": capacidade,
        "consumo_km_l": consumo
    }

    vans.append(van)
    print('Van cadastrada com sucesso!')

def listar_vans():
    """Exibe todas as vans cadastradas em formato organizado."""
    if not vans:
        print('\nNenhuma van foi cadastrada ainda.')
        return

    print('\n--- Lista de Vans Cadastradas ---')
    for i, van in enumerate(vans, start=1):
        print(f"{i}. Placa: {van['placa']} | Modelo: {van['modelo']} | Capacidade: {van['capacidade']} | Consumo: {van['consumo_km_l']} Km/L")
    print()

def atualizar_van():
    """Permite alterar dados de uma van já cadastrada."""
    listar_vans()
    if not vans:
        return

    try:
        indice = int(input('Digite o número da van que deseja atualizar: ')) - 1
        if not (0 <= indice < len(vans)):
            print('ERRO: Van não encontrada. Índice inválido.')
            return
    except ValueError:
        print("ERRO: Digite um número válido.")
        return

    van = vans[indice]
    print(f"\nAtualizando van {van['placa']}...")

    novo_modelo = input(f"Novo modelo (atual: {van['modelo']} | Enter para manter): ").strip()
    if novo_modelo:
        van['modelo'] = novo_modelo
    
    try:
        nova_capacidade_str = input(f"Nova capacidade (atual: {van['capacidade']} | Enter para manter): ").strip()
        if nova_capacidade_str:
            van['capacidade'] = int(nova_capacidade_str)
        
        novo_consumo_str = input(f"Novo consumo (Km/L) (atual: {van['consumo_km_l']} | Enter para manter): ").strip()
        if novo_consumo_str:
            van['consumo_km_l'] = float(novo_consumo_str)
    except ValueError:
        print("ERRO: Capacidade e consumo devem ser valores numéricos. A atualização foi parcial.")

    print('Van atualizada com sucesso!')

def remover_van():
    """Remove uma van da lista a partir do índice informado."""
    listar_vans()
    if not vans:
        return

    try:
        indice = int(input('Digite o número da van que você deseja remover: ')) - 1
        if not (0 <= indice < len(vans)):
            print('ERRO: Van não encontrada. Índice inválido.')
            return
    except ValueError:
        print("ERRO: Digite um número válido.")
        return
    
    van_removida = vans.pop(indice)
    print(f"Van {van_removida['placa']} removida com sucesso!")
