nome = str(input("Digite seu nome completo: ")).strip().capitalize()
nomes = nome.split()

print("Muito prazer em te conhecer!")

print("Seu primeiro nome é {}".format(nomes[0]))
print("Seu ultimo nome é {}".format(nomes[-1].capitalize()))