#6.1
def imprimir_frase():
    for _ in range(100):
        print('Romani ite domum')

imprimir_frase()
#6.3
def contar_espacos(string):
    count = 0
    for char in string:
        if char == ' ':
            count += 1
    return count

frase = "Esta é uma frase com espaços em branco."
quantidade_espacos = contar_espacos(frase)
print(f"A quantidade de espaços em branco na frase é: {quantidade_espacos}")

#6.4
def inverter_string(string):
    string_invertida = string[::-1]
    print(string_invertida)

frase = 'celacanto provoca maremoto'
inverter_string(frase)

#6.5
def eh_palindromo(word):
    word = word.lower()  
    return word == word[::-1]

palavra = "radar"
if eh_palindromo(palavra):
    print(f"'{palavra}' é um palíndromo.")
else:
    print(f"'{palavra}' não é um palíndromo.")

#6.6
def is_palindrome(s):
    
    s = s.lower()
    
   
    s = s.replace(" ", "")
    
   
    return s == s[::-1]


palavra = "Ovo"
if is_palindrome(palavra):
    print(f"'{palavra}' é um palíndromo.")
else:
    print(f"'{palavra}' não é um palíndromo.")

#6.7
def is_palindrome_ignore_case_and_whitespace(s):  
    s = s.lower().replace(" ", "")    
    return s == s[::-1]
frase = 'Seco de raiva coloco no colo caviar e doces'
if is_palindrome_ignore_case_and_whitespace(frase):
    print(f"'{frase}' é um palíndromo.")
else:
    print(f"'{frase}' não é um palíndromo.")
#6.8
nome_arquivo = 'seuarquivo.txt'

try:
    
    with open(nome_arquivo, 'r') as arquivo:
    
        conteudo = arquivo.read()
        conteudo_em_maiusculas = conteudo.upper()
        print(conteudo_em_maiusculas)
except FileNotFoundError:
    print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")
#6.9
def is_palindrome_ignore_case_and_whitespace(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
frase = 'Seco de raiva coloco no colo caviar e doces'
if is_palindrome_ignore_case_and_whitespace(frase):
    print(f"'{frase}' é um palíndromo.")
else:
    print(f"'{frase}' não é um palíndromo.")
nome_composto = 'Ana Paula'
if is_palindrome_ignore_case_and_whitespace(nome_composto):
    print(f"'{nome_composto}' é um palíndromo.")
else:
    print(f"'{nome_composto}' não é um palíndromo.")

#6.10

nome_arquivo = 'seuarquivo.txt'

try:
    
    with open(nome_arquivo, 'r') as arquivo:
        
        conteudo = arquivo.read()    
        conteudo_em_maiusculas = conteudo.upper()
        print(conteudo_em_maiusculas)

except FileNotFoundError:
    print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")

#6.11

nome_arquivo = 'seuarquivo.txt'

try:
    
    with open(nome_arquivo, 'r') as arquivo:       
        conteudo = arquivo.read()
        conteudo_em_minusculas = conteudo.lower()
        print(conteudo_em_minusculas)

except FileNotFoundError:
    print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")

#6.12
nome_arquivo = 'seuarquivo.txt'

try:
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        palavras = conteudo.split()
        palavras_capitalizadas = [palavra.capitalize() for palavra in palavras]
        texto_capitalizado = ' '.join(palavras_capitalizadas)
        print(texto_capitalizado)

except FileNotFoundError:
    print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")

#6.13
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32
conversoes = []
for celsius in range(301):
    fahrenheit = celsius_para_fahrenheit(celsius)
    conversoes.append((celsius, fahrenheit))
nome_arquivo = 'tabela_conversao_temperaturas.txt'

try:
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write("Celsius\tFahrenheit\n")
        for celsius, fahrenheit in conversoes:
            arquivo.write(f"{celsius}\t{fahrenheit}\n")

    print(f"Tabela de conversão de temperaturas salva em '{nome_arquivo}'.")

except Exception as e:
    print(f"Ocorreu um erro ao salvar a tabela: {str(e)}")

#6.14
import os
arquivo_origem = 'arquivo_origem.txt'
arquivo_destino = 'arquivo_destino.txt'

if os.path.isfile(arquivo_destino):
    resposta = input(f"O arquivo '{arquivo_destino}' já existe. Deseja sobrescrevê-lo? (S/N): ").strip().lower()
    
    if resposta != 's':
        print("Operação cancelada.")
    else:
        with open(arquivo_origem, 'r') as origem, open(arquivo_destino, 'w') as destino:
            conteudo = origem.read()
            destino.write(conteudo)
        print(f"O conteúdo de '{arquivo_origem}' foi copiado para '{arquivo_destino}'.")
else:
    with open(arquivo_origem, 'r') as origem, open(arquivo_destino, 'w') as destino:
        conteudo = origem.read()
        destino.write(conteudo)
    print(f"O conteúdo de '{arquivo_origem}' foi copiado para '{arquivo_destino}'.")

#6.15
import random

def dentro_do_circulo(x, y):
    return x**2 + y**2 <= 1

num_pontos = 10000

pontos_dentro = 0

nome_arquivo = 'pontos.txt'

try:
    
    with open(nome_arquivo, 'w') as arquivo:
        for _ in range(num_pontos):
            x = random.uniform(0, 1)  
            y = random.uniform(0, 1)  
            
            if dentro_do_circulo(x, y):
                pontos_dentro += 1
            
            arquivo.write(f"{x} {y}\n")
        pi = 4 * (pontos_dentro / num_pontos)
    
        arquivo.write(f"Valor de pi: {pi}\n")

    print(f"Pontos gerados e valor de pi calculado e armazenados em '{nome_arquivo}'.")

except Exception as e:
    print(f"Ocorreu um erro ao salvar o arquivo: {str(e)}")

