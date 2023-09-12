"""Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. """


numeros = []
maior = 0
menor = 999999

for x in range(0,5):
    numeros.append(int(input("Digite um valor para a posição: {} ".format(x))))
    if (numeros[x] > maior):
        maior = numeros[x]
    if (numeros[x] < menor):
        menor = numeros[x]

print("Voce digitos os valores: {}".format(numeros))

print("O maior valor digitado foi o {} e se encontra nas posições ".format(maior))
for i, v in enumerate(numeros):
    if (v == maior):
        print("{}...".format(i), end=" ")
print("\nO menor valor digitado foi o {} e se encontra nas posições ".format(menor))
for i, v in enumerate(numeros):
    if (v == menor):
        print("{}...".format(i), end=" ")