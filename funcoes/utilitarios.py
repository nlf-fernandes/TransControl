# funcoes/utilitarios.py
#Luis.H
import json

# Importa as listas globais de cada módulo
from .vans import lista_vans
from .viagens import lista_viagens, encontrar_viagem_por_id
from .passageiros import lista_passageiros

ARQUIVO_DADOS = "dados/dados_do_sistema.json"

# ====================== PERSISTÊNCIA ======================
def salvar_dados():
    """Salva todas as listas (vans, viagens e passageiros) em arquivo JSON."""
    dados_completos = {
        "vans": lista_vans,
        "viagens": lista_viagens,
        "passageiros": lista_passageiros
    }
    try:
        with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as f:
            json.dump(dados_completos, f, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"Erro ao salvar dados: {e}")

def carregar_dados():
    """Carrega todas as listas do arquivo JSON, substituindo as listas atuais."""
    try:
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as f:
            dados_completos = json.load(f)
            
            lista_vans.clear()
            lista_vans.extend(dados_completos.get("vans", []))
            
            lista_viagens.clear()
            lista_viagens.extend(dados_completos.get("viagens", []))
            
            lista_passageiros.clear()
            lista_passageiros.extend(dados_completos.get("passageiros", []))
            
    except FileNotFoundError:
        print("Arquivo de dados não encontrado. Começando com listas vazias.")
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo de dados. Pode estar corrompido.")

# ====================== CÁLCULOS DE VIAGEM ======================
def atualizar_calculos_viagem(viagem):
    """
    Atualiza os campos 'receita_total', 'custo_estimado' e 'lucro' de uma viagem.
    A receita é a soma dos valores pagos pelos passageiros.
    O custo é calculado usando o consumo da van e o preço do combustível.
    """
    # Receita total
    receita = sum(p["valor_pago"] for p in viagem["passageiros"])
    
    # Busca a van correspondente pela placa
    van = next((v for v in lista_vans if v["placa"] == viagem["van_placa"]), None)
    if van:
        consumo = van.get("consumo", 10)  # valor padrão 10 km/L se não definido
        custo = (viagem["distancia_km"] / consumo) * viagem["preco_combustivel"]
    else:
        custo = 0.0

    lucro = receita - custo

    # Atualiza os campos da viagem
    viagem["receita_total"] = receita
    viagem["custo_estimado"] = custo
    viagem["lucro"] = lucro

# ====================== CONSULTA DETALHADA ======================
def consultar_viagem():
    """
    Exibe os detalhes completos de uma viagem, incluindo passageiros
    e cálculos de receita, custo e lucro.
    """
    if not lista_viagens:
        print("\nNenhuma viagem cadastrada.")
        return

    try:
        id_viagem = int(input("Digite o ID da viagem que deseja consultar: "))
    except ValueError:
        print("ERRO: Digite um número válido.")
        return

    viagem = encontrar_viagem_por_id(id_viagem)
    if not viagem:
        print("ERRO: Viagem não encontrada.")
        return

    # Atualiza cálculos antes de exibir
    atualizar_calculos_viagem(viagem)

    print("\n=== Detalhes da Viagem ===")
    print(f"ID: {viagem['id']} | Destino: {viagem['destino']}")
    print(f"Distância: {viagem['distancia_km']} km")
    print(f"Preço Combustível: R$ {viagem['preco_combustivel']:.2f}")
    print(f"Van usada: {viagem['van_placa']}")
    print(f"Status: {viagem['status']}")

    print("\n--- Passageiros ---")
    if viagem["passageiros"]:
        for p in viagem["passageiros"]:
            print(f"- {p['nome']} | R$ {p['valor_pago']:.2f}")
    else:
        print("Nenhum passageiro cadastrado.")

    print("\n--- Cálculos ---")
    print(f"Receita total: R$ {viagem['receita_total']:.2f}")
    print(f"Custo estimado: R$ {viagem['custo_estimado']:.2f}")
    print(f"Lucro estimado: R$ {viagem['lucro']:.2f}")
