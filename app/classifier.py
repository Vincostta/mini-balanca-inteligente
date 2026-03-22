def classificar_produto(peso):
    if peso < 0.5:
        return "Produto leve 🪶"
    elif peso < 2:
        return "Produto médio 📦"
    else:
        return "Produto pesado 🏋️"