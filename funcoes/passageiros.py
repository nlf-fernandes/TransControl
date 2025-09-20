Observação Crucial para o Grupo (Principalmente para o Luis H.)
Para que o salvar_dados() e carregar_dados() funcione com essa estrutura, o arquivo utilitarios.py precisará importar as listas de todos os outros módulos.
O arquivo funcoes/utilitarios.py deverá ter um começo assim:

# funcoes/utilitarios.py
import json

# Importa as listas globais de cada módulo para poder salvá-las e carregá-las
from .vans import lista_vans
from .viagens import lista_viagens
from .passageiros import lista_passageiros

ARQUIVO_DADOS = "dados/dados_do_sistema.json"

def salvar_dados():
    # Agrupa todos os dados em um único dicionário
    dados_completos = {
        "vans": lista_vans,
        "viagens": lista_viagens,
        "passageiros": lista_passageiros
    }
    try:
        with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as f:
            json.dump(dados_completos, f, indent=4, ensure_ascii=False)
        # O print de sucesso fica no main.py
    except IOError as e:
        print(f"Erro ao salvar dados: {e}")

def carregar_dados():
    try:
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as f:
            dados_completos = json.load(f)
            
            # Limpa as listas atuais e carrega os dados do arquivo
            lista_vans.clear()
            lista_vans.extend(dados_completos.get("vans", []))
            
            lista_viagens.clear()
            lista_viagens.extend(dados_completos.get("viagens", []))
            
            lista_passageiros.clear()
            lista_passageiros.extend(dados_completos.get("passageiros", []))
            # O print de sucesso fica no main.py
            
    except FileNotFoundError:
        print("Arquivo de dados não encontrado. Começando com listas vazias.")
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo de dados. Pode estar corrompido.")
