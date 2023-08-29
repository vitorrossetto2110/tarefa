def arvore(linha):
    for i in range(linha):

        print(" " * (linha - i - 1), end="")
        

        for j in range(i + 1):
            print("■", end=" ")  
        print()  

linha = int(input("Digite o número de linhas para o padrão de quadrados: "))
arvore(linha)
