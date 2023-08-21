import random

v1 = input("Primeiro Aluno\nR:")
v2 = input("Segundo Aluno\nR:")
v3 = input("Terceido Aluno\nR:")
v4 = input("Quarto Aluno\nR:")

lista = [v1, v2, v3, v4]
sorteado = random.choice(lista)

print("O aluno escolhido foi {}".format(sorteado))
