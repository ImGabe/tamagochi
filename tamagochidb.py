import sqlite3
import os

# Função para criar um pasta
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

# Cria uma pasta chamada "database".
createFolder('./database/')

# Cria um Local Storage chamado tamagochidb.
conn = sqlite3.connect('./database/tamagochidb.db')
cursor = conn.cursor()
# Cria uma tabela toda errada se não existir.
cursor.execute('CREATE TABLE IF NOT EXISTS  tamagochi (ID INT PRIMARY KEY UNIQUE, Nome VARCHAR (255) UNIQUE NOT NULL, lvl INT NOT NULL)')

# Função para adicionar um tamagochi na tabela
def adicionar(nome, lvl):
    cursor.execute("INSERT INTO tamagochi (Nome, Lvl) VALUES (?,?)", (nome,lvl))
    conn.commit()
    conn.close()

