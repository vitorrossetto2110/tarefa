#1
def maior(lista):
    if len(lista) == 0:
        return None  
    maior = lista[0] 
    for numero in lista:
        if numero > maior:
            maior = numero
    return maior

numeros = [12, 45, 6, 78, 23, 9, 67]
resultado = maior(numeros)
print(f"O maior é: {resultado}")

#2
def contador_vogais(string):
    vogais = "aeiou"
    count = 0
    
    for char in string:
        if char in vogais:
            count += 1
            
    return count


frase = str(input("Digite frase: "))
quantidade_vogais = contador_vogais(frase)
print("A quantidade de vogais na frase é:", quantidade_vogais)

#3
def palindromo(string):
    string = string.replace(" ", "").lower()
    
    return string == string[::-1]

palavra = str(input("Digite a frase: "))
print(palindromo(palavra))

#4
def media(lista):
    if not lista:
        return None
    
    total = sum(lista)
    media = total / len(lista)
    return media

numeros = [10, 20, 30, 40, 50]
media_numeros = media(numeros)
print("A média dos números é:", media_numeros)

#5
def calcular_potencia(base, expoente):
    resultado = base ** expoente
    return resultado

base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
resultado_potencia = calcular_potencia(base, expoente)
print(f"{base} elevado a {expoente} é igual a:", resultado_potencia

#6
def encontrar_primos(numero):
    primos = []
    
    for num in range(2, numero + 1):
        if e_primo(num):
            primos.append(num)
    
    return primos

def e_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n = 17625346
numeros_primos = encontrar_primos(n)
print("Números primos menores ou iguais a", n, "são:", numeros_primos)

#7
def contar(lista, elemento):
    contador = 0
    
    for item in lista:
        if item == elemento:
            contador += 1
    
    return contador

elementos = [4, 2, 5, 7, 3, 7, 89, 4, 4, 5, 6]
elemento_alvo = 2
ocorrencias = contar(elementos, elemento_alvo)
print(f"O elemento {elemento_alvo} aparece {ocorrencias} vezes na lista.")

#8
def desconto(valor_produto, percentual_desconto):
    desconto = valor_produto * (percentual_desconto / 100)
    valor_desconto = valor_produto - desconto
    return valor_com_desconto

valor_original = int(input("Digite o valor: "))
percentual_desconto = int(input("Digite o valor do desconto: "))
valor_desconto = desconto(valor_original, percentual_desconto)
print(f"O desconto é: R${valor_desconto:.2f}")

#9
def verificar_anagrama(str1, str2):
    
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    
    if len(str1) != len(str2):
        return False
    
    
    count_dict1 = {}
    count_dict2 = {}
    
    
    for char in str1:
        count_dict1[char] = count_dict1.get(char, 0) + 1
    for char in str2:
        count_dict2[char] = count_dict2.get(char, 0) + 1
    
    
    return count_dict1 == count_dict2


palavra1 = str(input("Digite a 1 palavra: "))
palavra2 = str(input("Digite a 2 palavra: "))
print(verificar_anagrama(palavra1, palavra2))

#10
def encontrar_substring(string, substring):
    return substring in string

texto = str(input("Digite a frase: "))
sub = str(input("Digite a palavra: "))
resultado = encontrar_substring(texto, sub)
print(resultado)  

#11
def ordenar(lista):
    lista_ordenada = sorted(lista)
    return lista_ordenada

numeros = [10, 5, 20, 8, 15]
numeros_ordenados = ordenar(numeros)
print("Números ordenados:", numeros_ordenados

#12
def calcular_raiz_quadrada(numero):
    aprx = numero ** 0.5  _
    return round(aprx, 2)

numero = int(input("Digite o numero: "))
raiz_quadrada = calcular_raiz_quadrada(numero)
print("A raiz quadrada de", numero, "é aproximadamente:", raiz_quadrada)

#13
def quadrado(base, altura):
    for _ in range(altura):
        linha = "* " * base
        print(linha)


base = int(input("Digite o valor da base: "))
altura = int(input("Digite o valor da altura: "))
quadrado(base, altura)

#14
def quadrado(base, altura):
    for i in range(altura):
        if i == 0 or i == altura - 1:
            linha = "* " * base
        else:
            linha = "* " + "  " * (base - 2) + "*"
        print(linha)

base = int(input("Digite o valor da base: "))
altura = int(input("Digite o valor da altura: "))
quadrado(base, altura)