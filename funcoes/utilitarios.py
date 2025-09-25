# Luis H.
from .vans import vans
from .viagens import lista_viagens, encontrar_viagem_por_id, listar_viagens

# Define o nome do arquivo que guardará os dados
ARQUIVO_DADOS = "dados_do_sistema.txt"

def salvar_dados():
    """Salva os dados de vans e viagens (com seus passageiros) no arquivo."""
    try:
        with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
            # Salva a seção de vans
            f.write("[VANS]\n")
            for van in vans:
                linha = f"{van['placa']};{van['modelo']};{van['capacidade']};{van['consumo_km_l']}\n"
                f.write(linha)
            
            # Salva a seção de viagens
            f.write("[VIAGENS]\n")
            for viagem in lista_viagens:
                linha = f"{viagem['id']};{viagem['destino']};{viagem['distancia_km']};{viagem['preco_combustivel']};{viagem['van_placa']};{viagem['status']}\n"
                f.write(linha)

            # Salva a seção de passageiros, vinculando-os a uma viagem pelo ID
            f.write("[PASSAGEIROS]\n")
            for viagem in lista_viagens:
                for passageiro in viagem['passageiros']:
                    linha = f"{viagem['id']};{passageiro['nome']};{passageiro['valor_pago']}\n"
                    f.write(linha)
        
        print("Dados salvos com sucesso!")
    except IOError as e:
        print(f"ERRO ao salvar dados: {e}")

def carregar_dados():
    """Carrega os dados do arquivo para as listas do sistema."""
    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
            secao_atual = None
            # Limpa as listas atuais antes de carregar novos dados
            vans.clear()
            lista_viagens.clear()

            for linha in f:
                linha = linha.strip()
                if not linha:
                    continue

                if linha.startswith('['):
                    secao_atual = linha
                    continue

                partes = linha.split(";")
                if secao_atual == "[VANS]":
                    vans.append({
                        "placa": partes[0], "modelo": partes[1],
                        "capacidade": int(partes[2]), "consumo_km_l": float(partes[3])
                    })
                elif secao_atual == "[VIAGENS]":
                    lista_viagens.append({
                        "id": int(partes[0]), "destino": partes[1],
                        "distancia_km": float(partes[2]), "preco_combustivel": float(partes[3]),
                        "van_placa": partes[4], "status": partes[5], "passageiros": []
                    })
                elif secao_atual == "[PASSAGEIROS]":
                    id_viagem = int(partes[0])
                    viagem = encontrar_viagem_por_id(id_viagem)
                    if viagem:
                        viagem['passageiros'].append({"nome": partes[1], "valor_pago": float(partes[2])})
            
            print("Dados carregados com sucesso!")

    except FileNotFoundError:
        print("Arquivo de dados não encontrado. Começando um novo sistema.")
    except Exception as e:
        print(f"ERRO ao carregar dados: {e}")

def consultar_viagem_detalhes():
    """Mostra um relatório completo de uma viagem, incluindo o financeiro."""
    listar_viagens()
    if not lista_viagens:
        return
        
    try:
        id_viagem = int(input("\nDigite o ID da viagem para ver os detalhes: "))
        viagem = encontrar_viagem_por_id(id_viagem)
        if not viagem:
            print("ERRO: Viagem não encontrada com este ID.")
            return
    except ValueError:
        print("ERRO: ID inválido. Digite um número.")
        return

    # Encontrar a van associada para pegar o consumo
    van_associada = next((v for v in vans if v["placa"] == viagem["van_placa"]), None)
    
    # Cálculos
    receita = sum(p["valor_pago"] for p in viagem["passageiros"])
    custo = 0
    if van_associada and van_associada['consumo_km_l'] > 0:
        custo = (viagem["distancia_km"] / van_associada['consumo_km_l']) * viagem["preco_combustivel"]
    lucro = receita - custo

    print(f"\n--- Detalhes da Viagem {viagem['id']} para {viagem['destino']} ---")
    print(f"Status: {viagem['status']} | Van: {viagem['van_placa']}")
    print(f"Distância: {viagem['distancia_km']} km | Preço Combustível: R$ {viagem['preco_combustivel']:.2f}")

    print("\n--- Passageiros ---")
    if not viagem["passageiros"]:
        print("Nenhum passageiro nesta viagem.")
    else:
        for p in viagem["passageiros"]:
            print(f"- {p['nome']} (Pagou: R$ {p['valor_pago']:.2f})")

    print("\n--- Relatório Financeiro ---")
    print(f"Receita Total: R$ {receita:.2f}")
    print(f"Custo Estimado com Combustível: R$ {custo:.2f}")
    print(f"Lucro Estimado: R$ {lucro:.2f}")
    print("-" * 30)
