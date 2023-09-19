#4.1
import math

degrees = [0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330, 360]

print("Degrees   Sin         Cos         Tan")
print("---------------------------------------")

for degree in degrees:
    radian = math.radians(degree)
    sin_value = math.sin(radian)
    cos_value = math.cos(radian)
    
    if degree == 90 or degree == 270:
        tan_value = math.inf if degree == 90 else -math.inf
    else:
        tan_value = math.tan(radian)
    
    print(f"{degree: 3}°     {sin_value: .6f}     {cos_value: .6f}     {tan_value: .6f}")
    
    #4.2
def erxercicio_4_3(numero):
    print(F'numero ={numero}')
    print(F'{numero}² ={numero ** 2}')
    print(F'{numero}³ ={numero ** 3}')
valor = int(input('digite um valor:'))
erxercicio_4_3(valor)
    
    #4.3
from math import sqrt

def raiz_de_10_em_10():
    for numero in range(0,101,10):
        print(f'{numero} = {sqrt(numero):.3f}')


raiz_de_10_em_10()
raiz_de_10_em_10()
print('barril')
raiz_de_10_em_10()

    #4.4

def arvore(linha):
    for i in range(linha):

        print(" " * (linha - i - 1), end="")
        

        for j in range(i + 1):
            print("■", end=" ")  
        print()  

linha = int(input("Digite o número de linhas para o padrão de quadrados: "))
arvore(linha)

    
     #4.6

def draw_christmas_tree(altura):
    for i in range(altura):
        print(" " * (altura - i - 1) + "*" * (2 * i + 1))


    tronco_altura = altura // 3
    tronco_largura = altura // 3
    tronco_topo = altura - tronco_altura
    for i in range(tronco_altura):
        print(" " * (altura - tronco_largura // 2) + "*" * tronco_largura)


altura_árvore = int(input("Digite a altura da árvore de Natal: "))
draw_christmas_tree(altura_árvore)

    #4.7
def conceito(grade):
    if grade >= 9.0:
        print("Conceito: A")
    elif grade >= 8.0:
        print("Conceito: B")
    elif grade >= 7.0:
        print("Conceito: C")
    elif grade >= 5.0:
        print("Conceito: D")
    else:
        print("Conceito: E")

# Solicita a nota ao usuário
grade = float(input("Digite a nota entre 0.0 e 10.0: "))
if 0.0 <= grade <= 10.0:
    conceito(grade)
else:
    print("erro")


    #4.8
def conceito_ao_quadrado(numero):
    return numero ** 2


input_numero = int(input("Digite um número inteiro: "))
resultado = conceito_ao_quadrado(input_numero)
print(f"O quadrado de {input_numero} é {resultado}")

#4.9

def fahrenheit(celsius):
    return (celsius * 9/5) + 32


print("Temperatura:")
for celsius in range(0, 101, 10):
    fahrenheit_temperatura = fahrenheit(celsius)
    print(f"{celsius}°C = {fahrenheit_temperatura:.2f}°F")

    #4.10

def celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

começo = int(input("Digite o começo (em Fahrenheit): "))
fim = int(input("Digite o fim (em Fahrenheit): "))
intervalo = int(input("Digite o valor do intervalo: "))

print(f"Temperaturas  entre {começo}°F e {fim}°F em Celsius:")
for fahrenheit in range(começo, fim + 1, intervalo):
    celsius_temp = celsius(fahrenheit)
    print(f"{fahrenheit}°F = {celsius_temp:.2f}°C")

    #4.11
import math

def distancia(v1, t1, v2, t2):
    return math.sqrt((v2 - v1)**2 + (t2 - t1)**2)


v1 = float(input("Digite  v do primeiro ponto: "))
t1 = float(input("Digite  t do primeiro ponto: "))
v2 = float(input("Digite  v do segundo ponto: "))
t2 = float(input("Digite  t do segundo ponto: "))


dist = distancia(v1, t1, v2, t2)
print(f"A distância entre os pontos é: {dist:.2f}")


    #4.12
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


    #4.13
import random

def rolagem_do_dado(sides):
    return random.randint(1, sides)


resultado = rolagem_do_dado(6)
print(f"O resultado do dado é: {resultado}")


    #4.15
try:
    
    lista = [10, 20, 30]
    

    indice = int(input("Digite um índice : "))
    
  
    if 0 <= indice <= 2:
        elemento = lista[indice]
        print(f"O elemento no índice {indice} é {elemento}")
    else:
        raise IndexError("Índice fora da faixa permitida")
except ValueError:
    print("Digite um valor .")
except IndexError as e:
    print(e)
    #Não há variáveis globais, Todas as variáveis são locais ao bloco do programa


    #4.16
try:
    
    lista = [10, 20, 30]
    

    indice = int(input("Digite um índice : "))
    
  
    if 0 <= indice <= 2:
        elemento = lista[indice]
        print(f"O elemento no índice {indice} é {elemento}")
    else:
        raise IndexError("Índice fora da faixa permitida")
except ValueError:
    print("Digite um valor .")
except IndexError as e:
    print(e)


    #4.17

def fahrenheit(celsius):
    return (celsius * 9/5) + 32

print("Temperaturas equivalentes entre 0°C e 100°C em Fahrenheit:")

for celsius in range(0, 101, 10):
    try:
        celsius_temperatura = fahrenheit(celsius)
        print(f"{celsius}°C = {celsius_temperatura:.2f}°F")
    except ValueError:
        print("Erro: Valor inválido para celsius")

    


    

