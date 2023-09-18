"""Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também
a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela."""


aluno = dict()
aluno['nome'] = str(input("Nome: "))
aluno['media'] = float(input("Média de  {}: ".format(aluno["nome"])))
if aluno['media'] >= 7:
    aluno['status'] = "Aprovado"
elif aluno['media'] >= 5 and aluno ['media'] < 7:
    aluno['status'] = "Recuperação"
else:
    aluno['status'] = "Reprovado"

for k, v in aluno.items():
    print("      - {} é igual a {}".format(k, v))
