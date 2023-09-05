"""Exercício Python 005: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu
antecessor."""


n = int(input("Digite um numero\nR:"))
antecessor = n - 1
sucessor = n + 1

print("Voce digitou o numero {}, seu antecessor é o {} e seu sucessor é {}!".format(n,antecessor,sucessor))
