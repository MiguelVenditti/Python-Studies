def metade(a=0, formato=False):
    x = a / 2
    return x if formato is False else formatar(x)


def dobro(a=0, formato=False):
    x = a * 2
    return x if formato is False else formatar(x)


def desconto(valor=0, porc=0, formato=False):
    c = (valor * porc) / 100
    x = valor + c
    return x if formato is False else formatar(x)


def formatar(valor=0, moeda='R$'):
    return '{}{:.2f}'.format(moeda, valor).replace(".", ",")


"""
O Código comentado abaixo foi a primeiras versão que fiz!
Ela funciona, contudo, ao assistir a correção, vi que a versão do professor era melhor!

def formatar(valor):
    real = int(valor)
    cent = (valor - real) * 100
    return '{},{:.0f}'.format(real, cent)
"""