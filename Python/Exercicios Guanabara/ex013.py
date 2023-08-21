salario = float(input("Qual o valor do salario?\nR:"))
aumento = 15
novo_salario = salario + (salario * aumento / 100)
print("O salario de R${:.2f}, receberá um aumento de {}%! Agora será R${:.2f} ".format(salario, aumento, novo_salario))
