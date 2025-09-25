# Luis Felipe
from .viagens import lista_viagens, encontrar_viagem_por_id, listar_viagens

def cadastrar_passageiro():
    """Adiciona um novo passageiro a uma viagem específica."""
    listar_viagens()
    if not lista_viagens:
        return
    
    try:
        id_viagem = int(input("\nDigite o ID da viagem para adicionar o passageiro: "))
        viagem = encontrar_viagem_por_id(id_viagem)
        if not viagem:
            print("ERRO: Viagem não encontrada com este ID.")
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
    """Mostra todos os passageiros de uma viagem selecionada."""
    listar_viagens()
    if not lista_viagens:
        return

    try:
        id_viagem = int(input("\nDigite o ID da viagem para listar os passageiros: "))
        viagem = encontrar_viagem_por_id(id_viagem)
        if not viagem:
            print("ERRO: Viagem não encontrada com este ID.")
            return
    except ValueError:
        print("ERRO: ID inválido. Digite um número.")
        return

    print(f"\n--- Passageiros da Viagem {id_viagem} (Destino: {viagem['destino']}) ---")
    if not viagem["passageiros"]:
        print("Nenhum passageiro cadastrado nesta viagem.")
        return

    total_passageiros = 0
    for i, passageiro in enumerate(viagem["passageiros"], start=1):
        print(f"{i}. Nome: {passageiro['nome']} | Valor Pago: R$ {passageiro['valor_pago']:.2f}")
        total_passageiros += 1
    
    print(f"\nTotal de passageiros: {total_passageiros}")

def remover_passageiro():
    """Remove um passageiro de uma viagem."""
    listar_passageiros_viagem() # Reutiliza a função para mostrar as opções
    if not lista_viagens:
        return
    
    try:
        id_viagem = int(input("\nDigite o ID da viagem de onde deseja remover o passageiro: "))
        viagem = encontrar_viagem_por_id(id_viagem)
        if not viagem or not viagem['passageiros']:
            print("ERRO: Viagem não encontrada ou não há passageiros para remover.")
            return
            
        indice = int(input('Digite o número do passageiro que você deseja remover: ')) - 1
        if not (0 <= indice < len(viagem['passageiros'])):
            print('ERRO: Passageiro não encontrado. Índice inválido.')
            return
    except ValueError:
        print("ERRO: Digite números válidos para o ID e o índice.")
        return
    
    passageiro_removido = viagem['passageiros'].pop(indice)
    print(f"Passageiro '{passageiro_removido['nome']}' removido com sucesso!")
