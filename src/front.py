from tkinter import *
janela = Tk()
janela.title("STEAMCOFFEE")

escfull=False

def telacheia(event=None):
    global escfull
    escfull = not escfull
    janela.attributes("-fullscreen", escfull)
    
def window(event=None):
    global escfull
    escfull = False
    janela.attributes("-fullscreen", False)

janela.bind("<F11>", telacheia)

janela.bind("<Escape>", window)

janela.geometry("1080x720")

janela.mainloop()
