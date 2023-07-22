valor_produto = float(input("Qual o valor do produto?\nR:"))
desconto = 5
r_dtres = valor_produto * desconto
valor_descontado = r_dtres / 100
valor_final = valor_produto - valor_descontado

print("O produto que custava R${:.2f}, na promoção com desconto de {}% vai custar R${:.2f}".format(valor_produto, desconto, valor_final))
