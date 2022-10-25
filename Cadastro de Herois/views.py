
import sqlite3 as lite

con = lite.connect('banco_dados.db')

with con:
    cur = con.cursor()
    cur.execute('''CREATE TABLE if not exists cadastro( id INTEGER PRIMARY KEY  AUTOINCREMENT, nome TEXT,nivel INT,tipo TEXT,equipe TEXT,descricao TEXT,imagem TEXT)''')


def inserir_form(i):
    with con:
        cur = con.cursor()
        query = ('''INSERT INTO cadastro(nome,nivel,tipo,equipe,descricao,imagem) VALUES (?,?,?,?,?,?)''')
        cur.execute(query,i)


def atualizar_form(i):
    with con:
        cur = con.cursor()
        query = (''' UPDATE cadastro SET nome=?,nivel=?,tipo=?,equipe=?,descricao=?,imagem=? where id=?''')
        cur.execute(query,i)


def deletar_form(i):
    with con:
        cur = con.cursor()
        query = ('''DELETE FROM cadastro WHERE id=?''')
        cur.execute(query,i)


def ver_form():
    ver_dados = []
    with con:
        cur = con.cursor()
        query = ('''SELECT * FROM cadastro''')
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            ver_dados.append(row)
    return ver_dados


def ver_item_form(id):
    ver_dados_individual = []
    with con:
        cur = con.cursor()
        query = ('''SELECT * FROM cadastro WHERE id=?''')
        cur.execute(query,id)

        rows = cur.fetchall()
        for row in rows:
            ver_dados_individual.append(row)
    return ver_dados_individual
