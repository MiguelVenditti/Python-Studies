cont = 0
soma = 0

for tres in range(3, 500, 6):
    cont += 1
    soma = soma + tres
print("A soma de todos os {} valores solicitados é {}".format(cont, soma))
