from tkinter import *

from PIL import Image, ImageTk

class front:
    def __init__(self):
        self.janela = Tk()
        self.escfull=None
        self.escfull=False

    def telacheia(self, event):
        self.escfull = not self.escfull
        self.janela.attributes("-fullscreen", self.escfull)
        

    def window(self, event):
        self.escfull = False
        self.janela.attributes("-fullscreen", False)
     

    def telabarista(self):
        self.janelabarista = Tk()
        self.janela.destroy()
        self.janelabarista.mainloop()
    
    def telagarcom(self):
        self.janelagarcom= Tk()
        self.janela.destroy()
        self.janelagarcom.mainloop()
        print("Tela garçom")

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
        self.fb=PhotoImage(file="botaogarcom.png")

        # BOTOES
        gar=Button(self.janela, image=self.fb, text="GARÇOM", bg="#38312D")
        gar.pack(pady=3)

    def ativar(self):
        self.janela.mainloop()

if __name__ == "__main__":
    apli=front()
    apli.telainicial()
    apli.ativar()
     