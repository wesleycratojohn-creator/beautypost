import random
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DADOS_DIR = os.path.join(BASE_DIR, "dados")

def carregar_textos(nome_arquivo):
    caminho = os.path.join(DADOS_DIR, nome_arquivo)
    with open(caminho, "r", encoding="utf-8") as f:
        return [linha.strip() for linha in f if linha.strip()]

def gerar_resposta(pergunta):
    bases = carregar_textos("frases_base.txt")
    respostas = carregar_textos("respostas.txt")
    gatilhos = carregar_textos("gatilhos.txt")

    base = random.choice(bases)
    resposta = random.choice(respostas)
    gatilho = random.choice(gatilhos)

    return f"{base} {resposta} {gatilho}"
