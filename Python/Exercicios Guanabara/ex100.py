"""Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas
sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda
função vai mostrar a soma entre todos os valores pares sorteados pela função anterior."""

from random import randint

valores = list()


def gerar(y):

    for x in range(0, 5):
        y.append(randint(1, 10))
    print("Sorteando {} valores da lista: {}".format(len(valores), valores))


def soma(y):
    cont = 0
    for x in y:
        if (x % 2 == 0):
            cont += x
    print("Somando os valores pares de {}, temos {}".format(y, cont))


gerar(valores)
soma(valores)
