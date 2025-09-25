# Lista global para integração com utilitarios.py
lista_passageiros = []
# Funções stub para integração com o menu principal
def cadastrar_passageiro():
    if not lista_viagens:
        print("Nenhuma viagem cadastrada. Cadastre uma viagem antes de adicionar passageiros.")
        return

    print("\n--- Cadastro de Passageiro ---")
    nome = input("Nome do passageiro: ").strip()
    try:
        valor_pago = float(input("Valor pago pelo passageiro: R$ "))
    except ValueError:
        print("Valor inválido.")
        return

    print("Viagens disponíveis:")
    for v in lista_viagens:
        print(f"ID: {v['id']} | Destino: {v.get('destino', v.get('origem', ''))}")
    try:
        id_viagem = int(input("Digite o ID da viagem para associar o passageiro: "))
    except ValueError:
        print("ID inválido.")
        return

    viagem = next((v for v in lista_viagens if v['id'] == id_viagem), None)
    if not viagem:
        print("Viagem não encontrada.")
        return

    passageiro = {"nome": nome, "valor_pago": valor_pago}
    viagem["passageiros"].append(passageiro)
    print(f"Passageiro {nome} cadastrado na viagem {id_viagem} com sucesso!")

def listar_passageiros():
    print("Função listar_passageiros ainda não implementada.")

def editar_passageiro():
    print("Função editar_passageiro ainda não implementada.")

def remover_passageiro():
    print("Função remover_passageiro ainda não implementada.")

def contar_passageiros():
    print("Função contar_passageiros ainda não implementada.")

from funcoes.viagens import lista_viagens


def salvar_dados():
    try:
        with open("dados.txt", "w", encoding="utf-8") as f:
            for v in lista_viagens:
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
        lista_viagens.clear()  # limpa lista antes de carregar

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

        lista_viagens.extend(viagens_temp.values())
        print("✅ Dados carregados com sucesso!")

    except FileNotFoundError:
        print("⚠ Nenhum arquivo encontrado para carregar.")
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
