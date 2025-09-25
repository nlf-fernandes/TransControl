
from funcoes.viagens import viagens


def salvar_dados():
    try:
        with open("dados.txt", "w", encoding="utf-8") as f:
            for v in viagens:
                # salva dados da viagem
                linha_viagem = f"VIAGEM|{v['id']}|{v['origem']}|{v['destino']}|{v['data']}\n"
                f.write(linha_viagem)

                # salva passageiros da viagem
                for p in v["passageiros"]:
                    linha_pass = f"PASSAGEIRO|{v['id']}|{p['nome']}|{p['valor_pago']}\n"
                    f.write(linha_pass)

        print("✅ Dados salvos com sucesso!")

    except Exception as e:
        print(f"Erro ao salvar dados: {e}")


def carregar_dados():
    try:
        viagens.clear()  # limpa lista antes de carregar

        with open("dados.txt", "r", encoding="utf-8") as f:
            linhas = f.readlines()

        viagens_temp = {}
        for linha in linhas:
            partes = linha.strip().split("|")

            if partes[0] == "VIAGEM":
                id_viagem = int(partes[1])
                viagens_temp[id_viagem] = {
                    "id": id_viagem,
                    "origem": partes[2],
                    "destino": partes[3],
                    "data": partes[4],
                    "passageiros": []
                }

            elif partes[0] == "PASSAGEIRO":
                id_viagem = int(partes[1])
                if id_viagem in viagens_temp:
                    passageiro = {"nome": partes[2], "valor_pago": float(partes[3])}
                    viagens_temp[id_viagem]["passageiros"].append(passageiro)

        viagens.extend(viagens_temp.values())
        print("✅ Dados carregados com sucesso!")

    except FileNotFoundError:
        print("⚠ Nenhum arquivo encontrado para carregar.")
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
