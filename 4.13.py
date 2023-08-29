import random

def rolagem_do_dado(sides):
    return random.randint(1, sides)


resultado = rolagem_do_dado(6)
print(f"O resultado do dado é: {resultado}")
