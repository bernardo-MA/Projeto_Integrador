from tkinter import *
from conexaob import conecta
import pymysql
from pymysql import Error
from PIL import Image, ImageTk
import customtkinter


class front:
    def __init__(self):
        self.janela = Tk()
        self.escfull=None
        self.escfull=False
        self.cur=None
        self.pedido=[]
        self.datas = ["2025-07-28"]
        self.lista=[]

        ##IMAGENS
        self.expresso = PhotoImage(file='img/expresso.png')
        self.cappuccino = PhotoImage(file='img/cappuccino.png')
        self.latte = PhotoImage(file='img/latte.png')
        self.mocca = PhotoImage(file='img/mocca.png')
        self.pdq = PhotoImage(file='img/paodequeijo.png')
        self.torta = PhotoImage(file='img/torta.png')
        self.pastel = PhotoImage(file='img/pastel.png')
        self.concluido = PhotoImage(file='img/botaoconcluido.png')
        self.confirmar = PhotoImage(file='img/botaoconfirmar.png')
        self.retorno = PhotoImage(file='img/f5.png')
        self.lixeira = PhotoImage(file='img/lixeira.png')
        # self.confirmar_o = Image.open("img/botaoconfirmar.png")
        # self.confirmar_n = self.confirmar_o.resize((65,65))
        # self.confirmar = ImageTk.PhotoImage(self.confirmar_n)
        # self.retorno_o = Image.open("img/f5.png")
        # self.retorno_n = self.retorno_o.resize((125,125))
        # self.retorno = ImageTk.PhotoImage(self.retorno_n)
        # self.lixeira_o = Image.open("img/lixeira.png")
        # self.lixeira_n = self.lixeira_o.resize((65,65))
        # self.lixeira = ImageTk.PhotoImage(self.lixeira_n)
        self.voltf5=PhotoImage(file="img/f5.png")


    def mysqlconnect(self):
        try:
            self.conn = pymysql.connect(
                host='localhost',
                user='root', 
                password = '',
                db='cafeteria',
                )
            
            self.cur = self.conn.cursor()
            
            # self.conn.close()
        except pymysql.MySQLError as e:
            print(f"Deu erro porra {e}")

    def telacheia(self, event):
        self.escfull = not self.escfull
        self.janela.attributes("-fullscreen", self.escfull)
        
    def window(self, event):
        self.escfull = False
        self.janela.attributes("-fullscreen", False)

    ##FUNÇOES BOTOES
    def confirmardata(self):    
        self.datan = self.dtnova.get()
        self.datas.append(self.datan)
        self.atend.destroy()
        self.telaatend()

    def incompleto(self):
        self.listaorg=", ".join(self.lista)
        self.cur.execute('INSERT INTO barista (pedidocompl) VALUES (%s)',(self.listaorg,))
        self.lista.clear()
        self.garcom.destroy()
        self.telagarcom()

    def Outro(self):
        self.opção1.config(bg="#38312D");self.opção1.config(state=NORMAL)
        self.opção2.config(bg="#38312D");self.opção2.config(state=NORMAL)
        self.opção3.config(bg="#38312D");self.opção3.config(state=NORMAL)
        self.opção4.config(bg="#38312D");self.opção4.config(state=NORMAL)
        self.opção5.config(bg="#38312D");self.opção5.config(state=NORMAL)
        self.opção6.config(bg="#38312D");self.opção6.config(state=NORMAL)
        self.opção7.config(bg="#38312D");self.opção7.config(state=NORMAL)

    def Expresso(self):
        self.produto = "Expresso"
        self.Outro()
        self.opção1.config(state=DISABLED)

    def Cappuccino(self):
        self.produto = "Cappuccino"
        self.Outro()
        self.opção2.config(state=DISABLED)
    def Latte(self):
        self.produto = "Latte"
        self.Outro()
        self.opção3.config(state=DISABLED)
    def Mocca(self):
        self.produto = 'Mocca'
        self.Outro()
        self.opção4.config(state=DISABLED)
    def Torta(self):
        self.produto = "Torta"
        self.Outro()
        self.opção5.config(state=DISABLED)
    def Pdq(self):
        self.produto = 'Pao de Queijo'
        self.Outro()
        self.opção6.config(state=DISABLED)
    def Pastel(self):
        self.produto = "Pastel"
        self.Outro()
        self.opção7.config(state=DISABLED)

    def quantidade(self):
        self.qtns = self.qtn.get()
        self.feito = (f'{self.qtns}x {self.produto}')
        self.lista.append (self.feito)
        self.itens.insert(END,self.feito)
        self.qtn.delete(0,END)
        print(self.lista)

    def botoes(self):       
        # frame para botoes
        self.cardapio = Frame(self.garcom)
        self.cardapio.place(x=20,y=120)

        self.digitas = Frame(self.garcom,bg='#38312D',bd=0,)
        self.digitas.place(x=860,y=425)
        # Botoes do cardapio
        self.opção1 = Button(self.cardapio, image=self.expresso, command=self.Expresso,bg='#38312D',bd=0,activebackground='#38312D')
        self.opção1.pack(side='top')

        self.opção2 = Button(self.cardapio, image=self.cappuccino, command=self.Cappuccino,bg='#38312D',bd=0,activebackground='#38312D')
        self.opção2.pack(side='top')

        self.opção3 = Button(self.cardapio, image=self.latte, command=self.Latte,bg='#38312D',bd=0,activebackground='#38312D')
        self.opção3.pack(side='top')

        self.opção4 = Button(self.cardapio, image=self.mocca, command=self.Mocca,bg='#38312D',bd=0,activebackground='#38312D')
        self.opção4.pack(side='top')

        self.opção5 = Button(self.cardapio, image=self.torta, command=self.Torta,bg='#38312D',bd=0,activebackground='#38312D')
        self.opção5.pack(side='top')

        self.opção6 = Button(self.cardapio, image=self.pdq, command=self.Pdq,bg='#38312D',bd=0,activebackground='#38312D')
        self.opção6.pack(side='top')

        self.opção7 = Button(self.cardapio, image=self.pastel, command=self.Pastel,bg='#38312D',bd=0,activebackground='#38312D')
        self.opção7.pack(side='top')

        #Botoes de quantidade 
        self.qtnt = Label(self.digitas, text="Quantidade:",font=('Inknut Antiqua',15, 'bold'),fg="white",bg='#38312D')
        self.qtnt.pack(side='top')

        self.qtn = Entry(self.digitas, font=100, width=10)
        self.qtn.pack(side='left')

        self.add = Button(self.digitas,image=self.confirmar,command=self.quantidade,bg='#38312D',bd=0,)
        self.add.pack(side='left')
        #Botoes para delete 
        self.returne = Button(self.garcom,image=self.voltf5,bg='#38312D',bd=0,command=self.botaoReturne)
        self.returne.place(x=1100,y=490)
        self.delete = customtkinter.CTkButton(
            self.garcom,
            text="X",
            text_color="red",
            font=("Arial", 40, "bold"),
            fg_color="#D9D9D9",
            corner_radius=15,
            width=57,
            height=57,
            command=self.botaoX
        )
        self.delete.place(x=1025, y=485)
        # self.delete.place(x=950,y=425)

        #Lista do q estas a adicionar
        self.itens = Listbox(self.garcom,bg='#38312D',fg="#D9D9D9",font=("Inknut Antiqua", 12), width=30, height=6)
        self.itens.place(x=875, y=75)

        #seta
        self.seta = Button(self.garcom, image=self.st,command=self.incompleto,bg='#38312D',bd=0,)
        self.seta.place(x=0,y=5)

        #Concluir
        self.Concluido = Button(self.garcom,image=self.concluido,command=self.incompleto,bg='#38312D',bd=0,)
        self.Concluido.place(x=900,y=575)

    def botaoReturne(self):
        self.Selecionar=self.itens.size()
        if self.Selecionar  >0:
            self.itens.delete(self.Selecionar-1)
            self.lista.pop()
        else:
            print("deu erro irmão")

    def botaoX(self):
        if self.lista:
            self.itens.delete(0,END)
            self.lista.clear()
        else:
            print("X")


    def mostrar_info(self,data):
        info = Toplevel()
        info.title("Informações do dia")
        info.geometry("800x600")
        info.configure(bg="#38312D")

        titulo = Label(info, text="Detalhes do dia " + data, font=("Inknut Antiqua", 20, "bold"), fg="white", bg="#38312D")
        titulo.pack(pady=30)
        self.cur.execute('SELECT pedido FROM ordem WHERE hora like %s', (f"%{data}%",))
        inter=self.cur.fetchall()
        self.pedbon=[]
        for item in inter:
            self.pedbon.append(item[0])
        pedidobonito="\n".join(self.pedbon)


        texto = Label(info, text=pedidobonito, font=("Inknut Antiqua", 14), fg="#D9D9D9", bg="#38312D")
        texto.pack()

        fechar = customtkinter.CTkButton(
            info, 
            text="Fechar", 
            font=("Inknut Antiqua", 20),
            fg_color="#D9D9D9", 
            text_color="#38312D", 
            width=100, 
            height=40, 
            command=info.destroy,
            corner_radius=30,
            )
        fechar.pack(pady=20)

    def f5(self):
        self.atend.withdraw()
        self.janelabarista.withdraw()
        self.garcom.withdraw()
        self.janela.deiconify()

    def confirmbar(self):
        
        self.confmesa=self.qualmesa.get() 
        self.cur.execute('SELECT pedidocompl FROM barista WHERE pedidocompl LIKE %s',(f"{self.confmesa}%"))
        pedmesa=self.cur.fetchall()
        self.pedmesabonito=", ".join(str(p[0]) for p in pedmesa)
        self.cur.execute('INSERT INTO ordem (pedido) VALUES (%s)',(self.pedmesabonito) )
        self.cur.execute('DELETE FROM barista where pedidocompl LIKE %s', (f"{self.confmesa}%",))

        self.pedido=[]
        self.janelabarista.destroy()
        self.telabarista()

    def voltar(self):
        try:
            self.janelabarista.withdraw()
        except:
            pass
        try:
            self.garcom.withdraw()
        except:
            pass
        try:
            self.atend.withdraw()
        except:
            pass
        self.janela.deiconify()



    ## OUTRAS TELAS
    def telagarcom(self):
        self.garcom = Toplevel(self.janela)
        if self.janela.attributes("-fullscreen"):
            self.garcom.attributes("-fullscreen", True)
        self.garcom.bind("<F11>", self.telacheia)
        self.garcom.bind("<Escape>", self.window)
        self.garcom.geometry('1280x720')
        self.garcom.title("Garçom")

        self.garcom.config(background='#38312D')


        self.botoes()


        self.back=Button(self.garcom, image=self.st, command=self.voltar, bg="#38312D", borderwidth=0)
        self.back.place(x=0, y=0)

        self.nmenu = Label(self.garcom,text="GARÇOM",font=('Inknut Antiqua', 40, 'bold'),fg="#D9D9D9",bg='#38312D',)
        self.nmenu.place(x=50,y=-35)
        self.Itens = Label(self.garcom, text="Itens selecionados", font=('Inknut Antiqua', 12, 'bold'),fg="#D9D9D9",bg='#38312D',)
        self.Itens.place(x=875, y=40)
        linha1= Frame(self.garcom, bg="#D9D9D9", height=1, width=360)        
        linha1.place(x=15,y=100)
        linha2= Frame(self.garcom, bg="#D9D9D9", height=650, width=1)        
        linha2.place(x=850,y=50)

        self.janela.withdraw()



    def telabarista(self):
