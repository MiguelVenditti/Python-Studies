"""Exercicio Python 095: Aprimore o desafio 93 para que ele funcione com v�rios jogadores,
incluindo um sistema de visualiza��o de detalhes do aproveitamento de cada jogador."""


cadastro = list()

# Registrar dados

while True:

    jogador = dict()
    jogador['nome'] = str(input("Nome do Jogador: "))
    partidas = int(input("Quantas partidas {} jogou? ".format(jogador['nome'])))

    gol = list()

    for x in range(0, partidas):
        gol.append(int(input("Quantos gols na {}� partida? ".format(x + 1))))

    while True:
        terminar = str(input("Quer continuar? [S/N] ").strip().upper()[0])

        if (terminar in 'SN'):
            break
        print('Erro! Por favor, Digite apenas "S" ou "N"!')

    jogador['gols'] = gol[:]
    jogador['total'] = sum(gol)
    cadastro.append(jogador.copy())

    if (terminar == 'N'):
        break

print('{:=^60}'.format(''))

# Exibir Tabela
print("{:<4}{:^12}{:<20}{:<6}".format('Cod.', 'NOME', 'GOLS', 'TOTAL'))

print("{:-^42}".format(''))

for k, v in enumerate(cadastro):
    gols_formatados = ', '.join(map(str, v['gols']))
    print("{:<4}{:^12}{:<20}{:<6}".format(k, v['nome'], gols_formatados, v['total']))

print("{:-^42}".format(''))

# Exibir detalhes de cada nome cadastrado

while True:
    detalhes = int(input("Mostrar dados de qual jogador? (999 para encerrar) "))
    if (detalhes == 999):
        break
    if (detalhes < 0 or detalhes > len(cadastro) -1):
        print("Digite uma op��o valida!")
    else:
        print("     -- LEVANTAMENTO DO JOGADOR {} -- ".format(cadastro[detalhes]['nome']))

        for pos, gols in enumerate(cadastro[detalhes]['gols']):
            print("No jogo {} fez {} gols.".format(pos + 1, gols))

""" A primeira vez que solucionei o desafio, utilizei o codigo abaixo! Por�m a vers�o acima � mais curta e legivel!

        for x in range(0, len(cadastro[detalhes]['gols'])):
            print("No jogo {} fez {} gols.".format(x + 1, cadastro[detalhes]['gols'][x]))"""

print("<< PROGRAMA ENCERRADO >>")
