"""Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60
para cada jogo, cadastrando tudo em uma lista composta."""

from time import sleep
from random import randint
lista = [0, 0, 0, 0, 0]

print("{:=^30}\n{:^30}\n{:=^30}".format("", "JOGA NA MEGA SENA", ""))

quantidade = int(input("Quantos jogos você quer que eu sorteie? "))
print("{:=^30}".format(" SORTEANDO {} JOGOS ").format(quantidade))

for jogos in range(1, quantidade + 1):
    for y in range (0, 5):
        gerar = randint(0, 60)
        while gerar in lista:
            gerar = randint(0, 60)
        lista[y] = gerar
    sleep(0.5)
    lista.sort()
    print("Jogo {}: {}".format(jogos, lista))

print("{:=^30}".format(" < BOA SORTE! > "))
