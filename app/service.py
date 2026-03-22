from sensor import ler_peso
from classifier import classificar_produto

def processar_peso():
    peso = ler_peso()
    classificacao = classificar_produto(peso)

    return {
        "peso": peso,
        "classificacao": classificacao
    }