"""Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda()
que consiga mostrar os números como um valor monetário formatado."""


import operações

num = float(input("Digite o preço: R$"))

print("A metade de {} é {}".format(operações.formatar(num), operações.formatar(operações.metade(num))))
print("O dobro de {} é {}".format(operações.formatar(num), (operações.formatar(operações.dobro(num)))))
print("Aumentando 10%, temos {}".format(operações.formatar(operações.desconto(num, 10))))
