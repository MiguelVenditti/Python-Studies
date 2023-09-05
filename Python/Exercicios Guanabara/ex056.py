"""Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e
quantas mulheres têm menos de 20 anos."""


total_idades = 0
total_pessoas = int(input("Digite o numero total de pessoas que deseja cadastrar: "))
mais_velho = ''
idade_maior = 0
mulheres = 0

for p in range(1, total_pessoas + 1):  # Laço de repetição
    print("{:-^25}".format(" {}ª Pessoa ".format(p)))

    # Solicitando dados ao usuario

    nome = str(input("Nome: ")).strip().capitalize()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]")).strip().upper()

    # Tratando os dados

    if (sexo == "M" and idade > idade_maior):
        idade_maior = idade
        mais_velho = nome

    if (sexo == "F" and idade < 20):
        mulheres += 1

    total_idades += idade  # Acumulando as idades

# Calculando a média
media = total_idades / total_pessoas
print("Média de idade:", media)

print("A média de idade do grupo é de {:.1f}".format(media))
print("O homem mais velho tem {} anos e se chama {}".format(idade_maior, mais_velho))
print("Ao todo são {} mulheres com menos de 20 anos".format(mulheres))
