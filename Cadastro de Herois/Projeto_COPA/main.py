
from tkinter import ttk
from PIL import Image,ImageTk
import PIL  #pillow

from tkinter import *


root = Tk()

class Application():
    def __init__(self,master=None):
        self.root = root
        self.tela()
        self.frames_main()
        self.widgats_principal()

        root.mainloop()

    def tela(self):
        self.root.title('Copa do Mundo')
        self.root.geometry('1200x1000+10+10')

    def frames_main(self):
        self.frame_1_main = Frame(self.root)
        self.frame_1_main.place(relx=0.01,rely=0.01,relwidth=0.98,relheight=0.20)

        self.frame_2_main = Frame(self.root,bg='blue')
        self.frame_2_main.place(relx=0.01,rely=0.22,relwidth=0.57,relheight=0.77)

        self.frame_3_main = Frame(self.root,bg='green')
        self.frame_3_main.place(relx=0.59,rely=0.22,relwidth=0.40,relheight=0.77)

        # Imagem da Label do Título
        self.lb_titulo = PIL.Image.open('img_geral/stadio.jpg')
        self.lb_titulo = self.lb_titulo.resize((1200, 200))
        self.lb_titulo = ImageTk.PhotoImage(self.lb_titulo)

        self.label_titulo = Label(self.frame_1_main, image=self.lb_titulo,
                                  text='copa do mundo'.upper(), width=900,
                                  compound=CENTER, relief=RAISED, anchor=NW,
                                  font=('verdana 70 bold'), fg='#cfd5e1')
        self.label_titulo.place(relx=0, rely=0, relwidth=1, relheight=1)

 # Botoes Label e Entry
    def widgats_principal(self):

        self.label_pesquisa = Label(self.frame_2_main, text='    pesquise aqui pelo ano e país'.upper(), font=('verdana 12 bold'), bg='lightblue')
        self.label_pesquisa.place(relx=0.01, rely=0.02, relwidth=0.50, relheight=0.03)

        self.label_ano = Label(self.frame_2_main,text='ano'.upper(),font=('verdana 12 bold'),bg='lightblue')
        self.label_ano.place(relx=0.01,rely=0.08,relwidth=0.10,relheight=0.03)

        self.entry_ano = ttk.Combobox(self.frame_2_main,font=('verdana 12 bold'))
        self.entry_ano.place(relx=0.15,rely=0.08,relwidth=0.40,relheight=0.03)

    # Imagens e Botão Busca
        self.app_bt_busca = PIL.Image.open('img_geral/bola_paises.png')
        self.app_bt_busca = self.app_bt_busca.resize((45, 45))
        self.app_bt_busca = ImageTk.PhotoImage(self.app_bt_busca)

        self.botao_ano = Button(self.frame_2_main,
                            image=self.app_bt_busca,text='pesquisar'.upper(),font=('verdana 10 bold'),
                            width=900,compound=TOP,relief=RAISED,anchor=NW)
        self.botao_ano.place(relx=0.60,rely=0.02,relwidth=0.14,relheight=0.10)


    # 1930 - URUGUAI
        self.img_botao1930 = PIL.Image.open('img_poster/1930_Uruguai.jpg')
        self.img_botao1930 = self.img_botao1930.resize((72, 89))
        self.img_botao1930 = ImageTk.PhotoImage(self.img_botao1930)

        self.botao_img1930 = Button(self.frame_2_main, image=self.img_botao1930,
                                    text=' 1930'.upper(), font=('verdana 10 bold'),
                                    width=900, compound=BOTTOM, relief=RAISED, anchor=NW)
        self.botao_img1930.place(relx=0.02, rely=0.20, relwidth=0.12, relheight=0.15)


    # 1934 - ITÁLIA
        self.img_botao1934 = PIL.Image.open('img_poster/1934_italia.jpg')
        self.img_botao1934 = self.img_botao1934.resize((72, 89))
        self.img_botao1934 = ImageTk.PhotoImage(self.img_botao1934)

        self.botao_img1934 = Button(self.frame_2_main, image=self.img_botao1934,
                                    text=' 1934'.upper(), font=('verdana 10 bold'),
                                    width=900, compound=BOTTOM, relief=RAISED, anchor=NW)
        self.botao_img1934.place(relx=0.16, rely=0.20, relwidth=0.12, relheight=0.15)

    # 1938 - FRANÇA
        self.img_botao1938 = PIL.Image.open('img_poster/1938_franca.jpg')
        self.img_botao1938 = self.img_botao1938.resize((72, 89))
        self.img_botao1938 = ImageTk.PhotoImage(self.img_botao1938)

        self.botao_img1938 = Button(self.frame_2_main, image=self.img_botao1938,
                                    text=' 1938'.upper(), font=('verdana 10 bold'),
                                    width=900, compound=BOTTOM, relief=RAISED, anchor=NW)
        self.botao_img1938.place(relx=0.30, rely=0.20, relwidth=0.12, relheight=0.15)

    # 1950 - BRASIL
        self.img_botao1950 = PIL.Image.open('img_poster/1950_brasil.jpg')
        self.img_botao1950 = self.img_botao1950.resize((72, 89))
        self.img_botao1950 = ImageTk.PhotoImage(self.img_botao1950)

        self.botao_img1950 = Button(self.frame_2_main, image=self.img_botao1950,
                                    text=' 1950'.upper(), font=('verdana 10 bold'),
                                    width=900, compound=BOTTOM, relief=RAISED, anchor=NW)
        self.botao_img1950.place(relx=0.44, rely=0.20, relwidth=0.12, relheight=0.15)

    # 1954 - SUIÇA
        self.img_botao1954 = PIL.Image.open('img_poster/1954_suica.jpg')
        self.img_botao1954 = self.img_botao1954.resize((72, 89))
        self.img_botao1954 = ImageTk.PhotoImage(self.img_botao1954)

        self.botao_img1954 = Button(self.frame_2_main, image=self.img_botao1954,
                                    text=' 1954'.upper(), font=('verdana 10 bold'),
                                    width=900, compound=BOTTOM, relief=RAISED, anchor=NW)
        self.botao_img1954.place(relx=0.58, rely=0.20, relwidth=0.12, relheight=0.15)

    # 1958 - SUÉCIA
        self.img_botao1958 = PIL.Image.open('img_poster/1958_suecia.jpg')
        self.img_botao1958 = self.img_botao1958.resize((72, 89))
        self.img_botao1958 = ImageTk.PhotoImage(self.img_botao1958)

        self.botao_img1958 = Button(self.frame_2_main, image=self.img_botao1958,
                                    text=' 1958'.upper(), font=('verdana 10 bold'),
                                    width=900, compound=BOTTOM, relief=RAISED, anchor=NW)
        self.botao_img1958.place(relx=0.72, rely=0.20, relwidth=0.12, relheight=0.15)

    # 1962 - CHILE
        self.img_botao1962 = PIL.Image.open('img_poster/1962_chile.jpg')
        self.img_botao1962 = self.img_botao1962.resize((72, 89))
        self.img_botao1962 = ImageTk.PhotoImage(self.img_botao1962)

        self.botao_img1962 = Button(self.frame_2_main, image=self.img_botao1962,
                                    text=' 1962'.upper(), font=('verdana 10 bold'),
                                    width=900, compound=BOTTOM, relief=RAISED, anchor=NW)
        self.botao_img1962.place(relx=0.86, rely=0.20, relwidth=0.12, relheight=0.15)

    # 1966 - INGLATERRA
        self.img_botao1966 = PIL.Image.open('img_poster/1962_chile.jpg')
        self.img_botao1966 = self.img_botao1966.resize((72, 89))
        self.img_botao1966 = ImageTk.PhotoImage(self.img_botao1966)

        self.botao_img1966 = Button(self.frame_2_main, image=self.img_botao1966,
                                    text=' 1966'.upper(), font=('verdana 10 bold'),
                                    width=900, compound=BOTTOM, relief=RAISED, anchor=NW)
        self.botao_img1966.place(relx=0.02, rely=0.37, relwidth=0.12, relheight=0.15)



Application()