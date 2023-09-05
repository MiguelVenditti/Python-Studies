"""Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o."""


count = 0
soma = 0
print("Este programa soma apenas os números pares!")

for x in range(1,7):
    num = int(input("Digite o {}º numero ".format(x)))
    if (num % 2 == 0):
        soma = soma + num
if (soma == 0):
    print("Você não digitou nenhum valor par! Por isso o resultado é igual a {}".format(soma))
else:
    print("A soma de todos os numeros pares que voce digitou é igual a {}".format(soma))