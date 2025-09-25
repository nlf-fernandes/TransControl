# Luis Felipe

from .viagens import lista_viagens, encontrar_viagem_por_id

def cadastrar_passageiro():
    """Adiciona um novo passageiro a uma viagem que ainda não foi concluída."""
    
    # Filtra para mostrar apenas viagens que não estão "Concluidas"
    viagens_abertas = [v for v in lista_viagens if v.get('status') != 'Concluida']

    if not viagens_abertas:
        print("\nNão há viagens em aberto para adicionar passageiros.")
        return
    
    print("\n--- Viagens Disponíveis para Adicionar Passageiros ---")
    for v in viagens_abertas:
        print(f"ID: {v['id']} | Destino: {v['destino']} | Status: {v['status']}")
    
    try:
        id_viagem = int(input("\nDigite o ID da viagem para adicionar o passageiro: "))
        # Busca a viagem na lista de viagens abertas
        viagem = next((v for v in viagens_abertas if v['id'] == id_viagem), None)
        if not viagem:
            print("ERRO: Viagem não encontrada ou já foi concluída.")
            return
    except ValueError:
        print("ERRO: ID inválido. Digite um número.")
        return

    print(f"\nAdicionando passageiro à viagem para {viagem['destino']}.")
    nome = input("Nome do passageiro: ").strip()
    
    try:
        valor_pago = float(input("Valor pago pelo passageiro: R$ "))
        if valor_pago < 0:
            print("ERRO: O valor pago não pode ser negativo.")
            return
    except ValueError:
        print("ERRO: Valor inválido. Digite um número.")
        return

    passageiro = {"nome": nome, "valor_pago": valor_pago}
    viagem["passageiros"].append(passageiro)
    print(f"Passageiro {nome} cadastrado na viagem {id_viagem} com sucesso!")

def listar_passageiros_viagem():
    """Mostra todos os passageiros de uma viagem selecionada (qualquer status)."""
    if not lista_viagens:
        print("\nNenhuma viagem cadastrada.")
        return

    print("\n--- Listar Passageiros de uma Viagem ---")
    for v in lista_viagens:
        print(f"ID: {v['id']} | Destino: {v['destino']} | Status: {v['status']}")

    try:
        id_viagem = int(input("\nDigite o ID da viagem para listar os passageiros: "))
        viagem = encontrar_viagem_por_id(id_viagem)
        if not viagem:
            print("ERRO: Viagem не encontrada com este ID.")
            return
    except ValueError:
        print("ERRO: ID inválido. Digite um número.")
        return

    print(f"\n--- Passageiros da Viagem {id_viagem} (Destino: {viagem['destino']}) ---")
    if not viagem["passageiros"]:
        print("Nenhum passageiro cadastrado nesta viagem.")
        return

    for i, passageiro in enumerate(viagem["passageiros"], start=1):
        print(f"{i}. Nome: {passageiro['nome']} | Valor Pago: R$ {passageiro['valor_pago']:.2f}")
    
    print(f"\nTotal de passageiros: {len(viagem['passageiros'])}")

def remover_passageiro():
    """Remove um passageiro de uma viagem que ainda não foi concluída."""
    viagens_abertas = [v for v in lista_viagens if v.get('status') != 'Concluida' and v.get('passageiros')]

    if not viagens_abertas:
        print("\nNão há viagens com passageiros para remover.")
        return

    print("\n--- Viagens com Passageiros para Remover ---")
    for v in viagens_abertas:
        print(f"ID: {v['id']} | Destino: {v['destino']} | Passageiros: {len(v['passageiros'])}")

    try:
        id_viagem = int(input("\nDigite o ID da viagem para remover o passageiro: "))
        viagem = next((v for v in viagens_abertas if v['id'] == id_viagem), None)
        if not viagem:
            print("ERRO: Viagem não encontrada, já concluída ou sem passageiros.")
            return

        print(f"\n--- Passageiros da Viagem {id_viagem} ---")
        for i, p in enumerate(viagem['passageiros'], start=1):
            print(f"{i}. {p['nome']}")
            
        indice = int(input('\nDigite o número do passageiro que você deseja remover: ')) - 1
        if not (0 <= indice < len(viagem['passageiros'])):
            print('ERRO: Passageiro não encontrado. Índice inválido.')
            return
    except ValueError:
        print("ERRO: Digite números válidos para o ID e o índice.")
        return
    
    passageiro_removido = viagem['passageiros'].pop(indice)
    print(f"Passageiro '{passageiro_removido['nome']}' removido com sucesso!")
