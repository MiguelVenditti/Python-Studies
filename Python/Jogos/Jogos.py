import adivinhacao
import forca

print("Bem vindo ao menu principal de jogos!\nPor favor escolha uma das opções!")

jogo = int(input("Escolha (1) Para adivinhação ou (2) para Forca\nR:"))

if(jogo == 1):
    print("Iniciando Jogo de Adivinhação")
    adivinhacao.jogar()
elif(jogo == 2):
    print("Jogando Forca")
    forca.jogar()