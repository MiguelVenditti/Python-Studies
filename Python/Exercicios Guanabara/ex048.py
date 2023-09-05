"""Exercício Python 048: Faça um programa que calcule a soma entre todos os números que são múltiplos de
 três e que se encontram no intervalo de 1 até 500."""


cont = 0
soma = 0

for tres in range(3, 500, 6):
    cont += 1
    soma = soma + tres
print("A soma de todos os {} valores solicitados é {}".format(cont, soma))
