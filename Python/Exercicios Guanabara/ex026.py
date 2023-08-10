texto = str(input("Digite uma frase: ")).lower().strip()
print("A letra A aparece {} vezes na frase".format(texto.count("a")))
print("A primeira letra A aparece na posição {}".format(texto.find("a")+1))
print("A ultima letra A apareceu na posição {}".format(texto.rfind("a")+1))
