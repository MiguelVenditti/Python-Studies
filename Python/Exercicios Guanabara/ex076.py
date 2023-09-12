"""Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos
 preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular."""

tabela = ("Canela", 3.90,
          "Cravo", 3.0,
          "Pimenta", 5.0,
          "Cuminho", 2.75,
          "Mel", 12,
          "Sal", 15,
          "Açucar", 10)

for x in range (0, len(tabela)):
    if (x % 2 == 0):
        print("{:.<30}".format(tabela[x]), end="")
    else:
        print("R${:.>2.2f}".format(tabela[x]))

