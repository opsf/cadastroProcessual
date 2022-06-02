from tkinter import *
from tkinter import ttk
import datetime as dt
from bancoDados import *

co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"  # letra
co5 = "#e06636"  # - profit
co6 = "#038cfc"  # azul
co7 = "#ef5350"  # vermelha
co8 = "#263238"  # + verde
co9 = "#e9edf5"  # sky blue

janela = Tk()

janela.title('BENEFÍCIOS')
janela.geometry('1137x453')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)


def inserir():
    global tree

    nome = e_nome.get()
    beneficio = combo_beneficio.get()
    data = e_data.get()
    operacao = combo_operacao.get()
    processo = e_processo.get()

    lista = [nome, beneficio, data, operacao, processo]

    inserir_info(lista)  # insere o cadastro no banco de dados

    tree.insert("", 'end', values=lista)  # insere o cadastro no treeview

def suspender():
    global tree
    a = tree.focus()
    b = tree.item(a,
                  "values")  # b será uma tupla, só que queremos mudar somente a operacao. A tupla não pode ser mudada então teremos que converter para lista
    c = list(b)  # a lista pode ser mudada e nós vamos mudar o ultimo elemento para Suspensão
    c.insert(3, 'Suspensão')  # inserindo Suspensão na posição 3
    c.pop()  # exluindo a ultima posição
    inserir_info(c)  # insere o focus no banco de dados
    tree.insert("", 'end', values=c)  # insere a mudança em uma nova arvore  no treeview
    print(c)
    # AINDA TENHO QUE TROCAR A DATA PARA A DATA EM QUE FOI REALIZADA A SUSPENSÃO


def excluir():
    global tree
    a = tree.focus()  # coloca o elemento da árvore treeviw focado na variável a. São vários os elementos mas queremos só os valores
    b = tree.item(a, "values")  # extrai somente os values (aquilo que é visível no treeview)
    tree.delete(a)  # exlui o elemento selecionado da árvore. No entanto temos que exluir do banco de dados

    c = [b[0], b[3]]

    exluir_info(c)  # irá excluir do banco de dados o item selecionado do treeview


################### Dividindo a janela principal ######################

frame_cima = Frame(janela, width=310, height=50, background=co2, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=403, background=co1, relief='flat')
frame_baixo.grid(row=1, column=0, pady=1, padx=1)

frame_direita = Frame(janela, width=588, height=403, background=co1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, pady=0, padx=1)

###################### Label cima ########################

app_nome = Label(frame_cima, text='Cadastro de Beneficios', anchor=NW, font=('Helvetica', '16'), background=co2)
app_nome.place(x=10, y=10)

###################### Configurando frame-baixo ########################

l_nome = Label(frame_baixo, text='Nome*', anchor=NW, font=('Helvetica', '12'), bg=co1)
l_nome.place(x=10, y=10)

e_nome = Entry(frame_baixo, width=40, relief=SOLID)
e_nome.place(x=10, y=40)

l_beneficio = Label(frame_baixo, text='Beneficio*', anchor=NW, font=('Helvetica', '12'), bg=co1)
l_beneficio.place(x=10, y=90)

b_list = ["Auxílio transporte", "Pre Escolar", "Natalidade", "AGU transporte"]
b_list.sort()
combo_beneficio = ttk.Combobox(frame_baixo, values=b_list)
combo_beneficio.place(x=10, y=120)

l_data = Label(frame_baixo, text='Data*', anchor=NW, font=('Helvetica', '12'), bg=co1)
l_data.place(x=10, y=170)

## Definindo o valor padrão do entry data ##

dataPadrao = StringVar()
now = dt.datetime.now()
b = now.strftime("%d/%m/%y")
dataPadrao.set(b)
e_data = Entry(frame_baixo, width=12, relief=SOLID, textvariable=dataPadrao)
e_data.place(x=10, y=200)

l_operacao = Label(frame_baixo, text='Operacao*', anchor=NW, font=('Helvetica', '12'), bg=co1)
l_operacao.place(x=150, y=170)

vlist = ["Exclusão", "Suspensão", "Inclusão", "Atualização"]
vlist.sort()
combo_operacao = ttk.Combobox(frame_baixo, values=vlist)
combo_operacao.place(x=150, y=200)

l_processo = Label(frame_baixo, text='Processo*', anchor=NW, font=('Helvetica', '12'), bg=co1)
l_processo.place(x=10, y=240)
e_processo = Entry(frame_baixo, width=40, relief=SOLID)
e_processo.place(x=10, y=270)


#######BOTOÕES###########

## Botao incluir ##
b_inserir = Button(frame_baixo, text='Incluir', command=inserir, font=('Helvetica', '12'), bg=co6, fg=co1)
b_inserir.place(x=10, y=340)

## Botao excluir##
b_excluir = Button(frame_baixo, text='Excluir', command=excluir, font=('Helvetica', '12'), bg=co6, fg=co1)
b_excluir.place(x=65, y=340)

## Botao suspender##
b_suspender = Button(frame_baixo, text='Suspender', command=suspender,  font=('Helvetica', '12'), bg=co6, fg=co1)
b_suspender.place(x=127, y=340)

## Botao atualizar##
b_atualizar = Button(frame_baixo, text='Atualizar', font=('Helvetica', '12'), bg=co6, fg=co1)
b_atualizar.place(x=220, y=340)


###################### Configurando frame-direita (TREEVIW) ########################

def mostrar():
    global tree
    df_list = mostrar_info()  # pega a tabela que está no banco de dados e coloca na variável df_list

    head = ["Nome", "Beneficio","Data", "Operacao", "Processo"]
    tree = ttk.Treeview(frame_direita, columns=head, height=20, show='headings')

    tree.heading('#0', text='vazio')
    tree.heading('Nome', text='Nome')
    tree.heading('Beneficio', text='Beneficio')
    tree.heading('Data', text='Data')
    tree.heading('Operacao', text="Operacao")
    tree.heading('Processo', text="Processo")

    tree.column("Nome", width=280)
    tree.column("Data", width=100)
    tree.column("Operacao", width=110)
    tree.column("Beneficio", width=160)
    tree.column("Processo", width=150)

    vsb = ttk.Scrollbar(frame_direita, orient='vertical', command=tree.yview)
    hsb = ttk.Scrollbar(frame_direita, orient='horizontal', command=tree.xview)
        

    for i in df_list:
        tree.insert("", 'end', values=i)

    tree.grid(column=0, row=0)
    vsb.grid(column=1, row=0)
    hsb.grid(column=0, row=1)


mostrar()

janela.mainloop()