vl_casa = float(input("Qual o valor da casa?"))
salario = float(input("Qual o salario do comprador?"))
anos = int(input("Em quantos anos deseja parcelar?"))

prestacao = vl_casa / (anos * 12)
limite = salario * 30 / 100

print("Para pagar uma casa de {:.2f} em {} anos, a prestação será de {:.2f}".format(vl_casa,anos,prestacao))

if (prestacao > limite):
    print("Emprestimo NEGADO")
else:
    print("Emprestimo CONCEDIDO")



