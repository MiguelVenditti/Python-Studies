"""Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde
tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita
que o usuário possa mostrar as notas de cada aluno individualmente."""

alunos = list()

while True:

    name = str(input("Nome: "))
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    keep = str(input("Quer continuar: [S/N] ").strip().upper()[0])
    alunos.append([name, n1, n2])

    if (keep == 'N'):
        break
print("{:=^60}".format(''))

# Exibir Tabela
print("{:<4}{:^18}{:<6}".format('No.', 'NOME', 'MÉDIA'))
print("{:-^28}".format(''))
for num in range(0, len(alunos)):
    print("{:<4}{:^18}{:<6}".format(num, alunos[num][0], (alunos[num][1] + alunos[num][2]) / 2))
print("{:-^28}".format(''))

while True:
    ver_notas = int(input("Mostrar notas de qual aluno? (999 para encerrar): "))
    if ver_notas == 999:
        break
    if (ver_notas < 0 or ver_notas > len(alunos) -1):
        print("Digite uma opção valida!")
    else:
        print("Notas do {} são [{}, {}]".format(alunos[ver_notas][0], alunos[ver_notas][1], alunos[ver_notas][2]))

print("SISTEMA FINALIZADO!\nVOLTE SEMPRE!")
