print("{:=^30}\n{:^30}\n{:=^30}".format("", "10 TERMOS DE UMA PA", ""))

pterm = int(input("Primeiro Termo: "))
razao = int(input("Razao: "))
termo = pterm
count = 1

while (count <= 10):
    print("{}".format(termo), end=" -> ")
    termo += razao
    count += 1

print("Acabou")
