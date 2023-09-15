"""Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na
ordem correta."""

abre = []
fecha = []

exp = str(input("Digite sua expressão: "))

for x in exp:
    if (x == "("):
        abre.append(x)
    elif (x == ")"):
        fecha.append(x)

if (len(abre) == len(fecha)):
    print("Sua expressão esta valida")
else:
    print("Sua expressão está errada!")
