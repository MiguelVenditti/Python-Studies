#Entrada de Dados do usuario
palavra = input("Digite algo\nR:")

# Seguencia padrão do exercicios
print("O tipo da sua palavra é ", type(palavra))
print("Voce não digitou nada, só colocou espaço?!", palavra.isspace())
print("É um numero?", palavra.isnumeric())
print("É Alfabetico?", palavra.isalpha())
print("É alfa Numerico?", palavra.isalnum())
print("Esta em maiusculas?", palavra.isupper())
print("Esta em minusculas?", palavra.islower())
print("Esta capitalizada?", palavra.istitle())

# Validando a tipagem da variavel! E Solucionando bug "type"
numerico = palavra.isnumeric()

if (numerico == True):
    palavra = int(palavra)
    print("O tipo da sua palavra é ", type(palavra))
    print("Fim do exercicio!")
