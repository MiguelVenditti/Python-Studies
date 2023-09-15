"""Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com
valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta."""


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for x in range(0, 3):
    for y in range(0, 3):
        matriz[x][y] = int(input("Digite um valor: [{}, {}]: ".format(x, y)))

for x in range(0, 3):
    for y in range(0, 3):
        print("[{:^5}]".format(matriz[x][y]), end=' ')
    print()
