"""Exercício Python 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média."""


p_nota = float(input("Digite a primeira nota\n"))
s_nota = float(input("Digite a segunda nota\n"))
media = (p_nota + s_nota) / 2

print("A media entre {:.1f} e {:.1f} é igual a {:.1f}".format(p_nota, s_nota, media))
