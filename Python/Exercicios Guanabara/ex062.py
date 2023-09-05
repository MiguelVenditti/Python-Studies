print("{:=^30}\n{:^30}\n{:=^30}".format("", "10 TERMOS DE UMA PA", ""))

pterm = int(input("Primeiro Termo: "))
razao = int(input("Razao: "))
termo = pterm
count = 1

while (count <= 10):
    print("{}".format(termo), end=" -> ")
    termo += razao
    count += 1

mais = int(input("Quantos termos voce quer mostar a mais? "))


while mais != 0:
    count = 1
    while (count <= mais):
        print("{}".format(termo), end=" -> ")
        termo += razao
        count += 1
    mais = int(input("Quantos termos voce quer mostrar a mais? "))

print("Fim! Voce repetiu", count, " vezes")
