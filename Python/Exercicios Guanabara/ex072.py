"""Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por
 extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso."""



tupla = ("zero", "um", "dois", "três", "quatro", "cinco",
         "seis", "sete", "oito", "nove", "dez",
         "onze", "doze", "treze", "quatorze", "quinze",
         "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

while True:
    while True:
        num = int(input("Digite um número entre 0 e 20: "))
        if (num >= 0 and num <= 20):
            break
        print("Digite um número valido entre 0 e 20")
    print("Você digitou o número {}".format(tupla[num]))

    while True:
        continuar = str(input("Voce quer continuar rodando o programa? [S/N]")).strip().upper()[0]
        if(continuar in 'SN'):
            break
    if (continuar == 'N'):
        break