### MUDOU O JEITO DE CONIRMAR PEDIDO, criar uma entry que recebe o valor da mesa e ao confirmar apaga os dados do pedido daquela mesa e 
## recarrega a pagina


        # self.janelabarista.withdraw
        self.janelabarista = Toplevel(self.janela)
        if self.janela.attributes("-fullscreen"):
            self.janelabarista.attributes("-fullscreen", True)
        self.janelabarista.bind("<F11>", self.telacheia)
        self.janelabarista.bind("<Escape>", self.window)
        self.janela.withdraw()
        self.janelabarista.title("BARISTA")
        self.st=PhotoImage(file="img/seta.png")
        self.ref=PhotoImage(file="img/f5.png")

        self.janelabarista.configure(bg="#38312D")
        self.janelabarista.title("BARISTA")
        self.janelabarista.bind("<F11>", self.telacheia)
        self.janelabarista.bind("<Escape>", self.window)
        self.janelabarista.geometry("1280x720")
        ped=[]
        self.pedido=[]
        self.cur.execute('SELECT pedidocompl FROM barista')
        ped=self.cur.fetchall()
        for item in ped:
            self.pedido.append(item[0])
        self.mostpedido="\n".join(self.pedido)

        self.fbc=PhotoImage(file="img/botaoconfirmar.png")

        mostrarpedido=Label(self.janelabarista, text=self.mostpedido, font=("Inknut Antiqua Regular", 20), fg="#D9D9D9", bg="#38312D")
        mostrarpedido.grid(row=4, column=0,padx=4,pady=3)

        textoconf=Label(self.janelabarista, text="QUAL MESA DESEJA CONFIRMAR", font=("Inknut Antiqua", 23), fg="#D9D9D9", bg="#38312D")
        textoconf.grid(row=4, column=5, padx=3)

        self.qualmesa=Entry(self.janelabarista, font=30, width=5)
        self.qualmesa.grid(row=5, column=5, pady=2,padx=4)   

        confirmarpedido=Button(self.janelabarista, image=self.fbc, borderwidth=0, cursor="hand2", command=self.confirmbar, bg="#38312D")
        confirmarpedido.grid(row=6, column=5, padx=3, pady=3)


        seta=Button(self.janelabarista, image=self.st,borderwidth=0,bg="#38312D", command=self.voltar)
        seta.grid(row=0, column=0, pady=2, padx=2, sticky="w")

        jan=Label(self.janelabarista, text="BARISTA", font=("Inknut Antiqua Regular", 24), fg="#D9D9D9", bg="#38312D")
        jan.grid(row=1, column=0, pady=3)

        linhab= Frame(self.janelabarista, bg="#D9D9D9", height=1, width=500)        
        linhab.grid(row=3, column=0, pady=3)


    def telaatend(self):
        self.atend=Toplevel(self.janela)
        if self.janela.attributes("-fullscreen"):
            self.atend.attributes("-fullscreen", True)
        self.atend.bind("<F11>", self.telacheia)
        self.atend.bind("<Escape>", self.window)
        self.janela.withdraw()
        self.atend.title("Atendimentos")
        self.atend.geometry("1280x720")
        self.atend.configure(bg="#38312D")

        titulo = Label(self.atend, text="ATENDIMENTOS", font=("Inknut Antiqua", 24, "bold"), fg="white", bg="#38312D")
        titulo.pack(pady=(50, 10))

        linha = Frame(self.atend, bg="#D9D9D9", height=2)
        linha.pack(fill=X, padx=100, pady=(0, 30))

        seta=Button(self.atend, image=self.st,borderwidth=0,bg="#38312D", command=self.voltar)
        seta.place(x=1,y=1)

        frame_datas = Frame(self.atend, bg="#38312D")
        frame_datas.pack()

        adddatas=Label(
            self.atend,
            text="Insira a nova data:",
            font=("Inknut Antiqua", 20),
            fg="#D9D9D9",
            bg="#38312D",
                       )
        adddatas.place(x=990, y=440)
        self.dtnova=Entry(
            self.atend,
            width=20,
        )
        self.dtnova.place(x=1070, y=500)
        self.fbc=PhotoImage(file="img/botaoconfirmar.png")
        confdtnova=Button(
            self.atend,
            image=self.fbc,
            bg="#38312D",
            borderwidth=0,
            command=self.confirmardata,
        )
        confdtnova.place(x=1100, y=530)


        for i, data in enumerate(self.datas):
            botao = customtkinter.CTkButton(
                                            frame_datas, 
                                            text=data, 
                                            font=("Arial", 20, "bold"), 
                                            fg_color="#D9D9D9", 
                                            text_color="#38312D",
                                            width=100, 
                                            height=50, 
                                            command=lambda d=data: self.mostrar_info(d), 
                                            corner_radius=30
                                            )
            botao.grid(row=i//3, column=i%3, padx=10, pady=10)



    ##TELA INCIAL
    def telainicial(self):
        self.janela.configure(bg="#38312D")
        self.janela.title("STEAMCOFFEE")
        self.janela.bind("<F11>", self.telacheia)
        self.janela.bind("<Escape>", self.window)
        self.icon = PhotoImage(file='img/engrenagem.png')
        self.janela.iconphoto(True, self.icon)
        self.janela.geometry("1280x720")
        # self.janela.resizable(False,False)

        ## TEXTOS
        logo = Label (self.janela, text= "STEAMCOFFEE", font=("Inknut Antiqua Regular", 54), fg="#D9D9D9", bg="#38312D")        
        logo.pack(anchor=CENTER)

        linha= Frame(self.janela, bg="#D9D9D9", height=1, width=500)        
        linha.pack(pady=3)

        subtitulo=Label(self.janela, text="A sua cafeteria dos sonhos!", font=("Inknut Antiqua Regular", 20), fg="#D9D9D9",bg="#38312D")
        subtitulo.pack(pady=3)

        ##FUNDO BOTAO
        self.fbg=PhotoImage(file="img/botaogarcom.png")
        self.fbb=PhotoImage(file="img/botaobarista.png")
        self.fbn=PhotoImage(file="img/botaoatendimentos.png")
        self.st=PhotoImage(file="img/seta.png")

        # BOTOES
        gar=Button(self.janela, image=self.fbg, bg="#38312D",borderwidth=0,cursor="hand2", command=self.telagarcom)
        gar.pack(pady=5)

        bar=Button(self.janela, image=self.fbb, bg="#38312D",borderwidth=0,cursor="hand2", command=self.telabarista)
        bar.pack(pady=5)

        nota=Button(self.janela, image=self.fbn,bg="#38312D",borderwidth=0,cursor="hand2", command=self.telaatend)
        nota.pack(pady=5)

    def ativar(self):
        self.janela.mainloop()

if __name__ == "__main__":
    apli=front()
    apli.mysqlconnect()
    apli.telainicial()
    apli.ativar()   
     