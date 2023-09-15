"""Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""

lista_maior = []
lista_menor = []
maior = ['', 0]
menor = ['', 99999]
lista = []

while True:
    pessoa = str(input("Nome: "))
    lista.append(pessoa)

    peso = float(input("Peso: "))
    lista.append(peso)

    if (peso > maior[1]):
        maior = []
        maior.append(pessoa)
        maior.append(peso)
    elif (peso == maior[1]):
        maior.append(pessoa)
        maior.append(peso)
    elif (peso < menor[1]):
        menor = []
        menor.append(pessoa)
        menor.append(peso)
    elif (peso == menor[1]):
        menor.append(pessoa)
        menor.append(peso)

    fim = str(input("Continuar cadastrando? [S/N] ").strip().upper()[0])
    if (fim == 'N'):
        break


print("Ao todo voce cadastrou {:.0f} pessoas".format(len(lista) / 2))

for nome in range (0, len(maior)):
    if (nome % 2 == 0):
        lista_maior.append(maior[nome])

print("Os mais pesados são {}".format(lista_maior))

for nome in range(0, len(menor)):
    if (nome % 2 == 0):
        lista_menor.append(menor[nome])

print("Os mais leves são {}".format(lista_menor))
