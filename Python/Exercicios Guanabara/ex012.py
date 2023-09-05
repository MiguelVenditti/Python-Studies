"""Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
com 5% de desconto."""


valor_produto = float(input("Qual o valor do produto?\nR:"))
desconto = 5
novo_valor = valor_produto - (valor_produto * desconto / 100)
print("O produto que custava R${:.2f}, na promoção com desconto de {}% vai custar R${:.2f}".format(valor_produto, desconto, novo_valor))
