"""Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada."""


n = int(input("Digite um numero!\nR:"))
dobro = n * 2
triplo = n * 3
rquadra = n ** (1/2)

print("O dobro é {}, O tiplo é {} e a raiz quadrada de {} é igual a {}".format(dobro,triplo,n,rquadra))

