dias = int(input("Quantidade de dias alugado!\nR:"))
km = int(input("Quantidade de km percorridos!\nR:"))
valor_final = (dias * 60) + (km * 0.15)

print("O total a pagar é igual a {}".format(valor_final))
