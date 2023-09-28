def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print("Erro! {} é um preço invalido".format(entrada))
        else:
            valido = True
            return float(entrada)

