"""Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu
Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida"""


peso = float(input("Qual o seu peso? (Kg) "))
alt = float(input("Qual é a sua altura? (m) "))
imc = peso / (alt ** 2)

print("O IMC dessa pessoa é de {}".format(imc))

if (imc < 18.5):
    print("Voce esta abaixo do peso ideal")
elif (18.5 <= imc < 25):
    print("Voce esta na faixa de peso ideal")
elif (25 <= imc < 30):
    print("Voce esta em sobrepeso")
elif (30 <= imc < 40):
    print("Voce esta em obesidade")
else:
    print("Voce esta em obesidade morbida")
