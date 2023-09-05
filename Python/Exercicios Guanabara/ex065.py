num = int(input("Digite um número: "))
count = 1
soma = num
maior = 0
menor = 999999

continua = str(input("Quer continuar? [S/N] ")).strip().upper()[0]

while continua != 'N':
    num = int(input("Digite um número: "))

    if (num > maior):
        maior = num
    if (num < menor):
        menor = num

    continua = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    count += 1
    soma += num

media = soma / count

print("Você digitou {} números e a média foi {:.2f}".format(count, media))
print("O maior valor foi {} e o menor foi {}".format(maior, menor))
