tabuada = int(input("Digite um número para ver sua tabuada: "))

while (tabuada >= 0):
    for multiplicador in range(1, 11):
        resultado = tabuada * multiplicador
        print("{} X {} = {}".format(tabuada, multiplicador, resultado))
    tabuada = int(input("Digite um número para ver sua tabuada: "))
