import sqlite3


def conexao():
    banco = sqlite3.connect('jogadores.db')
    return banco


def leitura(sql):
    db = conexao()
    cursor = db.cursor()
    cursor.execute(sql)
    resultado = cursor.fetchall()
    db.close()
    return resultado


def menu_selecionar():
    while True:
        escolha = str(input("Digite o número da camisa correspondente ao jogador que deseja:\n").strip())
        if escolha.isnumeric():
            break
        else:
            print("Algo deu errado! Escolha novamente uma opção válida!")
    return escolha


def jogador_selecionado(num):
    vsql = "SELECT num_camisa, nome, nasc, " \
           "nacionalidade, altura, init_contrato, " \
           "pe, contrato, valor, posicao, classe FROM jogadores WHERE num_camisa='{}'".format(num)
    resultado = leitura(vsql)
    return resultado


def converte_tupla_para_variaveis(tupla):
    num_camisa, nome, nasc, nacionalidade, altura, init_contrato, pe, contrato, valor, posicao, classe = tupla
    return num_camisa, nome, nasc, nacionalidade, altura, init_contrato, pe, contrato, valor, posicao, classe


def atualizar_jogador(num_camisa, nome, nasc,
                      nacionalidade, altura, init_contrato,
                      pe, contrato, valor, posicao, classe):
    db = conexao()

    try:

        # Exibir e atualizar o nome
        novo_nome = input(f"Nome atual: {nome}\nDigite o novo nome (ou pressione Enter para manter o mesmo): ")
        if novo_nome:
            nome = novo_nome

        # Exibir e atualizar a data de nascimento
        nova_nasc = input(f"Data de nascimento atual: {nasc}\nDigite a nova data de nascimento "
                          f"(ou pressione Enter para manter a mesma): ")
        if nova_nasc:
            nasc = nova_nasc

        novo_nacionalidade = input(f"Nacionalidade atual: {nacionalidade}\n"
                                   f"Digite a nova nacionalidade (ou pressione Enter para manter o mesmo): ")
        if novo_nacionalidade:
            nacionalidade = novo_nacionalidade

        novo_altura = input(f"Altura atual: {altura}\n"
                            f"Digite a nova altura (ou pressione Enter para manter o mesmo): ")
        if novo_altura:
            altura = novo_altura

        novo_init_contrato = input(f"Data atual do inicio de contrato: {init_contrato}\n"
                                   f"Digite a nova data (ou pressione Enter para manter o mesmo): ")
        if novo_init_contrato:
            init_contrato = novo_init_contrato

        novo_pe = input(f"Pe atual: {pe}\n"
                        f"Digite a nova informação do pé (ou pressione Enter para manter o mesmo): ")
        if novo_pe:
            pe = novo_pe

        novo_contrato = input(f"Fim de contrato atual: {contrato}\n"
                              f"Digite o novo fim de contrato (ou pressione Enter para manter o mesmo): ")
        if novo_contrato:
            contrato = novo_contrato

        novo_valor = input(f"Valor atual: {valor}\n"
                           f"Digite o novo valor (ou pressione Enter para manter o mesmo): ")
        if novo_valor:
            valor = novo_valor

        novo_posicao = input(f"Posição atual: {posicao}\n"
                             f"Digite a nova posição (ou pressione Enter para manter o mesmo): ")
        if novo_posicao:
            posicao = novo_posicao

        novo_classe = input(f"Nome atual: {classe}\n"
                            f"Digite a nova classe (ou pressione Enter para manter o mesmo): ")
        if novo_classe:
            classe = novo_classe

        cursor = db.cursor()

        # Atualizar os dados no banco de dados
        cursor.execute("UPDATE jogadores SET nome=?, nasc=?, nacionalidade=?,"
                       " altura=?, init_contrato=?, pe=?, contrato=?, valor=?,"
                       " posicao=?, classe=? WHERE num_camisa=?",
                       (nome, nasc, nacionalidade,
                        altura, init_contrato, pe,
                        contrato, valor, posicao, classe, num_camisa))
        db.commit()
        print("Dados do jogador atualizados com sucesso!")

    except sqlite3.Error as error:
        print("Erro ao atualizar os dados do jogador:", error)

    finally:
        if db is not None:
            db.close()


# MAIN
num = menu_selecionar()

# Obter os dados do jogador
dados = jogador_selecionado(num)

# Verificar se há dados
if dados:
    # Converter a tupla para variáveis
    num_camisa, nome, nasc, nacionalidade, altura, init_contrato, pe,\
        contrato, valor, posicao, classe = dados[0]

    # Atualizar o jogador
    atualizar_jogador(num_camisa, nome, nasc,
                      nacionalidade, altura, init_contrato,
                      pe, contrato, valor, posicao, classe)
else:
    print("Jogador não encontrado.")
