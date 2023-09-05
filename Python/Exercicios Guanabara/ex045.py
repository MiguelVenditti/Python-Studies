"""Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você."""


from random import randint

jogada = ("Pedra", "Papel", "Tesoura")
maquina = randint(0,2)

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

while True:
    try:
        escolha = int(input("Qual é a sua jogada? "))

        if escolha in (0, 1, 2):
            escolha = int(escolha)
            break
        else:
            print("Por favor, selecione uma opção válida.")
    except ValueError:
        print("Por favor, insira um número válido.")

print("{:=^25}".format("JO KEN PO"))
print("Voce jogou {}".format(jogada[escolha]))
print("Seu adversario jogou {}".format(jogada[maquina]))

if (escolha == maquina):
    print("{:=^25}".format(" EMPATE "))
elif (escolha == 0 and maquina == 1 or escolha == 1 and maquina == 2 or escolha == 2 and maquina == 0):
    print("{:=^25}".format(" DERROTA "))
else:
    print("{:=^25}".format(" VITORIA "))
