from tkinter import *
from tkinter import Tk, StringVar, ttk, messagebox
from PIL import Image,ImageTk
from views import *
from tkinter import filedialog as fd

cor0 = '#2e2d2b' # Preto
cor1 = '#feffff' # Branco
cor2 = '#4fa882' # Verde
cor3 = '#38576b' # VALOR
cor4 = '#403d3d' # LETRA
cor5 = '#e06636' # - profit
cor6 = '#038cfc' # Azul
cor7 = '#3fbfb9' # Verde2
cor8 = '#263238' # Verde3
cor9 = '#e9edf5' # Verde4


janela = Tk()

janela.title('')
janela.geometry('1300x1000+12+12')
janela.configure(background=cor9)
janela.resizable(width=True,height=True)

style = ttk.Style(janela)
style.theme_use('clam')

#frame

frame_01 = Frame(janela,width=1043,height=50,bg=cor1,relief=FLAT)
frame_01.grid(row=0,column=0)

frame_02 = Frame(janela,width=1290,height=700,pady=20,bg='blue',relief=FLAT)
frame_02.grid(row=1,column=0,pady=1,padx=1,sticky=NSEW)

frame_03 = Frame(janela,width=1290,height=303,padx=2,pady=2,bg='green',relief=FLAT)
frame_03.grid(row=4,column=0,pady=1,padx=1,sticky=NSEW)

# criando Funçoes
global tree

# Inserir
def inserir():
    global imagem,imagem_string,l_imagem

    nome = entry_nome.get()
    nivel = entry_nivel.get()
    tipo = entry_nivel.get()
    equipe = entry_equi.get()
    descicao = entry_desc.get()
    imagem = imagem_string

    lista_inserir = [nome,nivel,tipo,equipe,descicao,imagem]
    for i in lista_inserir:
        if i == '':
            messagebox.showerror("ERRO", "Preencha todos os campos")
            return
    inserir_form(lista_inserir)
    messagebox.showinfo('Sucesso','Dados Inseridos com Sucesso!')

    entry_nome.delete(0,'end')
    entry_nivel.delete(0,'end')
    entry_tipo.delete(0,'end')
    entry_equi.delete(0,'end')
    entry_desc.delete(0,'end')
    #imagem.delete(0,'end')

    return mostrar()

def atualizar():
    try:
        global imagem, imagem_string, l_imagem
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']

        valor = treev_lista[0]

        entry_nome.delete(0, 'end')
        entry_nivel.delete(0, 'end')
        entry_tipo.delete(0, 'end')
        entry_equi.delete(0, 'end')
        entry_desc.delete(0, 'end')


        id = int(treev_lista[0])
        entry_nome.insert(0,treev_lista[1])
        entry_nivel.insert(0,treev_lista[2])
        entry_tipo.insert(0, treev_lista[3])
        entry_equi.insert(0, treev_lista[4])
        entry_desc.insert(0, treev_lista[5])
        imagem_string = treev_lista[6]


        def update():
            global imagem, imagem_string, l_imagem

            nome = entry_nome.get()
            nivel = entry_nivel.get()
            tipo = entry_nivel.get()
            equipe = entry_equi.get()
            descicao = entry_desc.get()
            imagem = imagem_string

            if imagem == '':
                imagem = entry_desc.insert(0,treev_lista[7])

            lista_atualizar = [nome, nivel, tipo, equipe, descicao,imagem,id]

            for i in lista_atualizar:
                if i == '':
                    messagebox.showerror("ERRO","Preencha todos os campos")
                    return

            atualizar_form(lista_atualizar)

            messagebox.showinfo("Sucesso","Os Dados foram Atualizados com Sucesso!")



            entry_nome.delete(0, 'end')
            entry_nivel.delete(0, 'end')
            entry_tipo.delete(0, 'end')
            entry_equi.delete(0, 'end')
            entry_desc.delete(0, 'end')
            return mostrar()

            botao_conf.destroy()

        botao_conf = Button(frame_02, image=up_ima,command=update, text='  confirmar'.upper(), width=95, compound='left', anchor=NW,
                            overrelief='ridge', font=('Ivy 8 bold'), bg=cor2, fg=cor1)
        botao_conf.place(x=330, y=200)



    except IndexError:
        messagebox.showerror("ERRO", "Selecione um dos Dados na Tabela ")

