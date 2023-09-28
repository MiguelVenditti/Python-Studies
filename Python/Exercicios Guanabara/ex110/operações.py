def metade(a=0, formato=False):
    x = a / 2
    return formatar(x) if formato is False else x


def dobro(a=0, formato=False):
    x = a * 2
    return formatar(x) if formato is False else x


def desconto(valor=0, porc=0, formato=False):
    c = (valor * porc) / 100
    x = valor - c
    return formatar(x) if formato is False else x


def acrescimo(valor=0, porc=0, formato=False):
    c = (valor * porc) / 100
    x = valor + c
    return formatar(x) if formato is False else x


def formatar(valor=0, moeda='R$'):
    return '{}{:.2f}'.format(moeda, valor).replace(".", ",")


def resumo(valor, aumet, dimin):
    print('-' * 50)
    print('{:^50}'.format('RESUMO DO VALOR'))
    print('-' * 50)
    print("{:<25}{:>24}".format('Preço analisado:', formatar(valor)))
    print("{:<25}{:>24}".format('Dobro do preço:', dobro(valor)))
    print("{:<25}{:>24}".format('Metade do preço:', metade(valor)))
    print("{:<25}{:>24}".format('{}% de aumento:'.format(aumet), acrescimo(valor, aumet)))
    print("{:<25}{:>24}".format('{}% de redução:'.format(dimin), desconto(valor, dimin)))

