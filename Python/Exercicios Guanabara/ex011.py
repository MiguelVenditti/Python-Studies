"""Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados."""


x = float(input("Digite a largura da sua parede\nR:"))
y = float(input("Agora digite a altura\nR:"))
area = x * y
tinta = area / 2
print("A Area da sua parede é igual a {:.3f}m².".format(area))
print("Para pintar a parede voces precisará de {:.4f} L de tinta".format(tinta))
