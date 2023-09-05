'''  Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai
informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.  '''


print("{:=^30}\n{:^30}\n{:=^30}".format("", "BANCO MV", ""))

valor = int(input("Qual o valor que deseja sacar? R$"))
cedula50 = int(valor / 50)
cedula20 = int((valor % 50) / 20)
cedula10 = int(((valor % 50) % 20) / 10)
cedula1 = int((((valor % 50) % 20) % 10) / 1)

if (cedula50 > 0):
    print("Total de {} cédulas de R$50".format(cedula50))
if (cedula20 > 0):
    print("Total de {} cédulas de R$20)".format(cedula20))
if (cedula10 > 0):
    print("Total de {} cédulas de R$10".format(cedula10))
if (cedula1 > 0):
    print("Total de {} cédulas de R$1".format(cedula1))
print("{:=^30}".format(''))
print("Volte sempre ao Banco MV! Tenha um bom dia!")
