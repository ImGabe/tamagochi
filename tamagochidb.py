import sqlite3
import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        
createFolder('./database/')
conn = sqlite3.connect('./database/tamagochidb.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS  tamagochi (ID INT PRIMARY KEY UNIQUE, Nome VARCHAR (255) UNIQUE NOT NULL, lvl INT NOT NULL)')

def adicionar(nome, lvl):
    cursor.execute("INSERT INTO tamagochi (Nome, Lvl) VALUES (?,?)", (nome,lvl))
    conn.commit()
    conn.close()

def remover(nome):
    pass

def listarTudo(table):
    cursor.execute('SELECT * FROM ?',(table))
    print(cursor.fetchone())
    conn.close()