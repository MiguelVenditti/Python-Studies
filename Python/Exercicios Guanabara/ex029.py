velo = int(input("Qual é a velocidade atual do carro?\n"))
multa = 0
if (velo > 80):
    multa = (velo - 80) * 7
    print("MULTADO! Você excedeu o limite prmitido que é de 80Lm/h\nVocê deve pagar uma multa de R${:.2f}".format(multa))
print("Tenha um bom dia! Dirija com segurança")