from random import randint
numero = randint(0,5)

print ("Pensei em um numero de 0 a 5. Tente adivinhar...")

chute = int(input("Em que numero eu pensei?"))
print("Analisando...")

if chute == numero:
    print ("Parabens! VOce conseguiu me vencer!")
else:
    print ("Haha, voce perdeu! O numero era {} e não {}!".format(numero,chute))
