"""Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora
a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat()
com a mesma funcionalidade."""


def num(msg):
    while True:
        try:
            x = int(input(msg))
        except (ValueError, TypeError):
            print("Erro! Por favor, digite um número inteiro válido.")
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuario.')
            return 0
        else:
            return x


n = num("Digite um valor: ")
print("O valor digitado foi {}".format(n))
