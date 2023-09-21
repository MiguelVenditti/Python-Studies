"""Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM',
o programa se encerrará. Importante: use cores."""


def busca(x):
    help(x)

def titulo(txt):
    x = len(txt) + 4
    print('=' * x)
    print('  {}'.format(x))
    print('=' * x)


resposta = ''

while True:
    titulo('SISTEMA DE AJUDA PYHELP')
    resposta = str(input("Função ou Biblioteca > "))
    if (resposta.upper() == 'FIM'):
        break
    else:
        busca(resposta)

titulo('ATÉ LOGO')
