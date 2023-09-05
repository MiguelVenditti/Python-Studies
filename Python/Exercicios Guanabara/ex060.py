"""Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
"""

x = int(input("Digite seu Número para\ncalcular seu Fatorial: "))
count = x

for fatorial in range(x -1, 0, -1):
    count *= fatorial

print("{}! = {}".format(x, count))

"""import math
x = int(input("Digite seu Número para\ncalcular seu Fatorial: "))
f = math.factorial(x)
print("{}! = {}".format(x, f))"""
