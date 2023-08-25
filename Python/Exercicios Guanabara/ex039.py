from datetime import date
nasc = int(input("Ano de nascimento: "))
hoje = date.today().year
idade = hoje - nasc
print("Quem nasceu em {} tem {} anos em {}.".format(nasc,idade,hoje))

if (idade == 18):
    print("Voce precisa se alistar")
elif (idade < 18):
    dif = 18 - idade
    print("Ainda faltam {} anos para o alistamento".format(dif))
elif (idade > 18):
    dif = idade - 18
    print("Voce ja deveria ter se alistado há {} anos.".format(dif))
