soma = 0
count = 0
while True:
    num = int(input("Digite um número [999 para parar]: "))
    if (num == 999):
        break
    count += 1
    soma += num

print("Voce somou {} vezes e o resultado foi {}".format(count, soma))
