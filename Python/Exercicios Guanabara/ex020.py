"""Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de
trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada."""

import random

v1 = input("Primeiro Aluno\nR:")
v2 = input("Segundo Aluno\nR:")
v3 = input("Terceido Aluno\nR:")
v4 = input("Quarto Aluno\nR:")

lista = [v1, v2, v3, v4]
random.shuffle(lista)

print ("A ordem de apresentação será: ")
print(lista)
