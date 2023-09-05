"""Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu."""


from random import randint
numero = randint(0,5)

print ("Pensei em um numero de 0 a 5. Tente adivinhar...")

chute = int(input("Em que numero eu pensei?"))
print("Analisando...")

if chute == numero:
    print ("Parabens! VOce conseguiu me vencer!")
else:
    print ("Haha, voce perdeu! O numero era {} e não {}!".format(numero,chute))
