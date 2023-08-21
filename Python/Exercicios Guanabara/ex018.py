from math import radians, sin, cos, tan

angulo = float(input("Digite o angulo que voce deseja\nR: "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print("O ângulo de {} tem o seno de {:.2f}, cosseno de {:.2f} e a tangente de {:.2f}".format(angulo, seno, cosseno, tangente))
