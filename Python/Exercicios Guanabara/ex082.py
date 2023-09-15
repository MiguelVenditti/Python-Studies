"""Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente. Ao final, mostre o conteúdo das três listas geradas."""


impar = []
par = []
lista = []

while True:
    num = int(input("Digite um número: "))
    lista.append(num)
    if (num % 2 == 0):
        par.append(num)
    else:
        impar.append(num)
    continua = str(input("Quer continuar? [S/N] ").strip().upper()[0])
    if (continua == 'N'):
        break

print("A lista completa é {}".format(lista))
print("A lista de pares é {}".format(par))
print("A lista de impartes é {}".format(impar))
