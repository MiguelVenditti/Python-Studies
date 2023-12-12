import sqlite3

nome = "Miguel"

idade = 18

try:

    banco = sqlite3.connect('primeiro_banco.db')

    cursor = banco.cursor()

    #  cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")

    #  cursor.execute(f"INSERT INTO pessoas VALUES('{nome}', '{idade}', 'aline.123@mail.com')")

    #  cursor.execute("DELETE from pessoas WHERE idade = 27")

    #  cursor.execute("UPDATE pessoas SET nome = 'Fabio' WHERE idade = 28")
    #  banco.commit()
    #  banco.close()
    #  print("Os dados foram removidos com sucesso!")

    cursor.execute("SELECT * FROM pessoas")
    print(cursor.fetchall())

except sqlite3.Error as erro:
    print("Erro ao excluir: ", erro)


#  cursor.execute("SELECT * FROM pessoas")
#  print(cursor.fetchall())
