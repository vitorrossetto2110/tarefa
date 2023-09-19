def soma_vetores(vetor1: list, vetor2:list) -> list:
    vetor_soma = []
    for i in range(len(vetor1)):
        vetor_soma.append(vetor1[i] + vetor2[i])
    return vetor_soma


l1 = [1, 2, 3]
l2 = [7, 8, 9]
result = soma_vetores(l1,l2)
print(result)