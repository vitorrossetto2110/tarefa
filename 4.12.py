import random

def estimate_pi(numero_de_pontos):
    inside_circulo = 0
    for _ in range(numero_de_pontos):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x**2 + y**2
        if distance <= 1:
             inside_circulo += 1
    return ( inside_circulo / numero_de_pontos) * 4

while True:
    numero_de_pontos = int(input("Digite o número de pontos a serem sorteados (0 para sair): "))
    
    if numero_de_pontos == 0:
        break
    
    estimativa_de_pi = estimate_pi(numero_de_pontos)
    print(f"Estimativa de pi com {numero_de_pontos} pontos: { estimativa_de_pi:.6f}")
