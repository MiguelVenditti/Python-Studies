from time import sleep

n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
escolha = ''

while True:
    print("Escolha uma das opções abaixo\n"
          "[ 1 ] Somar\n"
          "[ 2 ] Multiplicar\n"
          "[ 3 ] Maior\n"
          "[ 4 ] Novos Números\n"
          "[ 5 ] Sair do Programa")

    escolha = str(input("Qual é a sua opção? "))

    if (escolha == '1'):
        soma = n1 + n2
        print("{:=^30}".format(''))
        print("A soma entre {} + {} é {}".format(n1, n2, soma))
        print("{:=^30}".format(''))
        sleep(4)

    elif (escolha == '2'):
        mult = n1 * n2
        print("{:=^30}".format(''))
        print("A multiplicação entre {} e {} é igual a {}".format(n1, n2, mult))
        print("{:=^30}".format(''))
        sleep(4)

    elif (escolha == '3'):
        if (n1 > n2):
            print("{:=^30}".format(''))
            print("Entre {} e {}. {} é maior".format(n1, n2, n1))
            print("{:=^30}".format(''))
            sleep(4)
        else:
            print("{:=^30}".format(''))
            print("Entre {} e {}. {} é maior".format(n1, n2, n2))
            print("{:=^30}".format(''))
            sleep(4)

    elif (escolha == '4'):
        print("{:=^30}".format(''))
        n1 = int(input("Escolha um novo número para o Primeiro valor: "))
        n2 = int(input("Escolha um novo número para o Segundo valor: "))
        print("{:=^30}".format(''))
        sleep(2)

    elif (escolha == '5'):
        print("Obrigado por usar nosso sistema!")
        break
    else:
        print("{:=^30}".format(''))
        print("Por favor, escolha uma opção valida!")
        print("{:=^30}".format(''))
        sleep(2)


