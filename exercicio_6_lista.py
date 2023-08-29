def encontrar_primos(numero:int):
    primos = []
    for i in range(1,numero + 1):
        if e_primo(i):
            primos.append(i)

return primos


def e_primo(numero):
    for i in range(2,numero):
        divide = numero % i == 0
        if divide:
            return False
       
    return True
listas_primos = encontrar_primos(11231413444)
print(listas_primos)


