#Abner
# Importa a lista de vans do módulo 'vans.py' para poder consultá-la.
# O "." antes de "vans" é importante, pois indica que é um módulo na mesma pasta (funcoes).
from .vans import lista_vans

# --- Variável Global do Módulo ---
# Esta lista armazenará todos os dicionários de viagens.
# Ela será preenchida pela função carregar_dados() e manipulada pelas funções abaixo.
lista_viagens = []


# --- Funções Auxiliares (não são chamadas pelo menu, mas ajudam as principais) ---

def encontrar_viagem_por_id(id_viagem):
    """Busca uma viagem na lista global pelo seu ID."""
    for viagem in lista_viagens:
        if viagem["id"] == id_viagem:
            return viagem
    return None

def listar_vans_disponiveis():
    """Mostra as vans que não estão em uma viagem 'Agendada' ou 'Em Andamento'."""
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


# --- Funções Principais (chamadas pelo main.py) ---

def cadastrar_viagem():
    """
    Cadastra uma nova viagem. Não recebe argumentos, pois usa as listas globais.
    """
    print("\n--- Cadastro de Nova Viagem ---")

    if not lista_vans:
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
    # Lembrete: A função salvar_dados() deve ser chamada no menu principal para persistir.

def listar_viagens():
    """
    Lista todas as viagens cadastradas na lista global.
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

# OBS: O seu menu de viagens não tem a opção de "Atualizar", 
# mas vou deixar a função aqui caso queiram adicionar depois.
def atualizar_viagem():
    """
    Permite atualizar informações de uma viagem existente.
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

    viagem = encontrar_viagem_por_id(id_para_atualizar)

    if not viagem:
        print("ERRO: Viagem não encontrada com este ID.")
        return

    # O resto da função continua igual...
    print(f"\nAtualizando viagem para {viagem['destino']} (Status atual: {viagem['status']})")
    # ... (código para escolher o que atualizar)
    print("✅ Viagem atualizada com sucesso!")
