"""Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois
parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz
de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente."""


def exibir(a='<desconhecido>', b=0):
    print('O jogador {} fez {} gol(s) no campeonato'.format(a, b))


nome = str(input("Nome do Jogador: ").strip().capitalize())
gols = str(input("Número de Gols: "))
if (gols.isnumeric()):
    gols = int(gols)
else:
    gols = 0
if (nome == ""):
    exibir(b=gols)
else:
    exibir(nome, gols)
