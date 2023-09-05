"""Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre
na tela os N primeiros elementos de uma Sequência de Fibonacci.

Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8
"""


print("{:=^30}\n{:^30}\n{:=^30}".format("", "Sequência de Fibonacci", ""))
num = int(input("Quantos termos voce quer mostrar? "))
termo1 = 0
termo2 = 1
print("{} -> {}".format(termo1, termo2), end='')
cont = 3

while cont <= num:
    termo3 = termo1 + termo2
    print(" -> {}".format(termo3), end='')
    termo1 = termo2
    termo2 = termo3
    cont += 1
print("-> FIM")
