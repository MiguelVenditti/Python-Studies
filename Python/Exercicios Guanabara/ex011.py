x = float(input("Digite a largura da sua parede\nR:"))
y = float(input("Agora digite a altura\nR:"))
area = x * y
tinta = area / 2
print("A Area da sua parede é igual a {:.3f}m².".format(area))
print("Para pintar a parede voces precisará de {:.4f} L de tinta".format(tinta))
