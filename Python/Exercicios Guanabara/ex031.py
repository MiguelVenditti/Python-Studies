"""Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas."""


dist = int(input("Qual a distancia da sua viagem?"))
print("Voce esta prestes a começar uma viagem de {}Km".format(dist))
valor = 0

if (dist >= 200):
    valor = dist * 0.45
else:
    valor = dist * 0.5

print("O preço da sua passagem será de R${:.2f}".format(valor))
