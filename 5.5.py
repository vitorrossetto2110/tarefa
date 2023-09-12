impares =[]
for i in range(1,101,2):
    impares.append(i)
    print(impares)
for i in enumerate(impares):
    impares.append(i+1)
    impares[i] = v+1
    print(impares)    