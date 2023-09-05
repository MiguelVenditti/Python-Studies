"""Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo. """


tabuada = int(input("Digite um número para ver sua tabuada: "))

while (tabuada >= 0):
    for multiplicador in range(1, 11):
        resultado = tabuada * multiplicador
        print("{} X {} = {}".format(tabuada, multiplicador, resultado))
    tabuada = int(input("Digite um número para ver sua tabuada: "))
