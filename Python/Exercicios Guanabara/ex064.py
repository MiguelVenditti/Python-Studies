num = int(input("Digite um número [999 para parar]: "))
soma = 0
count = 0
while (num != 999):
    count += 1
    soma += num
    num = int(input("Digite um número [999 para parar]: "))

print("Voce somou {} vezes e o resultado foi {}".format(count, soma))
