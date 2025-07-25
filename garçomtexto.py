from tkinter import *

#configurações da janela
garcom = Tk()
garcom.geometry('1280x720')
garcom.title("Garçom")
icon = PhotoImage(file='logo.png')
garcom.iconphoto(True, icon)
garcom.config(background='#38312D')

#Escrita garçom
nmenu = Label(garcom,text="GARÇOM",font=('Arial', 45, 'bold'),fg="white",bg='#38312D',)
nmenu.place(x=0,y=0)

cardapio = Listbox(garcom,
                   fg='white',
                   bg='#38312D',
                   font=60,
                   selectmode=SINGLE,
                   activestyle='none',
                   selectbackground='green',
                   bd= 0, relief='flat', highlightthickness=0
                   )
cardapio.insert(1, "Expresso")
cardapio.insert(2, "Cappuccino")
cardapio.insert(3, "Latte")
cardapio.insert(4, "Mocca")
cardapio.insert(5, "Torta")
cardapio.insert(6, "Pão de Queijo")
cardapio.insert(7, "Pastel")
cardapio.place(x=50,y=100)

# qtn = Entry

garcom.mainloop()
