"""Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for."""


tabuada = int(input("Digite um número para ver sua tabuada: "))
for multiplicador in range(1, 11):
    resultado = tabuada * multiplicador
    print("{} X {} = {}".format(tabuada, multiplicador, resultado))
