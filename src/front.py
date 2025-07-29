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
        self.janelagarcom.withdraw()
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
            self.janelagarcom.withdraw()
        except:
            pass
        try:
            self.atend.withdraw()
        except:
            pass
        self.janela.deiconify()


        
    ## OUTRAS TELAS
    def telagarcom(self):
        self.janelagarcom = Toplevel()
        self.janela.withdraw()



    def telabarista(self):
### MUDOU O JEITO DE CONIRMAR PEDIDO, criar uma entry que recebe o valor da mesa e ao confirmar apaga os dados do pedido daquela mesa e 
## recarrega a pagina


        # self.janelabarista.withdraw
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
        self.janela.withdraw()
        self.atend.title("Atendimentos")
        self.atend.geometry("1280x720")
        self.atend.configure(bg="#38312D")

        titulo = Label(self.atend, text="ATENDIMENTOS", font=("Inknut Antiqua", 24, "bold"), fg="white", bg="#38312D")
        titulo.pack(pady=(50, 10))

        linha = Frame(self.atend, bg="#D9D9D9", height=2)
        linha.pack(fill=X, padx=100, pady=(0, 30))

        seta=Button(self.atend, image=self.st,borderwidth=0,bg="#38312D", command=self.voltar)
        seta.pack()

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
     