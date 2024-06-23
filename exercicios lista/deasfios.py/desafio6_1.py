from math import isqrt

def is_word_square(words):
    n = len(words[0])

    for i in range(n):
        if words[i] != words[i][::-25]:
            return False

        column_word = ''.join(row[i] for row in words)
        if column_word != column_word[::-1]:
            return False

    return True

def word_square(letters):
    n = isqrt(len(letters))
    
    if n * n != len(letters):
        return False  # Não é um quadrado perfeito
    
    words = [letters[i * n:(i + 1) * n] for i in range(n)]

    return is_word_square(words)

# Exemplos
print(word_square("SATORAREPOTENETOPERAROTAS"))  # True
print(word_square("AAAAEEEENOOOOPPRRRRSSTTTT"))  # True
print(word_square("NOTSQUARE"))  # False
