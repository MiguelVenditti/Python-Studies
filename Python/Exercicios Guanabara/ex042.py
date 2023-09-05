"""Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo
 de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes"""


print("-=-=-=" * 5)
print("Analisador de Triângulos")
print("-=-=-=" * 5)

r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))

if (r1 > (r2 + r3) or r2 > (r1 + r3) or r3 > (r1 + r2)):
    print("Os segmentos acima NÃO PODEM FORMAR um triângulo")
    if (r1 == r2 and r2 == r3):
        print("E o triângulo é Equilatero")
    elif (r1 != r2 and r2 != r3 and r1 != r3):
        print("E o triângulo é Escaleno")
    else:
        print("E o triângulo é Isósceles")
else:
    print("Os segmentos acima PODEM FORMAR um triângulo")
