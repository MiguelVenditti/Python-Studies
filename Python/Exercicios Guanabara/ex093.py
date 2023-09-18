"""Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols
feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo
o total de gols feitos durante o campeonato."""

futebol = dict()
gols = list()

futebol['nome'] = str(input("Nome do Jogador: "))

partidas = int(input("Quantas partidas {} jogou? ".format(futebol['nome'])))

for x in range(1, partidas + 1):
    gols.append(int(input('Quantos gols na {}ª partida? '.format(x))))

futebol['gol'] = gols[:]
futebol['total'] = sum(gols)

print('{:=^60}'.format(''))

print(futebol)

print('{:=^60}'.format(''))

for k, v in futebol.items():
    print("O campo {} tem o valor {}".format(k, v))

print('{:=^60}'.format(''))

print("O jogador {} jogou {} partidas".format(futebol['nome'], partidas))

for x in range(1, len(gols) + 1):
    print("    - Na partida {}, fez {} gols".format(x, gols[x - 1]))
print("Foi um total de {} gols".format(futebol['total']))
