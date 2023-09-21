"""Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber
como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma
pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições."""



def conta(num):
    from datetime import datetime
    resul = datetime.now().year - num
    return resul


def voto(num):
    if (num >= 18):
        return 'Voto Obrigatorio'
    elif (num < 18 and num >= 16):
        return "Voto Opcional"
    else:
        return "Não Vota"


nasc = int(input("Em que ano você nasceu? "))
idade = conta(nasc)
print("Com {} anos: {}".format(idade, voto(idade)))
