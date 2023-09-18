"""Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média"""


pessoa = dict()
cadastro = list()
tot = 0

# Loop para cadastro
while True:
    pessoa['nome'] = str(input('Nome: '))

    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ').strip().upper()[0])
        if (pessoa['sexo'] in 'MF'):
            break
        print("Erro! Por favor, digite apenas M ou F.")

    pessoa['idade'] = int(input("Idade: "))

    while True:
        finalizar = str(input('Quer continuar? [S/N] ').strip().upper()[0])
        if (finalizar in 'SN'):
            break
        print("Erro! Por favor, digite apenas S ou N.")

    # Armazenando dados

    tot += 1
    cadastro.append(pessoa.copy())

    if (finalizar == 'N'):
        break

# Média de idades

total = 0

for x in range(0, len(cadastro)):
    total += cadastro[x]['idade']

media = (total / len(cadastro))

# Validando Mulheres Cadastradas

mulheres = list()

for x in range(0, len(cadastro)):
    if (cadastro[x]['sexo'] == 'F'):
        mulheres.append(cadastro[x]['nome'])

# Validando pessoas acima da media de idade

acima = list()

for x in range(0, len(cadastro)):
    if (cadastro[x]['idade'] > media):
        acima.append(cadastro[x].copy())

print('{:=^60}'.format(''))

# Exibição de resultados

print("A) Ao todo temos {} pessoas cadastradas.".format(tot))
print("A média de idade é de {} anos".format(media))
print("As mulheres cadastradas foram {}".format(mulheres))
print("Lista das pessoas que estão acima da média de idade:\n{}".format(acima))
print()
print("<< ENCERADO >>")
