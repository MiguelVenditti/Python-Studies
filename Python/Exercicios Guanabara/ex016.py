"""Exercício Python 016:
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira."""


# Na correção do exercicio foi orientado a utilizar o ** import math ** e a função ** trunc **

n = float(input("Digite um valor\nR:"))
print("O valor digitado foi {} e sua porção inteira é {}".format(n,int(n)))
