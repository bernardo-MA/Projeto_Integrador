from tkinter import *
from PIL import Image, ImageTk

class telagarcom:
    def __init__(self):
        self.lista= []
        self.produto=''
    def Janela(self):
        # Configurações da janela
        self.garcom = Tk()
        self.garcom.geometry('1280x720')
        self.garcom.title("Garçom")
        self.icon = PhotoImage(file='img/logo.png')
        self.garcom.iconphoto(True, self.icon)
        self.garcom.config(background='#38312D')

        #imagens
        self.st = PhotoImage(file='img/seta.png')
        self.expresso = PhotoImage(file='img/expresso.png')
        self.cappuccino = PhotoImage(file='img/cappuccino.png')
        self.latte = PhotoImage(file='img/latte.png')
        self.mocca = PhotoImage(file='img/mocca.png')
        self.pdq = PhotoImage(file='img/paodequeijo.png')
        self.torta = PhotoImage(file='img/torta.png')
        self.pastel = PhotoImage(file='img/pastel.png')
        self.concluido = PhotoImage(file='img/botaoconcluido.png')
        self.confirmar_o = Image.open("img/botaoconfirmar.png")
        self.confirmar_n = self.confirmar_o.resize((65,65))
        self.confirmar = ImageTk.PhotoImage(self.confirmar_n)
        self.retorno_o = Image.open("img/Retorno.png")
        self.retorno_n = self.retorno_o.resize((125,125))
        self.retorno = ImageTk.PhotoImage(self.retorno_n)
        self.lixeira_o = Image.open("img/lixeira.png")
        self.lixeira_n = self.lixeira_o.resize((65,65))
        self.lixeira = ImageTk.PhotoImage(self.lixeira_n)

        #Escritas
        self.nmenu = Label(self.garcom,text="GARÇOM",font=('Inknut Antiqua', 40, 'bold'),fg="#D9D9D9",bg='#38312D',)
        self.nmenu.place(x=50,y=-35)
        self.Itens = Label(self.garcom, text="Itens selecionados", font=('Inknut Antiqua', 12, 'bold'),fg="#D9D9D9",bg='#38312D',)
        self.Itens.place(x=875, y=35)
        linha1= Frame(self.garcom, bg="#D9D9D9", height=1, width=360)        
        linha1.place(x=15,y=100)
        linha2= Frame(self.garcom, bg="#D9D9D9", height=650, width=1)        
        linha2.place(x=850,y=50)
        

    def botoes(self):
        #frame para botoes
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

        self.qtn = Entry(self.digitas, font=100, width=30)
        self.qtn.pack(side='left')

        self.add = Button(self.digitas,image=self.confirmar,command=self.quantidade,bg='#38312D',bd=0,)
        self.add.pack(side='left')
        #Botoes para delete 
        self.returne = Button(self.garcom,image=self.retorno,bg='#38312D',bd=0,)
        self.returne.place(x=900,y=425)
        self.delete = Button(self.digitas,image=self.lixeira,bg='#38312D',bd=0,)
        self.delete.pack(side='left')
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


    def incompleto(self):
        print("ainda n funcional")
    #Funções para Botoes
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
    def show(self):
        self.garcom.mainloop()


if __name__ =="__main__":
    app=telagarcom()
    app.Janela()
    app.botoes()
    app.show()