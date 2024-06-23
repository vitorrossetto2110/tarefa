def is_word_square(letters):
    n = int(len(letters) ** 0.5)  # Determina a ordem do quadrado

    if n * n != len(letters):
        return False  # O número de letras não forma um quadrado perfeito

    # Inicializa a matriz do quadrado
    word_square = [['' for _ in range(n)] for _ in range(n)]

    # Preenche a matriz com as letras da sequência
    for i in range(n):
        for j in range(n):
            word_square[i][j] = letters[i * n + j]

    # Verifica se as palavras formadas nas linhas são iguais às formadas nas colunas
    for i in range(n):
        row_word = ''.join(word_square[i])
        col_word = ''.join(word_square[j][i] for j in range(n))

        if row_word != col_word:
            return False

    return True

# Exemplo de uso
letters = "AAAAEEEENOOOOPPRRRRSSTTTT"
result = is_word_square(letters)
print(result)  # True

letters = "SATORAREPOTENETOPERAROTAS"
result = is_word_square(letters)
print(result)  # True

letters = "NOTSQUARE"
result = is_word_square(letters)
print(result)  # False