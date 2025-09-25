# funcoes/utilitarios.py

# Importa as listas globais de cada módulo
from .vans import vans
from .viagens import lista_viagens
from .passageiros import lista_passageiros

ARQUIVO_DADOS = "dados/dados_do_sistema.txt"


# ==============================
#   PERSISTÊNCIA DOS DADOS
# ==============================
def salvar_dados():
    """Salva vans, viagens e passageiros em arquivo .txt"""
    try:
        with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
            # ----- Salvar vans -----
            f.write("[VANS]\n")
            for van in vans:
                linha = f"{van['placa']};{van['modelo']};{van['capacidade']};{van['km_inicial']}\n"
                f.write(linha)

            # ----- Salvar viagens -----
            f.write("[VIAGENS]\n")
            for viagem in lista_viagens:
                linha = f"{viagem['van']};{viagem['destino']};{viagem['distancia']};{viagem['preco_combustivel']}\n"
                f.write(linha)

            # ----- Salvar passageiros -----
            f.write("[PASSAGEIROS]\n")
            for passageiro in lista_passageiros:
                linha = f"{passageiro['nome']};{passageiro['valor_pago']};{passageiro['viagem']}\n"
                f.write(linha)

        print(" Dados salvos com sucesso!")

    except IOError as e:
        print(f"Erro ao salvar dados: {e}")


def carregar_dados():
    """Carrega vans, viagens e passageiros do arquivo .txt"""
    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
            secao = None
            vans.clear()
            lista_viagens.clear()
            lista_passageiros.clear()

            for linha in f:
                linha = linha.strip()
                if not linha:
                    continue

                # Detecta seção
                if linha == "[VANS]":
                    secao = "vans"
                    continue
                elif linha == "[VIAGENS]":
                    secao = "viagens"
                    continue
                elif linha == "[PASSAGEIROS]":
                    secao = "passageiros"
                    continue

                # Carrega dados conforme a seção
                if secao == "vans":
                    placa, modelo, capacidade, km_inicial = linha.split(";")
                    vans.append({
                        "placa": placa,
                        "modelo": modelo,
                        "capacidade": int(capacidade),
                        "km_inicial": float(km_inicial)
                    })

                elif secao == "viagens":
                    van, destino, distancia, preco_combustivel = linha.split(";")
                    lista_viagens.append({
                        "van": van,
                        "destino": destino,
                        "distancia": float(distancia),
                        "preco_combustivel": float(preco_combustivel)
                    })

                elif secao == "passageiros":
                    nome, valor_pago, viagem = linha.split(";")
                    lista_passageiros.append({
                        "nome": nome,
                        "valor_pago": float(valor_pago),
                        "viagem": viagem
                    })

        print(" Dados carregados com sucesso!")

    except FileNotFoundError:
        print(" Nenhum arquivo de dados encontrado. Começando com listas vazias.")
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")


# ==============================
#   CÁLCULOS
# ==============================
def calcular_receita(viagem_id):
    """Soma o valor pago por todos os passageiros de uma viagem"""
    viagem = lista_viagens[viagem_id]
    placa_van = viagem["van"]
    receita = sum(p["valor_pago"] for p in lista_passageiros if p["viagem"] == placa_van)
    return receita


def calcular_custo(viagem_id):
    """Calcula custo estimado = distancia / consumo * preço do combustível"""
    viagem = lista_viagens[viagem_id]
    placa_van = viagem["van"]

    # Buscar a van correspondente
    van = next((v for v in vans if v["placa"] == placa_van), None)
    if not van:
        return 0.0

    # Aqui assumo que "km_inicial" não é o consumo, então você pode ajustar
    # Exemplo: consumo = 10 km/L
    consumo = 10  

    distancia = viagem["distancia"]
    preco = viagem["preco_combustivel"]
    return (distancia / consumo) * preco


def calcular_lucro(viagem_id):
    """Lucro = receita - custo"""
    return calcular_receita(viagem_id) - calcular_custo(viagem_id)


# ==============================
#   CONSULTAS
# ==============================
def consultar_viagem(viagem_id):
    """Mostra detalhes completos de uma viagem"""
    if viagem_id < 0 or viagem_id >= len(lista_viagens):
        print(" Viagem não encontrada.")
        return

    viagem = lista_viagens[viagem_id]
    print("\n===== DETALHES DA VIAGEM =====")
    print(f"Van usada: {viagem['van']}")
    print(f"Destino: {viagem['destino']}")
    print(f"Distância: {viagem['distancia']} km")
    print(f"Preço do combustível: R$ {viagem['preco_combustivel']:.2f}")

    # Passageiros dessa viagem
    print("\n--- Passageiros ---")
    passageiros_viagem = [p for p in lista_passageiros if p["viagem"] == viagem["van"]]
    if passageiros_viagem:
        for p in passageiros_viagem:
            print(f"{p['nome']} - R$ {p['valor_pago']:.2f}")
    else:
        print("Nenhum passageiro cadastrado.")

    # Cálculos
    receita = calcular_receita(viagem_id)
    custo = calcular_custo(viagem_id)
    lucro = calcular_lucro(viagem_id)

    print("\n--- Financeiro ---")
    print(f"Receita total: R$ {receita:.2f}")
    print(f"Custo estimado: R$ {custo:.2f}")
    print(f"Lucro: R$ {lucro:.2f}")
    print("===============================\n")

