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
