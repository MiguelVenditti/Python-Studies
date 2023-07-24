c1 = float(input("Cumprimento do cateto oposto\nR:"))
c2 = float(input("Cumprimento do cateto adjacente\nR:"))
hipo = (c1 ** 2 + c2 ** 2) **(1/2)

print("O valor da hipotenusa é igual a {:.2f}".format(hipo))
