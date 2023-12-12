import sqlite3
from datetime import datetime


def conexao():

    banco = sqlite3.connect('jogadores.db')
    return banco


def escolha_inicial():
    print("Olá, bem-vindo ao Sistema de cadastro e análise de desempenho dos atletas do Palmeiras!\n")
    while True:
        escolha = str(
            input(("Digite o número correspondente a opção que deseja:\n"
                   "1 - Escolher um jogador\n"
                   "2 - Exibir tabela\n"
                   "3 - Opções para dirigentes\n\n"
                   "Digite sua opção: ").strip()))

        if escolha in ('1', '2', '3'):
            break
        else:
            print("Algo deu errado! Escolha novamente uma opção válida!")
    return escolha


def escolha_inicial_op1():

    while True:
        escolha_nome = str(input("Digite o nome do Atleta: "))

        if escolha_nome.replace(" ", "").isalpha():
            return escolha_nome
        else:
            print("Algo deu errado! Digite novamente um nome válido!")


def leitura(sql):
    db = conexao()
    cursor = db.cursor()
    cursor.execute(sql)
    resultado = cursor.fetchall()
    db.close()
    return resultado


def deletar(info):
    db = conexao()
    cursor = db.cursor()
    comando_sql = f"DELETE FROM jogadores WHERE num_camisa = {info}"
    cursor.execute(comando_sql)
    db.commit()
    db.close()


def exibir_um_jogador(nome):
    nome_limpo = ''
    for corrige_nome in nome.split():
        nome_limpo += corrige_nome.capitalize() + " "

    vsql = """SELECT num_camisa, nome, nasc,
           nacionalidade, altura, init_contrato,
           pe, contrato, valor, posicao
           FROM jogadores WHERE nome='{}'""".format(nome_limpo.strip())
    resultado = leitura(vsql)
    for r in resultado:
        print(r)


def exibir_tabela(valor):

    if valor == '0':

        vsql = "SELECT num_camisa, nome, nasc, " \
           "nacionalidade, altura, init_contrato, " \
           "pe, contrato, valor, posicao " \
           "FROM jogadores"
        resultado = leitura(vsql)
        for r in resultado:
            print(r)


def escolha_inicial_op2():
    option = 0

    while True:
        escolha_op2 = str(input("Deseja filtrar por posição? [S/N] ").strip().upper()[0])

        if escolha_op2 not in "SN":
            print("Algo deu errado! Digite novamente uma opção válida!")
        elif escolha_op2 == "S":
            option += 1
            while True:
                print("Digite um numero correspondente a sua escolha:\n\n"
                      "1 - Goleiro\n"
                      "2 - Zagueiro\n"
                      "3 - Lateral\n"
                      "4 - Meio-Campo\n"
                      "5 - Ataque\n")
                escolha_op2_1 = str(input("Escolha: "))

                if escolha_op2_1.isnumeric():
                    if int(escolha_op2_1) < 1 or int(escolha_op2_1) > 5:
                        print("Opção inválida!")
                    else:
                        option += int(escolha_op2_1)
                        break
            break
        else:
            break
    return option


def escolha_inicial_op3():
    while True:
        escolha_op3 = str(input(("Digite o número correspondente a opção que deseja:\n"
                                 "1 - Cadastrar um novo jogador\n"
                                 "2 - Atualizar um jogador\n"
                                 "3 - Deletar um jogador\n\n"
                                 "Digite sua opção: ").strip()))

        if escolha_op3 in ('1', '2', '3'):
            break

        else:
            print("Algo deu errado! Escolha novamente uma opção válida!")

    return escolha_op3


def converter_data(data):
    try:
        data_formatada = datetime.strptime(data, "%d/%m/%Y").strftime("%Y-%m-%d")
        return data_formatada
    except ValueError:
        print("Formato de data inválido. Certifique-se de usar o formato dd/mm/aaaa.")
        return None


def cadastrar_jogador(num_camisa, nome, nasc,
                      nacionalidade, altura, init_contrato,
                      pe, contrato, valor, posicao, classe):
    db = conexao()

    try:
        cursor = db.cursor()
        cursor.execute("INSERT INTO jogadores VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                       (num_camisa, nome, nasc, nacionalidade, altura, init_contrato, pe, contrato, valor, posicao,
                        classe))
        db.commit()
        print("Jogador cadastrado com sucesso!")
    except sqlite3.Error as error:
        print("Erro ao cadastrar jogador:", error)
    finally:
        db.close()


def menu_cadastral():
    num_camisa, nome, nasc, \
        nacionalidade, altura, init_contrato, \
        pe, contrato, valor, \
        posicao, classe = obter_informacoes()

    print("\nConfira as informações:")
    print("Número da camisa:", num_camisa)
    print("Nome:", nome)
    print("Data de nascimento:", nasc)
    print("Nacionalidade:", nacionalidade)
    print("Altura:", altura)
    print("Data de início do contrato:", init_contrato)
    print("Pé principal:", pe)
    print("Data do final do contrato:", contrato)
    print("Valor de mercado:", valor)
    print("Posição do jogador:", posicao)
    print("Classe:", classe)

    confirmacao = input("\nAs informações estão corretas? (S/N): ").strip().upper()

    if confirmacao == 'S':
        cadastrar_jogador(num_camisa, nome, nasc, nacionalidade, altura, init_contrato, pe, contrato, valor, posicao,
                          classe)
    else:
        print("Cadastro cancelado.")


def obter_informacoes():
    num_camisa = int(input('Digite abaixo as informações necessárias:\nNúmero da camisa que o jogador irá usar: '))
    nome = str(input('Nome: '))
    data_nascimento = str(input("Digite a data de nascimento (dd/mm/aaaa): "))
    nasc = converter_data(data_nascimento)
    nacionalidade = str(input("Nacionalidade do jogador: "))
    altura = float(input("Altura: "))
    primeira_data = str(input("Digite a data de início do contrato (dd/mm/aaaa): "))
    init_contrato = converter_data(primeira_data)
    pe = str(input("Pé principal para chute: "))
    fim_data = str(input("Digite a data do final do contrato (dd/mm/aaaa): "))
    contrato = converter_data(fim_data)
    valor = float(input("Valor de mercado: "))
    posicao = str(input("Posição do jogador: "))
    classe = int(input("Qual área o jogador atua?\n1 = Goleiro\n2 = Defesa\n3 = Meio Campo\n4 = Ataque\n"))

    return num_camisa, nome, nasc, nacionalidade, altura, init_contrato, pe, contrato, valor, posicao, classe


def jogador_selecionado(num):

    vsql = "SELECT nome FROM jogadores WHERE num_camisa='{}'".format(num)
    resultado = leitura(vsql)
    return resultado


def menu_selecionar():
    while True:
        escolha = str(input("Digite o número da camisa correspondente ao jogador que deseja:\n").strip())
        if escolha.isnumeric():
            break
        else:
            print("Algo deu errado! Escolha novamente uma opção válida!")
    return escolha


def certifica_delete(num):

    print(f"{jogador_selecionado(num)[0][0]} é o jogador que corresponde a camisa {num}!")

    while True:
        aceitar = str(input("Deseja mesmo excluir o jogador selecionado? [S/N]").strip().upper()[0])

        if aceitar in ('S', 'N'):
            break

    if aceitar == 'N':
        print("Ok! Selecione outro jogador")
        return 1
    else:
        deletar(num)
        return 0
