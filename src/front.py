from tkinter import *

class front:
    def __init__(self):
        self.janela = Tk()
        self.escfull=None
        self.escfull=False
        self.janelabarista = Tk()

    def telacheia(self, event):
        self.escfull = not self.escfull
        self.janela.attributes("-fullscreen", self.escfull)

    def window(self, event):
        self.escfull = False
        self.janela.attributes("-fullscreen", False)

    def telabarista(self):
        self.janela.destroy()
        self.janelabarista.mainloop()
    
    def telagarcom(self):
        print("Tela garçom")

    def telainicial(self):
        self.janela.title("STEAMCOFFEE")

        self.janela.bind("<F11>", self.telacheia)
        self.janela.bind("<Escape>", self.window)
        self.janela.geometry("1280x720")
        self.janela.resizable(False,False)
        ## TEXTOS
        label = Label (self.janela, text= "STEAMCOFFEE", font=("Arial Bold", 25),)        
        texto1= Label (self.janela, text ="Selecione qual area deseja acessar", font=("Arial Bold", 20))
        label.grid(row=0, column=0, padx=0, pady=20, sticky="w")
        espaco= Label(self.janela, text="")
        espaco.grid(pady=20)
        texto1.grid(row=28, column=0, pady=10, sticky="w")
        ## BOTOES
        bar = Button (self.janela, text="Barista", command=self.telabarista)
        bar.grid(row=30, column=0, padx=5, pady=15, sticky="nsew")

        gar = Button (self.janela, text="Garçom")
        gar.pack
        gar.grid(row=35, column=0, padx=5, pady=15, sticky="nsew")

        notas=Button (self.janela, text="Notas")
        notas.grid(row=40, column=0, padx=5, pady=15, sticky="nsew")

    def ativar(self):
        self.janela.mainloop()

if __name__ == "__main__":
    apli=front()
    apli.telainicial()
    apli.ativar()