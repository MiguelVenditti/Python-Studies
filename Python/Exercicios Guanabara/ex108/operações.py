def metade(a):
    x = a / 2
    return x


def dobro(a):
    x = a * 2
    return x


def desconto(valor, porc):
    c = (valor * porc) / 100
    x = valor + c
    return x

def formatar(valor=0 , moeda ='R$'):
    return '{}{}'.format(moeda, valor).replace(".", ",")

"""
O Código comentado abaixo foi a primeiras versão que fiz!
Ela funciona, contudo, ao assistir a correção, vi que a versão do professor era melhor!

def formatar(valor):
    real = int(valor)
    cent = (valor - real) * 100
    return '{},{:.0f}'.format(real, cent)
"""