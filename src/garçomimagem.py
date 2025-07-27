from tkinter import *
from PIL import Image, ImageTk
lista = ["cafe latte"]

# Configurações da janela
garcom = Tk()
garcom.geometry('1280x720')
garcom.title("Garçom")
icon = PhotoImage(file='img/logo.png')
garcom.iconphoto(True, icon)
garcom.config(background='#38312D')

#Escrita garçom
nmenu = Label(garcom,text="GARÇOM",font=('Arial', 45, 'bold'),fg="white",bg='#38312D',)
nmenu.place(x=0,y=0)

#Funções para Botoes
def Expresso():
    lista.append("Cafe expresso")
    print(lista)
    opção1.config(bg='green')
    opção1.config(state=DISABLED)
def Mcake():
    lista.append("Torta de Morango")
    print(lista)
    opção2.config(bg='green')
    opção2.config(state=DISABLED)
def quantidade():
    qtns = Entry.get()
    

#Imagens
imagem = Image.open("img/cafe.png") 
resizedimage = imagem.resize((200,200))
cafe = ImageTk.PhotoImage(resizedimage)

imagem2 = Image.open('img/Tortamorango.png')
resizedimage2 = imagem2.resize((200,200))
tortamorango = ImageTk.PhotoImage(resizedimage2)

# Butoes do cardapio
opção1 = Button(garcom, image=cafe, command=Expresso)
opção1.place(x=50, y=100)

opção2 = Button(garcom, image=tortamorango, command=Mcake)
opção2.place(x=300,y=100)

qtnt = Label(garcom, text="Quantidade:",font=('Arial',15, 'bold'),fg="white",bg='#38312D')
qtnt.place(x=280,y=680)

qtn = Entry(garcom, font=45)
qtn.place(x=425,y=681)

add = Button(garcom, text="Add",relief=RAISED,bd=2,command=quantidade)
add.place(x=620,y=680)

# itens = Listbox(garcom)
# Listbox.insert(1,image=cafe)
# Listbox.place(x=100,y=100)
garcom.mainloop()