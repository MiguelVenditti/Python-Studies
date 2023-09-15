"""Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha."""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = 0
maior = 0

for x in range(0, 3):
    for y in range(0, 3):
        matriz[x][y] = int(input("Digite um valor: [{}, {}]: ").format(x, y))
        if (matriz[x][y] % 2 == 0):
            par += matriz[x][y]

# Descobrindo maior da segunda linha
for y in range (0, 3):
    if (matriz[1][y] > maior):
        maior = matriz[1][y]

# Exibir matriz

print("{:=>30}".format(''))
for x in range(0, 3):
    for y in range(0, 3):
        print("[{:^5}]".format(matriz[x][y]), end=' ')
    print()
print("{:=>30}".format(''))

print("Soma dos pares digitados: {}".format(par))
print("Soma de todos os valores da terceira coluna: {}".format((matriz[0][2] + matriz[1][2] + matriz[2][2])))
print("O maior  valor da segunda linha é o {}".format(maior))
