"""Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o
(com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o
ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar."""


from datetime import datetime
pessoa = dict()

pessoa['nome'] = str(input("Nome: "))
nasc = int(input("Ano de Nascimento: "))
pessoa['idade'] = datetime.now().year - nasc
pessoa['ctps'] = int(input("Carteira de Trabalho (0 caso não tenha): "))
if (pessoa['ctps'] != 0):
    pessoa['contrato'] = int(input("Ano de Contratação: "))
    pessoa['salario'] = float(input("Salário: R$"))
    pessoa['aposentadoria'] = ((pessoa['contrato'] + 35) - datetime.now().year)

print('{:=>60}'.format(''))

for k, v in pessoa.items():
    print("     - {} tem o valor {}".format(k.capitalize(), v))
