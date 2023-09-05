"""Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome."""


nome = str(input("digite seu nome completo:\n")).strip()
print("Analisando seu nome...")
print("Seu nome completo em maiusculas é {}".format(nome.upper()))
print("Seu nome completo em minusculas é {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras".format(len(nome) - nome.count(' ')))

lista = nome.split()

print("Primeiro nome é {} e tem {} letras".format(lista[0], len(lista[0])))
