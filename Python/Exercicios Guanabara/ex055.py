"""Exercício Python 055: Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos."""


maior = 0
menor = 500

for x in range(1,6):
    num = float(input("Peso da {}ª pessoa: ".format(x)))
    if (num > maior):
        maior = num
    elif (num < menor):
        menor = num

print(("O maior peso lido foi de {}Kg".format(maior)))
print(("O menor peso lido foi de {}Kg".format(menor)))

