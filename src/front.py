from tkinter import *
from conexaob import conecta
import pymysql
from pymysql import Error
from PIL import Image, ImageTk


class front:
    def __init__(self):
        self.janela = Tk()
        self.escfull=None
        self.escfull=False
        self.cur=None
        self.pedido=[]

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
    def f5(self):
        self.janelabarista.withdraw
        self.janelabarista.deiconify()

    def pedidobarista(self):
        print("pedido")


    def voltar(self):
        self.janela.deiconify()
        self.janelabarista.withdraw()
        self.janelagarcom.withdraw()
        self.janelanotas.withdraw()
        
    ## OUTRAS TELAS
    def telagarcom(self):
        self.janelagarcom = Toplevel()
        self.janela.withdraw()



    def telabarista(self):
        self.janelabarista = Toplevel(self.janela)
        self.janela.withdraw()
        self.janelabarista.title("BARISTA")
        self.st=PhotoImage(file="img/seta.png")
        self.ref=PhotoImage(file="img/f5.png")

        self.janelabarista.configure(bg="#38312D")
        self.janelabarista.title("BARISTA")
        self.janelabarista.bind("<F11>", self.telacheia)
        self.janelabarista.bind("<Escape>", self.window)
        self.janelabarista.geometry("1280x720")

        self.cur.execute('SELECT pedidocompl FROM barista')
        ped=self.cur.fetchall()
        for item in ped:
            self.pedido.append(item)

        mostrarpedido=Label(self.janelabarista, text=self.pedido, font=("Inknut Antiqua Regular", 20), fg="#D9D9D9", bg="#38312D")
        mostrarpedido.grid(row=4, column=0,padx=4,pady=3)


        f5bar=Button(self.janelabarista, image=self.ref, borderwidth=0, bg="#38312D", command=self.f5)
        f5bar.grid(row=0, column=1, pady=2,padx=2, sticky="w")

        seta=Button(self.janelabarista, image=self.st,borderwidth=0,bg="#38312D", command=self.voltar)
        seta.grid(row=0, column=0, pady=2, padx=2, sticky="w")

        jan=Label(self.janelabarista, text="BARISTA", font=("Inknut Antiqua Regular", 24), fg="#D9D9D9", bg="#38312D")
        jan.grid(row=1, column=0, pady=3)

        linhab= Frame(self.janelabarista, bg="#D9D9D9", height=1, width=500)        
        linhab.grid(row=3, column=0, pady=3)
        


    def telaatend(self):
        self.janelanotas=Toplevel()
        self.janela.withdraw()
        

    ##TELA INCIAL
    def telainicial(self):
        self.janela.configure(bg="#38312D")
        self.janela.title("STEAMCOFFEE")
        self.janela.bind("<F11>", self.telacheia)
        self.janela.bind("<Escape>", self.window)
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
     