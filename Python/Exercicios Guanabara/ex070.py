"""Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. """


caro = 0
barato = 9999999999
nomebarato = ''
total = 0

print("{:=^30}\n{:^30}\n{:=^30}".format("", "LOJÃO SUPER BARATÃO", ""))

while True:
    nome = str(input("Nome do Produto: "))
    valor = float(input("Preço: "))
    total += valor
    if (valor > 1000):
        caro += 1
    if (valor < barato):
        barato = valor
        nomebarato = nome.capitalize()

    continua = str(input("Mais alguma compra? [S/N] ")).strip().upper()[0]
    while (continua not in 'SN'):
        continua = str(input("Digite uma opção valida!\nMais alguma compra? [S/N] ")).strip().upper()[0]
    if (continua == 'N'):
        break

print("Valor total das compras foi R${:.2f}".format(total))
print("Temos {} produtos custando mais de R$1000.00".format(caro))
print("O produto mais barato foi {} que custa R${:.2f}".format(nomebarato, barato))