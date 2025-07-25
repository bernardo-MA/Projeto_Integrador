from tkinter import *

class telagarcom:
    def __init__(self):
        self.lista= ["cafe latte"]
        self.produto=''
    def Janela(self):
        # Configurações da janela
        self.garcom = Tk()
        self.garcom.geometry('1280x720')
        self.garcom.title("Garçom")
        self.icon = PhotoImage(file='logo.png')
        self.garcom.iconphoto(True, self.icon)
        self.garcom.config(background='#38312D')

        #imagens
        self.st = PhotoImage(file='seta.png')
        self.expresso = PhotoImage(file='expresso.png')
        self.cappuccino = PhotoImage(file='cappuccino.png')
        self.latte = PhotoImage(file='latte.png')
        self.mocca = PhotoImage(file='mocca.png')
        self.pdq = PhotoImage(file='paodequeijo.png')
        self.torta = PhotoImage(file='torta.png')
        self.pastel = PhotoImage(file='pastel.png')

        #Escrita garçom
        self.nmenu = Label(self.garcom,text="GARÇOM",font=('Arial', 45, 'bold'),fg="white",bg='#38312D',)
        self.nmenu.place(x=15,y=50)
        self.seta = Button(self.garcom, image=self.st,command=self.incompleto,bg='#38312D',bd=0, )
        self.seta.place(x=0,y=5)

    def botoes(self):
        #frame para botoes
        self.cardapio = Frame(self.garcom)
        self.cardapio.place(x=20,y=150)

        # Butoes do cardapio
        self.opção1 = Button(self.cardapio, image=self.expresso, command=self.Expresso,bg='#38312D',bd=0)
        self.opção1.pack(side='top')

        self.opção2 = Button(self.cardapio, image=self.cappuccino, command=self.Cappuccino,bg='#38312D',bd=0)
        self.opção2.pack(side='top')

        self.opção3 = Button(self.cardapio, image=self.latte, command=self.Latte,bg='#38312D',bd=0)
        self.opção3.pack(side='top')

        self.opção4 = Button(self.cardapio, image=self.mocca, command=self.Mocca,bg='#38312D',bd=0)
        self.opção4.pack(side='top')

        self.opção5 = Button(self.cardapio, image=self.torta, command=self.Torta,bg='#38312D',bd=0)
        self.opção5.pack(side='top')

        self.opção6 = Button(self.cardapio, image=self.pdq, command=self.Pdq,bg='#38312D',bd=0)
        self.opção6.pack(side='top')

        self.opção7 = Button(self.cardapio, image=self.pastel, command=self.Pastel,bg='#38312D',bd=0)
        self.opção7.pack(side='top')

        self.qtnt = Label(self.garcom, text="Quantidade:",font=('Arial',15, 'bold'),fg="white",bg='#38312D')
        self.qtnt.place(x=280,y=680)

        self.qtn = Entry(self.garcom, font=45)
        self.qtn.place(x=425,y=681)

        self.add = Button(self.garcom, text="Add",relief=RAISED,bd=2,command=self.quantidade)
        self.add.place(x=620,y=680)

    def incompleto(self):
        print("ainda n funcional")
    #Funções para Botoes
    def Expresso(self):
        self.lista.append("Cafe expresso")
        print(self.lista)
        self.opção1.config(bg='green')
        self.opção1.config(state=DISABLED)
    def Cappuccino(self):
        self.produto = "Cappuccino"
    def Latte(self):
        self.produto = "Latte"
    def Mocca(self):
        self.produto = 'Mocca'
    def Torta(self):
        self.produto = "Torta"
        print(self.lista)
        self.opção2.config(bg='green')
        self.opção2.config(state=DISABLED)
    def Pdq(self):
        self.produto = 'Pao de Queijo'
    def Pastel(self):
        self.produto = "Pastel"

    def quantidade(self):
        self.qtns = Entry.get()
        self.lista.append (f'{self.qtns}x {self.produto}')
    def show(self):
        self.garcom.mainloop()


if __name__ =="__main__":
    app=telagarcom()
    # app.Imagens()
    app.Janela()
    app.botoes()
    app.show()