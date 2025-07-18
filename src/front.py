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

    def telainicial(self):
        self.janela.title("STEAMCOFFEE")

        self.janela.bind("<F11>", self.telacheia)
        self.janela.bind("<Escape>", self.window)
        self.janela.geometry("1280x720")
        self.janela.resizable(False,False)

        label = Label (self.janela, text= "STEAMCOFFEE", font=("Arial Bold", 25), bg="black", fg="white")

        label.grid(row=0, column=0, padx=0, pady=0)

        botao = Button (self.janela, text="Barista")
        botao.grid(row=5, column=0, padx=0, pady=2)

    def ativar(self):
        self.janela.mainloop()

if __name__ == "__main__":
    apli=front()
    # apli.telacheia()
    # apli.window()
    apli.telainicial()
    apli.ativar()