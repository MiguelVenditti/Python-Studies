"""Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado."""


from time import sleep
from random import randint
from operator import itemgetter

tabela = dict()
ranking = list()

for gerar in range(1, 5):
    tabela['jogadores{}'.format(gerar)] = randint(1, 6)

for k, v in tabela.items():
    print('{} tirou {} no dado'.format(k, v))
    sleep(0.3)

print("{:=^60}".format(''))
print('{:^60}'.format('== RANKING DOS JOGADORES =='))

ranking = sorted(tabela.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print("{}º lugar: {} com {}".format(i + 1, v[0], v[1]))
