nome = str(input("digite seu nome completo:\n")).strip()
print("Analisando seu nome...")
print("Seu nome completo em maiusculas é {}".format(nome.upper()))
print("Seu nome completo em minusculas é {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras".format(len(nome) - nome.count(' ')))

lista = nome.split()

print("Primeiro nome é {} e tem {} letras".format(lista[0], len(lista[0])))
