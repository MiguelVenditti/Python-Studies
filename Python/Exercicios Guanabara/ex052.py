num = int(input("Digite um número: "))
vezes = 0

for c in range(1, num + 1):
    if (num % c == 0):
        print("\033[34m", end=" ")
        vezes += 1
    else:
        print("\033[31m", end=" ")
    print("{}".format(c), end=" ")

print("\n\033[mO número {}  foi divisível {} vezes".format(num,vezes))
if (vezes == 2):
    print("Ele é primo!")
else:
    print("Ele NÃO é primo!")