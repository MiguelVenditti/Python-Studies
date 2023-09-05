"""Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os
valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto."""


sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input("Digite uma opção valida: ")).strip().upper()[0]

print("Sexo {} registrado com sucesso".format(sexo))
