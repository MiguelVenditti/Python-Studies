import random

v1 = input("Primeiro Aluno\nR:")
v2 = input("Segundo Aluno\nR:")
v3 = input("Terceido Aluno\nR:")
v4 = input("Quarto Aluno\nR:")

lista = [v1, v2, v3, v4]
random.shuffle(lista)

print ("A ordem de apresentação será: ")
print(lista)
