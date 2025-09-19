vans = []

# Função que vai cadastrar as vans, suas placas, modelos e etc
def cadastrar_van():
    placa = input('Placa: ')
    modelo = input('Modelo da van: ')
    capacidade = int(input('Capacidade máxima da van: '))
    km_inicial = float(input('KM inicial da van: '))
    
    van = {
        "placa": placa,
        "modelo": modelo,
        "capacidade": capacidade,
        "km_inicial": km_inicial
    }
    
    vans.append(van)
    print('\nSua van foi cadastrada!\n')


# Função que lista todas as vans cadastradas
def listar_vans():
    if not vans:
        print('\nNenhuma van foi cadastrada ainda.\n')
        return
    
    print('\n==== LISTA DE VANS ====\n')
    for i, van in enumerate(vans, start=1): 
        print(f"{i}. Placa: {van['placa']} | Modelo: {van['modelo']} | " f"Capacidade: {van['capacidade']} | KM: {van['km_inicial']}")
    print()

# Função que vai atualizar os dados das vans
def atualizar_van():
    listar_vans()
    if not vans:
        return
    
    indice = int(input('Digite o número da van que deseja atualizar: ')) - 1
    if 0 <= indice < len(vans):
        van = vans[indice]  # Pegando a van diretamente
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


# Função que vai remover a van da lista
def remover_van():
    listar_vans()
    if not vans:
        return
    
    indice = int(input('Digite o número da van que você deseja remover: ')) - 1
    if 0 <= indice < len(vans):
        van_removida = vans.pop(indice)
        print(f"Van {van_removida['placa']} removida com sucesso!\n")
    else:
        print('Van não encontrada.\n')
