from funcoes.passageiros import (
    cadastrar_passageiro,
    listar_passageiros,
    editar_passageiro,
    remover_passageiro,
    contar_passageiros
)

# Submenu de Passageiros
def menu_passageiros():
    while True:
        print("\n=== Gerenciamento de Passageiros ===")
        print("1 - Cadastrar Passageiro")
        print("2 - Listar Passageiros")
        print("3 - Editar Passageiro")
        print("4 - Remover Passageiro")
        print("5 - Contar Passageiros por Viagem")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_passageiro()
        elif opcao == "2":
            listar_passageiros()
        elif opcao == "3":
            editar_passageiro()
        elif opcao == "4":
            remover_passageiro()
        elif opcao == "5":
            contar_passageiros()
        elif opcao == "0":
            break
        else:
            print("Opção inválida! Tente novamente.")

# Editar passageiro
def editar_passageiro():
    if not viagens:
        print("\nNenhuma viagem cadastrada.\n")
        return

    id_viagem = int(input("Digite o ID da viagem: "))
    viagem = next((v for v in viagens if v["id"] == id_viagem), None)

    if viagem is None:
        print("Viagem não encontrada.")
        return

    if not viagem["passageiros"]:
        print("Nenhum passageiro cadastrado nessa viagem.")
        return

    for i, p in enumerate(viagem["passageiros"], start=1):
        print(f"{i}. Nome: {p['nome']} | Valor Pago: R$ {p['valor_pago']:.2f}")

    indice = int(input("Digite o número do passageiro para editar: ")) - 1
    if 0 <= indice < len(viagem["passageiros"]):
        novo_nome = input("Novo nome (ou Enter para manter): ")
        if novo_nome:
            viagem["passageiros"][indice]["nome"] = novo_nome

        novo_valor = input("Novo valor pago (ou Enter para manter): ")
        if novo_valor:
            viagem["passageiros"][indice]["valor_pago"] = float(novo_valor)

        print("Passageiro atualizado com sucesso!")
    else:
        print("Passageiro não encontrado.")


# Remover passageiro
def remover_passageiro():
    if not viagens:
        print("\nNenhuma viagem cadastrada.\n")
        return

    id_viagem = int(input("Digite o ID da viagem: "))
    viagem = next((v for v in viagens if v["id"] == id_viagem), None)

    if viagem is None:
        print("Viagem não encontrada.")
        return

    if not viagem["passageiros"]:
        print("Nenhum passageiro cadastrado nessa viagem.")
        return

    for i, p in enumerate(viagem["passageiros"], start=1):
        print(f"{i}. Nome: {p['nome']} | Valor Pago: R$ {p['valor_pago']:.2f}")

    indice = int(input("Digite o número do passageiro para remover: ")) - 1
    if 0 <= indice < len(viagem["passageiros"]):
        removido = viagem["passageiros"].pop(indice)
        print(f"Passageiro {removido['nome']} removido com sucesso!")
    else:
        print("Passageiro não encontrado.")


# Contar total de passageiros
def contar_passageiros():
    if not viagens:
        print("\nNenhuma viagem cadastrada.\n")
        return

    print("\n=== Total de Passageiros por Viagem ===")
    for v in viagens:
        print(f"Viagem {v['id']} ({v['origem']} -> {v['destino']}) tem {len(v['passageiros'])} passageiro(s).")
