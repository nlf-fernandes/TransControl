def encontrar_viagem_por_id(lista_viagens, id_viagem):
    """Busca uma viagem na lista pelo seu ID e retorna o dicionário da viagem ou None."""
    for viagem in lista_viagens:
        if viagem["id"] == id_viagem:
            return viagem
    return None

def listar_vans_disponiveis(lista_vans, lista_viagens):
    """
    Mostra as vans que não estão associadas a uma viagem "Agendada" ou "Em Andamento".
    Retorna a lista de placas de vans disponíveis.
    """
    placas_em_viagem = {
        viagem["van_placa"] for viagem in lista_viagens 
        if viagem["status"] in ["Agendada", "Em Andamento"]
    }
    
    vans_disponiveis = [
        van for van in lista_vans 
        if van["placa"] not in placas_em_viagem
    ]

    if not vans_disponiveis:
        print("\nNenhuma van disponível no momento.")
        return []

    print("\n--- Vans Disponíveis ---")
    for van in vans_disponiveis:
        print(f"Placa: {van['placa']}, Modelo: {van['modelo']}, Capacidade: {van['capacidade']} passageiros")
    
    return [van['placa'] for van in vans_disponiveis]

def criar_viagem(lista_viagens, lista_vans):
    """
    Função para cadastrar uma nova viagem, associando a uma van disponível.
    """
    print("\n--- Cadastro de Nova Viagem ---")

    if not lista_vans:
        print("ERRO: Nenhuma van cadastrada no sistema. Peça para o Nicolas cadastrar uma primeiro.")
        return

    placas_disponiveis = listar_vans_disponiveis(lista_vans, lista_viagens)
    if not placas_disponiveis:
        return

    placa_escolhida = input("Digite a placa da van que fará a viagem: ").upper().strip()
    
    if placa_escolhida not in placas_disponiveis:
        print("ERRO: Placa inválida ou van não está disponível.")
        return

    destino = input("Destino da viagem: ")
    
    while True:
        try:
            distancia_km = float(input("Distância total da viagem (em km): "))
            if distancia_km > 0:
                break
            print("ERRO: A distância deve ser um número positivo.")
        except ValueError:
            print("ERRO: Digite um valor numérico para a distância.")

    while True:
        try:
            preco_combustivel = float(input("Preço do combustível (por litro): R$ "))
            if preco_combustivel > 0:
                break
            print("ERRO: O preço deve ser um número positivo.")
        except ValueError:
            print("ERRO: Digite um valor numérico para o preço.")
            
    novo_id = len(lista_viagens) + 1

    nova_viagem = {
        "id": novo_id,
        "destino": destino,
        "distancia_km": distancia_km,
        "preco_combustivel": preco_combustivel,
        "van_placa": placa_escolhida,
        "passageiros": [],
        "status": "Agendada",
        "custo_estimado": 0.0,
        "receita_total": 0.0,
        "lucro": 0.0
    }

    lista_viagens.append(nova_viagem)
    print(f"\n✅ Viagem para {destino} (ID: {novo_id}) cadastrada com sucesso!")

def listar_viagens(lista_viagens):
    """
    Lista todas as viagens cadastradas com suas informações principais.
    """
    print("\n--- Lista de Todas as Viagens ---")
    if not lista_viagens:
        print("Nenhuma viagem cadastrada.")
        return

    for viagem in lista_viagens:
        print(f"ID: {viagem['id']} | Destino: {viagem['destino']}")
        print(f"  Van: {viagem['van_placa']} | Status: {viagem['status']}")
        print(f"  Passageiros: {len(viagem['passageiros'])}")
        print("-" * 20)

def atualizar_viagem(lista_viagens):
    """
    Permite atualizar informações de uma viagem existente, como o status.
    """
    print("\n--- Atualizar Informações da Viagem ---")
    if not lista_viagens:
        print("Nenhuma viagem para atualizar.")
        return

    try:
        id_para_atualizar = int(input("Digite o ID da viagem que deseja atualizar: "))
    except ValueError:
        print("ERRO: ID inválido.")
        return

    viagem = encontrar_viagem_por_id(lista_viagens, id_para_atualizar)

    if not viagem:
        print("ERRO: Viagem não encontrada com este ID.")
        return

    print(f"\nAtualizando viagem para {viagem['destino']} (Status atual: {viagem['status']})")
    print("O que você deseja atualizar?")
    print("1. Destino")
    print("2. Status da Viagem")
    
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        novo_destino = input(f"Digite o novo destino (anterior: {viagem['destino']}): ")
        viagem['destino'] = novo_destino
        print("✅ Destino atualizado com sucesso!")
    
    elif opcao == '2':
        print("\nEscolha o novo status:")
        print("  - Agendada")
        print("  - Em Andamento")
        print("  - Concluída")
        novo_status = input("Digite o novo status: ").strip().title()

        if novo_status in ["Agendada", "Em Andamento", "Concluída"]:
            viagem['status'] = novo_status
            print(f"✅ Status da viagem ID {viagem['id']} alterado para '{novo_status}'.")
            if novo_status == "Concluída":
                print(f"Lembrete: A van de placa {viagem['van_placa']} agora está disponível para outra viagem.")
        else:
            print("ERRO: Status inválido.")
    else:
        print("ERRO: Opção inválida.")
