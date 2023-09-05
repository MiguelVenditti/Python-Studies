"""Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou
no final do jogo. """


from random import randint
print("{:=^30}\n{:^30}\n{:=^30}".format("", "Vamos jogar Par ou Impar", ""))
count = 0

while True:
    num = int(input("Digite um valor: "))
    parimpar = str(input("Par ou Impar? [P/I] ")).strip().upper()[0]
    comp = randint(0, 11)
    winlose = (num + comp) % 2
    if (winlose == 0):
        winlose = 'P'
    else:
        winlose = 'I'

    if (parimpar == winlose):
        count += 1
        print("Voce jogou {} e o adversario {}, isso é {}".format(num, comp, winlose))
        print("Voce VENCEU!")
        print("Vamos para a {}ª rodada".format(count + 1))
    else:
        print("Voce jogou {} e o adversario {}, isso é {}".format(num, comp, winlose))
        break

print("GAME OVER! Você venceu {} vezes".format(count))