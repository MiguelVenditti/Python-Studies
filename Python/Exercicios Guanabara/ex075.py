"""Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares."""


x1 = int(input("Digite o primeiro numero: "))
x2 = int(input("Agora o segundo: "))
x3 = int(input("Terceiro: "))
x4 = int(input("Ultimo: "))

x = (x1, x2, x3, x4)

print("Voce digitou os valores: ", x)
print("O número 9 apareceu {} vezes".format(x.count(9)))
print("O primeiro número 3 aparece na posição {}".format(x.index(3) +1 ))
print("Os números pares que aparecem na tupla são:")

for c in x:
    if (c % 2 == 0):
        print(c, end=' ')