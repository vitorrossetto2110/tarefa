def conceito(grade):
    if grade >= 9.0:
        print("Conceito: A")
    elif grade >= 8.0:
        print("Conceito: B")
    elif grade >= 7.0:
        print("Conceito: C")
    elif grade >= 5.0:
        print("Conceito: D")
    else:
        print("Conceito: E")

# Solicita a nota ao usuário
grade = float(input("Digite a nota entre 0.0 e 10.0: "))
if 0.0 <= grade <= 10.0:
    conceito(grade)
else:
    print("erro")
