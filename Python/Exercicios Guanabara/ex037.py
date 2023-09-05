"""Exercício Python 037: Escreva um programa em Python que leia um número inteiro
qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para
hexadecimal."""


num = int(input("Digite um numero: "))
print(''' Escolha uma das bases para conversão:
[ 1 ] Converter para Binario
[ 2 ] Converter para Octal
[ 3 ] Converter para Hexadecimal ''')

escolha = 0

while True:
    escolha = int(input("Sua opção: "))

    if escolha in (1, 2, 3):
        escolha = int(escolha)
        print("Ok!")
        break
    else:
        print("Por favor, selecione uma opção válida.")

if (escolha == 1):
    print("{} convertido para Binário é igual a {}".format(num, bin(num)[2:]))
elif (escolha == 2):
    print("{} convertido para Octal é igual a {}".format(num, oct(num)[2:]))
else:
    print("{} convertido para  é igual a {}".format(num, hex(num)[2:]))