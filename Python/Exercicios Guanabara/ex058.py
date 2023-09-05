"""Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um
número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer."""


from random import randint
from time import sleep
numero = randint(0, 10)
count = 1

print ("Pensei em um numero de 0 a 10. Tente adivinhar...")

chute = int(input("Em que numero eu pensei? "))
print("Analisando...")
sleep(0.80)

while (chute != numero):
    count += 1
    if (chute < numero):
        chute = int(input("O numero que pensei é maior "))
    else:
        chute = int(input("O numero que eu pensei é menor "))

if chute == numero:
    print("Parabens! Voce venceu! em apenas {} chance(s)\nO numero secreto era {}!".format(count, numero))
