frase = str(input("Digite uma frase:")).strip().upper()
separa = frase.split()
junta = ''.join(separa)
inverso = junta[::-1]

if (inverso == junta):
    junta = frase
    inverso = junta
    print("{} foi o que voce digitou! E de trás pra frente fica\n{}".format(junta, inverso))
    print("É Palíndromo!")
else:
    print("{} foi o que voce digitou! E de trás pra frente fica\n{}".format(junta, inverso))
    print("Não é Palíndromo!")
