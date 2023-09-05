"""Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores."""


from datetime import date
hoje = date.today().year
menor = 0
maior = 0

for loop in range(1, 8):
    nasc = int(input("Em que ano a {}ª pessoa nasceu? ".format(loop)))
    idade = hoje - nasc
    if (idade < 18):
        menor += 1
    else:
        maior += 1
print("Ao todo temos {} maiores de idade e {} menos de idade".format(maior, menor))

