"""Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções."""


import operações

num = float(input("Digite o preço: R$"))

print("A metade de R${} é R${}".format(num, operações.metade(num)))
print("O dobro de R${} é R${}".format(num, operações.dobro(num)))
print("Aumentando 10%, temos R${}".format(operações.desconto(num, 10)))
