"""Exercício Python 098: Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens
através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada"""


from time import sleep


def titulo(a, b, c):
    d = b
    if (b < 0):
        d += 2
    elif (b == 0):
        d += 1
    print("~" * 60)
    print("  Contagem de {} até {} de {} em {}".format(a, d - 1, c, c))


def contagem(a, b, c):
    for x in range(a, b, c):
        print(x, end=', ')
        sleep(0.4)
    print("FIM")


titulo(1, 11, 1)
contagem(1, 11, 1)
titulo(10, -1, -2)
contagem(10, -1, -2)

print("Agora é sua vez de personalizar a contagem")
ini = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))

titulo(ini, fim, passo)
contagem(ini, fim, passo)
