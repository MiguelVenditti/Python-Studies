"""Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um
parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
desenvolvida no desafio 108."""


import operações

num = float(input("Digite o preço: R$"))

print("A metade de {} é {}".format(operações.formatar(num), operações.metade(num, formato=True)))
print("O dobro de {} é {}".format(operações.formatar(num), (operações.dobro(num, formato=True))))
print("Aumentando 10%, temos {}".format(operações.desconto(num, 10, formato=True)))
