import sqlite3

conn = sqlite3.connect('cadastroProcessual.db')

# criando tabela
with conn:
    cur = conn.cursor()
    cur.execute(''' CREATE TABLE IF NOT EXISTS dadosCadastrais(nome TEXT, beneficio TEXT, data DATE, operacao TEXT, processo TEXT, observacao TEXT)''')

# inserindo dados

def inserir_info(i):
    with conn:
        cur = conn.cursor()
        query = '''INSERT INTO dadosCadastrais(nome, beneficio, data, operacao, processo, observacao) VALUES (?,?,?,?,?,?)'''
        cur.execute(query,i)


# consultando tabela
def mostrar_info():
    with conn:
        cur = conn.cursor()
        query = '''SELECT * FROM dadosCadastrais'''
        lista = cur.execute(query).fetchall()
    return lista

# atualizando tabela
def atualizar_info():
    with conn:
        cur = conn.cursor()
        query = '''UPDATE dadosCadastrais SET operacao=? WHERE nome = ?'''
        cur.execute(query)



def exluir_info(lista):
    with conn:
        cur = conn.cursor()
        query = '''DELETE FROM dadosCadastrais WHERE nome = ? AND operacao = ?'''
        cur.execute(query, lista)

mostrar_info()
