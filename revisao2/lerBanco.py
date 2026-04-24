import json

def ler_arquivo():
    with open('times.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    return dados