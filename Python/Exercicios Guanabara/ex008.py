"""Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em
centímetros e milímetros."""

medida = float(input("Digite uma distancia em metros\nR:"))
cm = medida * 100
mm = medida * 1000
km = medida / 1000
print(" {} corresponde a {}cm, {}mm e {}km".format(medida, cm, mm, km))
