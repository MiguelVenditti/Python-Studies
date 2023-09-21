"""Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros
com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior."""


def maior(* x):
    z = 0
    print("=" * 55)
    print("Analisando os valores passado...")
    for y in x:
        print("{}".format(y), end=", ")
        if (y > z):
            z = y
    print("Foram informados {} valores ao todo".format(len(x)))
    print("O maior valor informado foi {}".format(z))

maior()
