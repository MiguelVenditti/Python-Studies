"""Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços.

Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO,
ANOTARAM A DATA DA MARATONA."""


frase = str(input("Digite uma frase:")).strip().upper()
separa = frase.split()
junta = ''.join(separa)
inverso = junta[::-1]

if (inverso == junta):
    junta = frase
    inverso = junta
    print("{} foi o que voce digitou! E de trás pra frente fica\n{}".format(junta, inverso))
    print("É Palíndromo!")
else:
    print("{} foi o que voce digitou! E de trás pra frente fica\n{}".format(junta, inverso))
    print("Não é Palíndromo!")
