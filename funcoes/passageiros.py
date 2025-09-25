from funcoes.viagens import viagens

# Função para cadastrar passageiro em uma viagem
def cadastrar_passageiro():
    if not viagens:
        print("\nNenhuma viagem cadastrada ainda.\n")
        return
    
    print("\n=== Cadastro de Passageiros ===")
    for v in viagens:
        print(f"ID: {v['id']} | Origem: {v['origem']} -> Destino: {v['destino']} | Data: {v['data']}")

    try:
        id_viagem = int(input("Digite o ID da viagem para adicionar passageiro: "))
        viagem = next((v for v in viagens if v["id"] == id_viagem), None)

        if viagem is None:
            print("Viagem não encontrada.")
            return

        nome = input("Nome do passageiro: ")
        valor_pago = float(input("Valor pago: "))

        passageiro = {
            "nome": nome,
            "valor_pago": valor_pago
        }

        viagem["passageiros"].append(passageiro)
        print(f"Passageiro {nome} adicionado na viagem {id_viagem} com sucesso!\n")

    except ValueError:
        print("Entrada inválida. Digite os dados corretamente.")


# Função para listar passageiros de todas as viagens
def listar_passageiros():
    if not viagens:
        print("\nNenhuma viagem cadastrada ainda.\n")
        return

    print("\n=== Lista de Passageiros ===")
    for v in viagens:
        print(f"\nViagem {v['id']} | {v['origem']} -> {v['destino']} | Data: {v['data']}")
        if not v["passageiros"]:
            print("   Nenhum passageiro cadastrado.")
        else:
            for i, p in enumerate(v["passageiros"], start=1):
                print(f"   {i}. Nome: {p['nome']} | Valor Pago: R$ {p['valor_pago']:.2f}")


