from datetime import datetime

def log(mensagem):
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{agora}] {mensagem}")