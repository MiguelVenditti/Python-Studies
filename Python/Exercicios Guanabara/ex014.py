"""Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e
converta para graus Fahrenheit."""

celsius = float(input("Informe a temperatura em graus celsius\nR:"))
fah = (celsius * 9/5) + 32

print("A temperatura de {}°C corresponde a {}°F".format(celsius,fah))
