def calcular_media(nota1,nota2,nota3):
    media = (nota1 + nota2 + nota3)//3
    return media
n1 = 10
n2 = 8
n3 = 7
media = calcular_media(n1,n1,n3)
print(f' media = {media:.2f}')