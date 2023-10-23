#7.1
def imprimir_inverso(frase):
    if len(frase) == 0:
        return
    else:
        print(frase[-1], end='') 
        imprimir_inverso(frase[:-1])  


frase = "celacanto provoca maremoto"
imprimir_inverso(frase)
#7.2
def is_palindromo(palavra):
    
    palavra = palavra.lower().replace(" ", "")


    if len(palavra) <= 1:
        return True

   
    if palavra[0] == palavra[-1]:

        return is_palindromo(palavra[1:-1])

    return False


print(is_palindromo("arara"))  
print(is_palindromo("ovo"))    
print(is_palindromo("radar"))  
print(is_palindromo("osso"))   
print(is_palindromo("python")) 

#7.3
def is_palindromo(frase):
    
    frase = frase.lower().replace(" ", "")


    if len(frase) <= 1:
        return True

   
    if frase[0] == frase[-1]:
 
        return is_palindromo(frase[1:-1])

    return False

print(is_palindromo("A mala nada na lama"))  
print(is_palindromo("a base do teto desaba"))  
print(is_palindromo("Python é legal"))  

#7.4
def calcular_fatorial(n):
    if n == 0:
        return 1
    else:
        return n * calcular_fatorial(n - 1)

numero = 5
resultado = calcular_fatorial(numero)
print(f'O fatorial de {numero} é {resultado}')

#7.5
def somar_n_primeiros_numeros_lista(n):
    def somar_lista(n, lista):
        if n == 0:
            return sum(lista)
        else:
            lista.append(n)
            return somar_lista(n - 1, lista)

    return somar_lista(n, [])
n = 5
resultado = somar_n_primeiros_numeros_lista(n)
print(f'A soma dos primeiros {n} números é {resultado}')

#7.6
def somar_n_primeiros_numeros(n):
    if n <= 0:
        return 0
    else:
        return n + somar_n_primeiros_numeros(n - 1)

n = 5
resultado = somar_n_primeiros_numeros(n)
print(f'A soma dos primeiros {n} números é {resultado}')

