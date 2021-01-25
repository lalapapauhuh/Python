import sqlite3

dbase = sqlite3.connect("employee_records.db")
cur = dbase.cursor()
dbase.execute(""" CREATE TABLE IF NOT EXISTS employee_records(
                  ID INT PRIMARY KEY NOT NULL,
                  NAME TEXT NOT NULL)""")

# Aplica todas as mudanças na database
dbase.commit()

# Função que escreve ID NAME dentro da database
def write(ID, NAME):
    cur.execute(""" INSERT into employee_records(ID, NAME) VALUES(? ?)""", (ID, NAME))
    dbase.commit()
