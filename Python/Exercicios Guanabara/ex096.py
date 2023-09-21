"""Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões
de um terreno retangular (largura e comprimento) e mostre a área do terreno."""


def iniciar(x):
    print(" {} ".format(x))
    print("-" * 22)


def calculo(x, y):
    total = x * y
    print("A área de um terreno de {} x {} é igual a {}".format(l, c, total))


iniciar('Controle de Terrenos')

l = float(input("Largura (m): "))
c = float(input("Comprimento (m): "))

calculo(l, c)
