from tkinter import *

window = Tk()
window.geometry("720x720")
window.title("AMOGUS")
icon = PhotoImage(file='logo.png')
window.iconphoto(True, icon)
window.config(background="#38312D")
photo = PhotoImage(file='logo.png')

label = Label(window,
               text="Hello World!",
               font=('Arial', 40, 'bold'),
               fg='#D9D9D9', #cor da letra
               bg='#38312D', #cor do fundo da letra
               relief=RAISED, #adiciona borda
               bd=10, # aumenta tamanho da borda
               padx=20,
               pady=20,
            #    image=photo, #adiciona foto
            #    compound='bottom' #seleciona aonde deve aparecer
               )
label.pack()
# label.place(x=0,y=0)
def click():
    print("Parabens")

button = Button(window,
                text="Clica aq",
                fg='#D9D9D9',
                bg='#38312D',
                activeforeground='#38312D', #altera o efeito de cor quando clicado
                activebackground='#38312D',
                image=photo,
                compound='top',
                #state=DISABLED #faz o botao ficar inativo
                command=click
                )
button.pack()

def submit():
    nome = entry.get()
    print("Olá " +nome)

entry = Entry(window)
# entry.config(show="*") #mostraria * como em uma senha
entry.pack(side=LEFT)

submit = Button(window,
                text="Enviar ",
                command=submit,
                )
submit.pack(side=RIGHT)


window.mainloop() #coloca a tela