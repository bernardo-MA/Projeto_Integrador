from tkinter import *

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
        print("Tela Barista")
    




    def telainicial(self):
        self.janela.title("STEAMCOFFEE")

        self.janela.bind("<F11>", self.telacheia)
        self.janela.bind("<Escape>", self.window)
        self.janela.geometry("1280x720")
        self.janela.resizable(False,False)

        label = Label (self.janela, text= "STEAMCOFFEE", font=("Arial Bold", 25),)        
        texto1= Label (self.janela, text ="Selecione qual area deseja acessar", font=("Arial Bold", 20))
        # label.grid( padx=2, pady=1)
        label.grid(row=0, column=0, padx=2, pady=1, sticky="w")
        texto1.grid(row=5, column=0)

        botao = Button (self.janela, text="Barista")
        botao.grid(row=7, column=0, padx=0, pady=2)

    def ativar(self):
        self.janela.mainloop()

if __name__ == "__main__":
    apli=front()
    apli.telainicial()
    apli.ativar()