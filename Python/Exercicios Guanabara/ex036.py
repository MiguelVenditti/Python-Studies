vl_casa = float(input("Qual o valor da casa?"))
salario = float(input("Qual o salario do comprador?"))
anos = int(input("Em quantos anos deseja parcelar?"))

prestacao = salario / (anos * 12)

print("{:.2f}".format(prestacao))