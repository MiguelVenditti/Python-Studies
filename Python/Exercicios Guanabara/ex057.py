sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input("Digite uma opção valida: ")).strip().upper()[0]

print("Sexo {} registrado com sucesso".format(sexo))
