"""Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome."""


nome = str(input("Digite o seu nome: ")).strip().upper()
nomes = nome.split()
nomein = str(("SILVA" in nomes))


print("Seu nome tem Silva?", nomein)