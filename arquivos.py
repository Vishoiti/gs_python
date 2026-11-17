"""Leitura e gravação de arquivos JSON do programa."""
import json
import os


def ler_json(caminho, padrao):
    """Lê um arquivo JSON e devolve o conteúdo.
    
    Se o arquivo não existir ou estiver corrompido, devolve o valor padrão
    ([] para listas, {} para dicionários), para o programa não quebrar.
    """
    try:
        with open(caminho, encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return padrao
    except json.JSONDecodeError:
        print(f"Aviso: {caminho} está corrompido. Começando vazio.")
        return padrao


def salvar_json(caminho, dados):
    """Grava os dados (lista ou dicionário) em um arquivo JSON.
    
    Cria a pasta do arquivo se ela ainda não existir e substitui o conteúdo antigo.
    """
    pasta = os.path.dirname(caminho)
    if pasta:
        os.makedirs(pasta, exist_ok=True)
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=2)