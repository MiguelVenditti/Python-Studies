from datetime import date
hoje = date.today().year
nasc = int(input("Ano de Nascimento: "))
idade = hoje - nasc

if (idade <= 9):
    print("Categoria Mirim")
elif (idade <= 14):
    print("Categoria Infantil")
elif (idade <=19):
    print("Categoria Junior")
elif (idade <=25):
    print("Categoria Senio")
else:
    print("Categoria Master")
