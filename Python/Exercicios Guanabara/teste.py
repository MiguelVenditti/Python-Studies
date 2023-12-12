import datetime
import sqlite3
import functions

def idade():
    nasc = "SELECT nasc FROM jogadores"

    # Converta a data de nascimento para um objeto de data
    data_de_nascimento = datetime.datetime.strptime(nasc, "%Y-%m-%d")

    # Obtenha a data atual
    data_atual = datetime.datetime.now()

    # Calcule a diferença entre as datas para obter a idade
    idade = data_atual.year - data_de_nascimento.year

    # Verifique se a data atual ainda não atingiu o aniversário deste ano
    if data_atual.month < data_de_nascimento.month or (
            data_atual.month == data_de_nascimento.month and data_atual.day < data_de_nascimento.day):
        idade -= 1  # Ainda não fez aniversário este ano, subtrai 1 da idade
