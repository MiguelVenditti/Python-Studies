n = str(input("informe um numero:\n"))
print("Analisando o numero {}".format(n))
print("Unidade: {}".format(n[-1]))
if (n[-2] == True):
    print("Dezena: {}".format(n[-2]))
else:
    print("Seu numero termina por aqui!")
print("Centena: {}".format(n[-3]))
print("Milhar: {}".format(n[-4]))
