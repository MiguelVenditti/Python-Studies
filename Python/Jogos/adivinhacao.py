import random

def jogar():
# Introdução

    print(27 * "*")
    print("Você entrou em uma furada!")
    print(27 * "*")
    print("Para sair dessa! Voce deverá adivinhar um Numero Secreto!")

    total_chances = 0
    pontos = 1000
    numero_secreto = random.randrange(0, 101)

# Nivel de dificuldade

    while True:
        dificuldade = input("Qual o seu nivel de habilidade?\n(1) Expert\n(2) Intermediario\n(3) Amador\nR:")

        if dificuldade in ('1', '2', '3'):
            dificuldade = int(dificuldade)
            print("Ok!")
            break
        else:
            print("Por favor, selecione uma opção válida.")

# Validando resposta!

    if (dificuldade == 1):
        total_chances = 5
    elif (dificuldade == 2):
        total_chances = 10
    else:
        total_chances = 20

# Laço de Repetição da Solicitação

    for rodada in range(1, total_chances + 1):
        print("Tentativa {} de {}.".format(rodada, total_chances))
        tentativa = input("Por favor, digite um numero de 1 a 100\nR:")
        chute = int(tentativa)

# Criação das variaveis

        acertou = chute == numero_secreto
        maior = chute < numero_secreto
        menor = chute > numero_secreto

# Apresentação de resultados
        if(chute < 1 or chute > 100):
            print("Resposta invalida! Somente numeros de 1 à 100")
            continue

        if (acertou):
            print("Parabens! Voce solucionou o problema! Sua pontuação foi {}".format(pontos))
            break
        elif (maior):
            print(" O numero misterioso é maior que sua resposta!")
        else:
            print(" O numero misterioso é menor que sua resposta!")

        pontos_perdidos = abs(chute - numero_secreto)
        pontos = pontos - pontos_perdidos

if(__name__ == "__main__"):
    jogar()