"""Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
 mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite."""


velo = int(input("Qual é a velocidade atual do carro?\n"))
multa = 0
if (velo > 80):
    multa = (velo - 80) * 7
    print("MULTADO! Você excedeu o limite prmitido que é de 80Lm/h\nVocê deve pagar uma multa de R${:.2f}".format(multa))
print("Tenha um bom dia! Dirija com segurança")