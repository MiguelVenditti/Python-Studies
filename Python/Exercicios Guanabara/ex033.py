val_1 = int(input("Digite um numero: "))
val_2 = int(input("Digite um novo numero: "))
val_3 = int(input("Digite mais um numer: "))

lista = [val_1, val_2, val_3]

valor_maior = max(lista)
valor_menor = min(lista)

print("O maior valor digitado foi: {}\nE o menor: {}".format(valor_maior,valor_menor))
