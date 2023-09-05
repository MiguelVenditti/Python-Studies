"""Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
mostre os 10 primeiros termos dessa progressão."""

print("{:=^30}\n{:^30}\n{:=^30}".format("", "10 TERMOS DE UMA PA", ""))

pterm = int(input("Primeiro Termo: "))
razao = int(input("Razao: "))
decimo = pterm + (10 - 1) * razao

for pa in range (pterm, decimo, razao):
    print(pa, end=" -> ")
print("Acabou")