def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor = treev_lista[0]

        deletar_form([valor])
        messagebox.showinfo("Sucesso","Os Dados foram DELETADOS com Sucesso!")
        mostrar()



    except IndexError:
        messagebox.showerror("ERRO", "Selecione um dos Dados na Tabela ")



# Escolher IMAGEM

global imagem, imagem_string, l_imagem


def escolher_img_H():
    global imagem, imagem_string, l_imagem

    imagem = fd.askopenfilename()
    imagem_string = imagem
    imagem = Image.open(imagem)

    imagem = imagem.resize((810, 450))
    imagem = ImageTk.PhotoImage(imagem)

    label_IMAGEM = Label(frame_02, image=imagem, width=820, height=460, anchor='center', bg=cor1, fg=cor4)
    label_IMAGEM.place(x=450, y=0)

def escolher_img_V():
    global imagem, imagem_string, l_imagem

    imagem = fd.askopenfilename()
    imagem_string = imagem
    imagem = Image.open(imagem)

    imagem = imagem.resize((470, 660))
    imagem = ImageTk.PhotoImage(imagem)

    label_IMAGEM = Label(frame_02, image=imagem, width=470, height=660, anchor='center', bg=cor1, fg=cor4)
    label_IMAGEM.place(x=450, y=0)
    texto_label = Listbox(frame_02,width=54, height=28)
    texto_label.place(x=940, y=0)

def ver_imagem():
    global imagem, imagem_string, l_imagem

    treev_dados = tree.focus()
    treev_dicionario = tree.item(treev_dados)
    treev_lista = treev_dicionario['values']

    valor = [int(treev_lista[0])]

    item = ver_item_form(valor)

    imagem = item[0][6]


    imagem = Image.open(imagem)

    imagem = imagem.resize((820,460))

    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frame_02, image=imagem, width=820, height=460, anchor='center', bg=cor1, fg=cor4)
    l_imagem.place(x=450, y=0)



# Label IMAGEM DA BUSCA
entry_vertical = Radiobutton(frame_02,text='vertical',value=0,command=escolher_img_V)
entry_vertical.place(x=240,y=200)

entry_horizontal = Radiobutton(frame_02, text='Horizontal', value=1, command=escolher_img_H)
entry_horizontal.place(x=130, y=200)


