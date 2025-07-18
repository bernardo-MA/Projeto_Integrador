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

label = Label (janela, text= "Hello World!", font=("Arial Bold", 25), bg="black", fg="white")

label.grid(row=0, column=0, padx=440, pady=320)


janela.mainloop()
