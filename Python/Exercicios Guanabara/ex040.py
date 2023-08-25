n1 = float(input("Primeira Nota: "))
n2 = float(input("Segunda Nota: "))

media = (n1 + n2) / 2

print("Tirando {} e {}, a média do aluno é {}".format(n1,n2,media))

if (media < 5):
    print("O aluno esta REPROVADO")
elif (media >= 5 and media <= 7):
    print("O aluo esta de RECUPERAÇÂO")
else:
    print("O aluno esta APROVADO")