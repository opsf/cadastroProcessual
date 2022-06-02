import sqlite3

conn = sqlite3.connect('cadastroProcessual.db')

# criando tabela
with conn:
    cur = conn.cursor()
    cur.execute(''' CREATE TABLE IF NOT EXISTS dadosCadastrais(nome TEXT, beneficio TEXT,data date, operacao TEXT, processo TEXT)''')

# inserindo dados

def inserir_info(i):
    with conn:
        cur = conn.cursor()
        query = '''INSERT INTO dadosCadastrais(nome, beneficio, data, operacao, processo) VALUES (?,?,?,?,?)'''
        cur.execute(query,i)


# consultando tabela
def mostrar_info():

    with conn:
        cur = conn.cursor()
        query = '''SELECT * FROM dadosCadastrais'''

        lista = cur.execute(query).fetchall()
        print(lista)
    return lista

# atualizando tabela
def atualizar_info():
    with conn:
        cur = conn.cursor()
        query = '''UPDATE dadosCadastrais SET operacao=? WHERE nome = ?'''
        cur.execute(query)


lista = ['orlando pedro', 'inclusão']
def exluir_info(lista):
    with conn:
        cur = conn.cursor()
        query = '''DELETE FROM dadosCadastrais WHERE nome = ? AND operacao = ?'''
        cur.execute(query, lista)

mostrar_info()
exluir_info(lista)