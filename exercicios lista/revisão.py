#
vetor = [1,2,3,4,5]
soma = sum(vetor)
print('vetor',vetor)
print('soma',soma)
#
vetor1 = [1,2,3,4,5]
vetor2 = [1,2,3,4,5]
soma = sum(vetor1 + vetor2)
print('vetor',vetor1, vetor2)
print('soma',soma)
#

def transpor(matriz: list) -> list:
    transposta = []

    for _ in range(len(matriz[0])):
        transposta.append([0 for _ in range(len(matriz))])
   
    for i, l in enumerate(matriz):  
        for j, v in enumerate(l): 
            transposta[j][i] = v

    return transposta

def transpor_chatGpt(matriz):
    num_linhas = len(matriz)
    num_colunas = len(matriz[0])

    transposta = [[0 for _ in range(num_linhas)] for _ in range(num_colunas)]

    for i in range(num_linhas):
        for j in range(num_colunas):
            transposta[j][i] = matriz[i][j]

    return transposta



matriz = [
    [1, 7, 5],
    [8, 2, 1],
    [4, 9, 0],
    [2, 3, 9]
]

t = transpor(matriz)
print(t)