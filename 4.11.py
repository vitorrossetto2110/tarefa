import math

def distancia(v1, t1, v2, t2):
    return math.sqrt((v2 - v1)**2 + (t2 - t1)**2)


v1 = float(input("Digite  v do primeiro ponto: "))
t1 = float(input("Digite  t do primeiro ponto: "))
v2 = float(input("Digite  v do segundo ponto: "))
t2 = float(input("Digite  t do segundo ponto: "))


dist = distancia(v1, t1, v2, t2)
print(f"A distância entre os pontos é: {dist:.2f}")
