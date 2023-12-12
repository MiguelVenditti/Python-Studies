import functions

OPCAO_1_EXIBIR_JOGADOR = '1'


while True:
    inicio = functions.escolha_inicial()

    if inicio == OPCAO_1_EXIBIR_JOGADOR:
        nome = functions.escolha_inicial_op1()
        functions.exibir_um_jogador(nome)

    elif inicio == "2":
        functions.escolha_inicial_op2()
    else:
        escolha = functions.escolha_inicial_op3()

        if escolha == '1':
            functions.menu_cadastral()

        elif escolha == '3':
            while True:
                num = functions.menu_selecionar()
                fim = functions.certifica_delete(num)
                if fim == 0:
                    break

    continuar = str(input('Digite "S" para voltar ao menu inicial ou "N" para encerrar o programa!\n'
                          'R: ').strip().upper()[0])
    if continuar == 'N':
        break
