def draw_christmas_tree(altura):
    for i in range(altura):
        print(" " * (altura - i - 1) + "*" * (2 * i + 1))


    tronco_altura = altura // 3
    tronco_largura = altura // 3
    tronco_topo = altura - tronco_altura
    for i in range(tronco_altura):
        print(" " * (altura - tronco_largura // 2) + "*" * tronco_largura)


altura_árvore = int(input("Digite a altura da árvore de Natal: "))
draw_christmas_tree(altura_árvore)
