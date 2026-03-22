from service import processar_peso
from utils import formatar_saida
from logger import log
import time

def iniciar_balanca():
    log("🔌 Sistema iniciado")

    while True:
        dados = processar_peso()
        saida = formatar_saida(dados["peso"], dados["classificacao"])

        log(saida)
        time.sleep(2)

if __name__ == "__main__":
    iniciar_balanca()