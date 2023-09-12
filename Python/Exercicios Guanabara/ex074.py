"""Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que
estão na tupla."""

from random import randint

x = (randint(0, 10), randint(0, 10), randint(0, 10),
     randint(0, 10), randint(0, 10))

maior = -1
menor = 11

for c in x:
    if (c > maior):
        maior = c
    if (c < menor):
        menor = c

print("Os valores sorteados foram:\n", x)
print("O maior número da tupla é ", maior)
print("O menor número da tupla é ", menor)
