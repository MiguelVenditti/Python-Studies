"""Exercício Python 003: Crie um programa que leia dois números e mostre a soma entre eles."""


x = int(input("Por favor, digite um numero!\nR: "))
y = int(input("Agora digite um numero para ser somado ao anterior!\nR: "))

soma = x + y

print("A soma de {} + {} é igual a {}".format(x, y, soma))
