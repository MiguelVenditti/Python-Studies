"""Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e
cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente."""


lista = [[], []]
for vezes in range(0, 7):
    num = int(input("Por favor, digite um número "))

    if (num % 2 == 0):
        lista[0].append(num)
    else:
        lista[1].append(num)

lista[0].sort()
lista[1].sort()

print("Os valores pares digitados foram: {}".format(lista[0]))
print("Os valores impares digitados foram: {}".format(lista[1]))
