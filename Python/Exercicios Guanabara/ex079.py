"""Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente. """

lista = []

while True:
    num = int(input("Digite um valor: "))
    if (num in lista):
        print("Valor duplicado! Não adicionado a lista!")
    else:
        lista.append(num)
        print("Valor adicionado com sucesso...")
    continua = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if (continua == "N"):
        break
lista.sort()
print(lista)
