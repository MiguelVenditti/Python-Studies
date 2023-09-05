"""Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos
dólares ela pode comprar."""

real = float(input("Qual o valor voce deseja converter para dolar?\nR:"))
dolar = real * 4.80
print("Com R${:.2f} voce pode comprar U${:.2f}".format(real,dolar))
