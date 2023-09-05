"""Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente."""


nome = str(input("Digite seu nome completo: ")).strip().capitalize()
nomes = nome.split()

print("Muito prazer em te conhecer!")

print("Seu primeiro nome é {}".format(nomes[0]))
print("Seu ultimo nome é {}".format(nomes[-1].capitalize()))