# logo
app_img = Image.open('aranha.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frame_01,image=app_img,compound=LEFT)
app_logo.place(x=0,y=0)

texto_logo = Label(frame_01,text='Cadastro de Herois',width=500,compound=LEFT,relief=RAISED,anchor="center",font=('Verdana 25 bold'),bg=cor1)
texto_logo.place(relx=0.05,rely=0.05,relwidth=0.81,relheight=0.90)

#frame 02

#label e Antrys

label_nome = Label(frame_02,text='Nome',height=1,anchor=NW,font=('Ivy 10 bold'),bg='red',fg=cor4)
label_nome.place(x=10,y=10)
entry_nome = Entry(frame_02,width=30,justify='left',relief=SOLID)
entry_nome.place(x=130,y=11)

label_nivel = Label(frame_02,text='Nivel',height=1,anchor=NW,font=('Ivy 10 bold'),bg='red',fg=cor4)
label_nivel.place(x=10,y=40)
entry_nivel = Entry(frame_02,width=30,justify='left',relief=SOLID)
entry_nivel.place(x=130,y=41)

label_tipo = Label(frame_02,text='Tipo',height=1,anchor=NW,font=('Ivy 10 bold'),bg='red',fg=cor4)
label_tipo.place(x=10,y=70)
entry_tipo = Entry(frame_02,width=30,justify='left',relief=SOLID)
entry_tipo.place(x=130,y=71)

label_equi = Label(frame_02,text='Equipe',height=1,anchor=NW,font=('Ivy 10 bold'),bg='red',fg=cor4)
label_equi.place(x=10,y=100)
entry_equi = Entry(frame_02,width=30,justify='left',relief=SOLID)
entry_equi.place(x=130,y=101)

label_desc = Label(frame_02,text='Descriçao',height=1,anchor=NW,font=('Ivy 10 bold'),bg='red',fg=cor4)
label_desc.place(x=10,y=130)
entry_desc = Entry(frame_02,width=30,justify='left',relief=SOLID)
entry_desc.place(x=130,y=131)


# Botoes
"""label_ima = Label(frame_02,text='Imagem',height=1,anchor=NW,font=('Ivy 10 bold'),bg='red',fg=cor4)
label_ima.place(x=10,y=160)
botao_ima = Button(frame_02,text='Buscar Imagem'.upper(),width=29,compound='center',anchor='center',overrelief='ridge',font=('Ivy 8'),bg=cor1,fg=cor0)
botao_ima.place(x=130,y=161)"""

# Botão Adicionar
add_ima = Image.open('simb_super.png')
add_ima = add_ima.resize((20,20))
add_ima = ImageTk.PhotoImage(add_ima)

botao_inserir = Button(frame_02,image=add_ima,text='  adicionar'.upper(),command=inserir,width=95,compound='left',anchor=NW,overrelief='ridge',font=('Ivy 8'),bg=cor1,fg=cor0)
botao_inserir.place(x=330,y=10)

# Botão Atualizar
up_ima = Image.open('simb_flesh.png')
up_ima = up_ima.resize((20,20))
up_ima = ImageTk.PhotoImage(up_ima)

botao_atual = Button(frame_02,image=up_ima,text='  atualizar'.upper(),command=atualizar,width=95,compound='left',anchor=NW,overrelief='ridge',font=('Ivy 8'),bg=cor1,fg=cor0)
botao_atual.place(x=330,y=50)



# Botão Deletar
del_ima = Image.open('simb_bat.png')
del_ima = del_ima.resize((20,20))
del_ima = ImageTk.PhotoImage(del_ima)

botao_del = Button(frame_02,image=del_ima,text='  deletar'.upper(),command=deletar,width=95,compound='left',anchor=NW,overrelief='ridge',font=('Ivy 8'),bg=cor1,fg=cor0)
botao_del.place(x=330,y=90)

# Botão Carregar Imagem
carregar_ima = Image.open('ferro.png')
carregar_ima = carregar_ima.resize((20,20))
carregar_ima = ImageTk.PhotoImage(carregar_ima)

botao_carregar = Button(frame_02,image=carregar_ima,text='  ver item '.upper(),command=ver_imagem,width=95,compound='left',anchor=NW,overrelief='ridge',font=('Ivy 8'),bg=cor1,fg=cor0)
botao_carregar.place(x=330,y=161)




# TABELA
def mostrar():
    global tree

    tabela_cabecalho = ["#",'Nome','Nível','Tipo','Equipe','Descrição','Imagem']
    lista_itens = ver_form()

    tree = ttk.Treeview(frame_03,selectmode='extended',columns=tabela_cabecalho,show='headings')

    vsb = ttk.Scrollbar(frame_03,orient='vertical',command=tree.xview)

    hsb = ttk.Scrollbar(frame_03,orient='horizontal',command=tree.xview)

    tree.configure(yscrollcommand=vsb.set,xscrollcommand=hsb.set)

    tree.grid(column=0,row=0,sticky='nsew')
    vsb.grid(column=1,row=0,sticky='ns')
    hsb.grid(column=0,row=1,sticky='ew')
    frame_03.grid_rowconfigure(0,weight=10)

    hd = ['center','center','center','center','center','center','center']
    h = [40,200,80,150,150,160,100]
    n = 0

    for col in tabela_cabecalho:
        tree.heading(col,text=col.title(),anchor='center')
        tree.column(col,width=h[n],anchor=hd[n])
        n+=1

    for item in lista_itens:
        tree.insert('','end',values=item)


mostrar()





janela.mainloop()