n = str(input("informe um numero:\n"))
comprimento = len(n)

print("Analisando o numero {}".format(n))

if comprimento < 4:
    n = n.zfill(4)

print("Unidade: {}".format(n[-1]))

# Validando e Exibindo cada digito!

if (n[-2] + n[-3] + n[-4] == "000"):
    print("Seu numero acaba por aqui")
elif (n[-3] + n[-4] == "00"):
    print("Dezena: {}".format(n[-2]))
    print("Seu numero acaba por aqui")
elif n[-4] == "0":
    print("Dezena: {}".format(n[-2]))
    print("Centena: {}".format(n[-3]))
    print("Seu numero acabou por aqui")
else:
    print("Dezena: {}".format(n[-2]))
    print("Centena: {}".format(n[-3]))
    print("Milhar: {}".format(n[-4]))

# correção_guanabara:

# num = int(input("informe um numero: "))
# u = num // 1 % 10
# d = num // 10 % 10
# c = num // 100 % 10
# m = num // 1000 % 10

# print ("Analisando o numero {}".format(num))
# print ("Unidade: {}".format(u))
# print ("Dezena: {}".format(d))
# print ("Centena: {}".format(c))
# print ("Milhar: {}".format(m))

'''
if (n[-4: -1] == "000"):
    print("Seu numero acaba por aqui")
elif (n[-3: -1] == "00"):
    print("Dezena: {}".format(n[-2]))
    print("Seu numero acaba por aqui")
elif n[-4] == "0":
    print("Dezena: {}".format(n[-2]))
    print("Centena: {}".format(n[-3]))
    print("Seu numero acabou por aqui")
else:
    print("Dezena: {}".format(n[-2]))
    print("Centena: {}".format(n[-3]))
    print("Milhar: {}".format(n[-4]))'''