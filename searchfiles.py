"""
Módulo para processar arquivos e retornar um JSON com os caminhos encontrados.
"""

from pathlib import Path
import json

def retorna_numero(pasta):
    """
    Navega por todos os subdiretórios de um diretório e retorna um JSON com os arquivos encontrados.

    Args:
        pasta (str): Caminho da pasta a ser explorada.

    Returns:
        str: JSON com caminhos completos como valores.
    """
    p = Path(pasta)
    filerelations = {}

    stack = [p]
    while stack:
        current = stack.pop()
        for item in current.iterdir():
            if item.is_dir():
                stack.append(item)
            elif item.is_file():
                filerelations[str(item)] = item.name

    return json.dumps(filerelations, indent=4)

def salvar_json(json_data):
    """
    Pergunta ao usuário se deseja salvar o JSON em um arquivo e, se sim, pede o nome do arquivo.

    Args:
        json_data (str): O JSON a ser salvo.
    """
    resposta = input("Você gostaria de baixar o arquivo JSON? (s/n): ").strip().lower()
    if resposta == 's':
        while True:
            nome_arquivo = input("Digite o nome do arquivo JSON (sem extensão): ").strip()
            if nome_arquivo:
                with open(f"{nome_arquivo}.json", "w", encoding='utf-8') as f:
                    f.write(json_data)
                print(f"Arquivo '{nome_arquivo}.json' salvo com sucesso!")
                break
            print("Nome inválido. Por favor, digite um nome válido.")

def main(path):
    """
    Função principal para executar o processamento dos arquivos e gerar o JSON.
    """
    caminho = f"{path}"  # Altere para o caminho desejado
    json_resultado = retorna_numero(caminho)
    print(json_resultado)
    salvar_json(json_resultado)

# Exemplo de uso
if __name__ == "__main__":
    main("caminho desejado")
