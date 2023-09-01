print("{:=^30}\n{:^30}\n{:=^30}".format("", "10 TERMOS DE UMA PA", ""))

pterm = int(input("Primeiro Termo: "))
razao = int(input("Razao: "))
decimo = pterm + (10 - 1) * razao
print(decimo)
for pa in range (pterm, decimo, razao):
    print(pa, end=" -> ")
print("Acabou")
