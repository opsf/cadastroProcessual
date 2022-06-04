from tkinter import *
from tkinter import ttk
from bancoDados import *
from tkinter import messagebox



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

def pesquisa():

    top = Tk()

    ###################### retornando dados da pesquisa ########################

    def pesquisar():
        global tree

        # COLOCAR AQUI O CODIGO PARA LIMPEZA DO TREEVIEW - PESQUISAR


        lista = mostrar_info()  # mostra uma lista de tuplas cadastradas no banco de dados

        nome = e_p_nome.get() # pega o valor escrito no campo nome
        beneficio = combo_p_beneficio.get() # pega o valor selecionado no campo Escolha o beneficio
        data = e_p_data.get()
        operacao = combo_operacao.get()
        processo = e_p_processo.get()

        for tupla in lista:

            if tupla[0] == nome or tupla[1] == beneficio or tupla[2]==data or tupla[3]==operacao or tupla[4]==processo:
                tree.insert("", 'end', values=tupla)


        ######## limpando os campos de entrada da pesquisa##########
        e_p_nome.delete(0,"end")
        combo_p_beneficio.delete(0, "end")
        e_p_data.delete(0, "end")
        combo_operacao.delete(0, "end")
        e_p_processo.delete(0, "end")







    ################### Dividindo a janela top ######################

    frame_top_cima = Frame(top, width=1000, height=100, background=co1, relief='flat')
    frame_top_cima.grid(row=0, column=0)

    frame_top_baixo = Frame(top, width=1000, height=403, background=co1, relief='flat')
    frame_top_baixo.grid(row=1, column=0)


    ###################### Configurando frame-top_cima ########################

    l_p_nome = Label(frame_top_cima, text='Digite o nome', anchor=NW, font=('Helvetica', '12'), bg=co1)
    l_p_nome.place(x=10, y=10)

    e_p_nome = Entry(frame_top_cima, width=40, relief=SOLID)
    e_p_nome.place(x=10, y=30)

    l_p_beneficio = Label(frame_top_cima, text='Escolha o beneficio', anchor=NW, font=('Helvetica', '12'), bg=co1)
    l_p_beneficio.place(x=300, y=10)

    b_p_list = ["Auxílio transporte", "Pre Escolar", "Natalidade", "AGU transporte"]
    b_p_list.sort()
    combo_p_beneficio = ttk.Combobox(frame_top_cima, values=b_p_list)
    combo_p_beneficio.place(x=300, y=30)

    l_p_data = Label(frame_top_cima, text='Data(dd/mm/aa)', anchor=NW, font=('Helvetica', '12'), bg=co1)
    l_p_data.place(x=500, y=10)

    e_p_data = Entry(frame_top_cima, width=18, relief=SOLID)
    e_p_data.place(x=500, y=30)

    l_p_operacao = Label(frame_top_cima, text='Operacao*', anchor=NW, font=('Helvetica', '12'), bg=co1)
    l_p_operacao.place(x=650, y=10)

    vlist = ["Exclusão", "Suspensão", "Inclusão", "Atualização"]
    vlist.sort()
    combo_operacao = ttk.Combobox(frame_top_cima, values=vlist, width=10)
    combo_operacao.place(x=650, y=30)

    l_p_processo = Label(frame_top_cima, text='Processo*', anchor=NW, font=('Helvetica', '12'), bg=co1)
    l_p_processo.place(x=750, y=10)
    e_p_processo = Entry(frame_top_cima, width=40, relief=SOLID)
    e_p_processo.place(x=750, y=30)

    #######BOTOÕES###########

    ##Botão pesquisar##
    b_p_pesquisar = Button(frame_top_cima, text='Pesquisar', command=pesquisar, font=('Helvetica', '12'), bg=co6, fg=co1)
    b_p_pesquisar.place(x=450, y=60)

    ###################### Configurando frame-top_baixo ########################

    global tree

    head = ["Nome", "Beneficio", "Data", "Operacao", "Processo", 'Observacao']
    tree = ttk.Treeview(frame_top_baixo, columns=head, height=20, show='headings')

    tree.heading('#0', text='vazio')
    tree.heading('Nome', text='Nome')
    tree.heading('Beneficio', text='Beneficio')
    tree.heading('Data', text='Data')
    tree.heading('Operacao', text="Operacao")
    tree.heading('Processo', text="Processo")
    tree.heading('Observacao', text="Observacao")

    tree.column("Nome", width=280)
    tree.column("Beneficio", width=160)
    tree.column("Data", width=100)
    tree.column("Operacao", width=110)
    tree.column("Processo", width=150)
    tree.column('Observacao', width=280)

    vsb = ttk.Scrollbar(frame_top_baixo, orient='vertical', command=tree.yview)
    hsb = ttk.Scrollbar(frame_top_baixo, orient='horizontal', command=tree.xview)



    tree.grid(column=0, row=0)
    vsb.grid(column=1, row=0)
    hsb.grid(column=0, row=1)



    top.mainloop()

pesquisa()