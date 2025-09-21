# Abner
from .vans import vans 

lista_viagens = []

def encontrar_viagem_por_id(id_viagem):
    for viagem in lista_viagens:
        if viagem["id"] == id_viagem:
            return viagem
    return None

def listar_vans_disponiveis():
    placas_em_viagem = {
        viagem["van_placa"] for viagem in lista_viagens
        if viagem["status"] in ["Agendada", "Em Andamento"]
    }
    
    vans_disponiveis = [
        van for van in vans 
        if van["placa"] not in placas_em_viagem
    ]

    if not vans_disponiveis:
        print("\nNenhuma van disponível no momento.")
        return []

    print("\n--- Vans Disponíveis ---")
    for van in vans_disponiveis:
        print(f"Placa: {van['placa']}, Modelo: {van['modelo']}, Capacidade: {van['capacidade']} passageiros")
    
    return [van['placa'] for van in vans_disponiveis]

def cadastrar_viagem():
    print("\n--- Cadastro de Nova Viagem ---")

    if not vans:
        print("ERRO: Nenhuma van cadastrada no sistema.")
        return

    placas_disponiveis = listar_vans_disponiveis()
    if not placas_disponiveis:
        return

    placa_escolhida = input("Digite a placa da van que fará a viagem: ").upper().strip()
    
    if placa_escolhida not in placas_disponiveis:
        print("ERRO: Placa inválida ou van não está disponível.")
        return

    destino = input("Destino da viagem: ")
    try:
        distancia_km = float(input("Distância total da viagem (em km): "))
        preco_combustivel = float(input("Preço do combustível (por litro): R$ "))
        if distancia_km <= 0 or preco_combustivel <= 0:
            print("ERRO: Distância e preço devem ser números positivos.")
            return
    except ValueError:
        print("ERRO: Digite valores numéricos válidos para distância e preço.")
        return
            
    novo_id = len(lista_viagens) + 1
    nova_viagem = { "id": novo_id, "destino": destino, "distancia_km": distancia_km, "preco_combustivel": preco_combustivel, "van_placa": placa_escolhida, "passageiros": [], "status": "Agendada", "custo_estimado": 0.0, "receita_total": 0.0, "lucro": 0.0 }
    lista_viagens.append(nova_viagem)
    print(f"\n Viagem para {destino} (ID: {novo_id}) cadastrada com sucesso!")

def listar_viagens():
    print("\n--- Lista de Todas as Viagens ---")
    if not lista_viagens:
        print("Nenhuma viagem cadastrada.")
        return
    for viagem in lista_viagens:
        print(f"ID: {viagem['id']} | Destino: {viagem['destino']}")
        print(f"  Van: {viagem['van_placa']} | Status: {viagem['status']}")
        print(f"  Passageiros: {len(viagem['passageiros'])}")
        print("-" * 20)
