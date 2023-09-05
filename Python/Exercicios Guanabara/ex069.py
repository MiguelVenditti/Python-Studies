"""Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. """


maior = 0
homens = 0
mmvinte = 0

while True:
    print("{:=^30}\n{:^30}\n{:=^30}".format("", "CADASTRE UMA PESSOA", ""))
    idade = int(input("Idade: "))
    if (idade >= 18):
        maior += 1
    sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]
    if (sexo == "M"):
        homens += 1
    elif (sexo == "F" and idade < 20):
        mmvinte += 1
    print("{:=^30}".format(''))
    continua = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    while (continua not in 'SN'):
        continua = str(input("Digite uma opção valida!\nQuer continuar? [S/N] ")).strip().upper()[0]
    if (continua == 'N'):
        break
print("O total de pessoas com mais de 18 anos: {}".format(maior))
print("Ao todo temos {} homens cadastrados".format(homens))
print("E temos {} mulheres com menos de 20 anos".format(mmvinte))
