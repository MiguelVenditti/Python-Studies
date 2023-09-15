"""Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""

list = []

while True:
    num = int(input("Digite um numero: "))
    list.append(num)
    continua = str(input("Quer continuar? [S/N] ").strip().upper()[0])
    if (continua == 'N'):
        break

print("Voce digitou {} elementos".format(len(list)))

list.sort(reverse=True)
print("De trás para frente fica: {}".format(list))

try:
    if (list.index(5)):
        print('O numero "5" faz parte da lista')
except:
    print('Não temos o numero "5" na lista')
