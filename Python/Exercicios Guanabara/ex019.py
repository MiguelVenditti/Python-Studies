"""Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido."""


import random

v1 = input("Primeiro Aluno\nR:")
v2 = input("Segundo Aluno\nR:")
v3 = input("Terceido Aluno\nR:")
v4 = input("Quarto Aluno\nR:")

lista = [v1, v2, v3, v4]
sorteado = random.choice(lista)

print("O aluno escolhido foi {}".format(sorteado))
