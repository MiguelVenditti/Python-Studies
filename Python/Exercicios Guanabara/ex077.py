"""Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais."""


x = ("APRENDER", "PROGRAMAR", "LINGUAGEM", "PYTHON", "CURSO",
     "GRATIS", "ESTUDAR", "PRATICAR", "TRABALHAR",
     "MERCADO", "PROGRAMADOR", "FUTURO")

for palavra in x:
    print("\n A palavra {} tem as vogais:".format(palavra),  end=" ")
    for vogais in palavra:
        if (vogais.lower() in "aeiou"):
            print(vogais, end=" ")


