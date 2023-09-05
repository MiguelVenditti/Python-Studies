"""Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""


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
