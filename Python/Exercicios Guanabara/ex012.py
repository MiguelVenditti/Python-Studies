valor_produto = float(input("Qual o valor do produto?\nR:"))
desconto = 5
novo_valor = valor_produto - (valor_produto * desconto / 100)
print("O produto que custava R${:.2f}, na promoção com desconto de {}% vai custar R${:.2f}".format(valor_produto, desconto, novo_valor))
