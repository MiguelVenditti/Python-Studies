"""Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR."""


num = int(input("Me diga um número qualquer: "))

ioupar = num % 2

if (ioupar == 1):
    print("O número {} é impar".format(num))
else:
    print("O número {} é par".format(num))
