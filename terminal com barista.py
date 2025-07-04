import os
import time
bebidas=[]
pedido = []
ped=[]
completo=[]
esc = 0


def cardapio(op,esc,pedido):
    op = ["Expresso","Cappuccino", "Latte", "Moca", "Torta Chocolate", "Torta Morango", "Pão de Queijo", "Pastel"]
    t = 1
    # mesa=input("Qual mesa fez o pedido?")
    os.system("CLS")
    while t < 2:
        x = 1
        for item in op:
            print(x,"-", item)
            x = x+1
        esc = int(input("Qual deseja? "))
        pedido += [op[esc-1]]
        print(pedido[-1], "adicionado")
        print("--------------------")
        print("Pedido atual:")
        for item in pedido:
            print(item)
        print("--------------------")
        print("Deseja:")
        print("1 - Adicionar ao pedido")
        print("2 - Finalizar")
        t = int(input(""))
        os.system("CLS")
    ped.append(pedido)


mesa=input("Qual mesa fez o pedido?")
cardapio(bebidas,esc,pedido)
# ped.append(pedido)



def barista():
    q=len(ped)
    # for i in ped:
    for i in range(0,q):
        print(mesa,"-", ped[i],"\n")


while 0!=1:
    print("1- Barista")
    print("2- Garçom")
    se=input("Deseja ver a tabela do barista? ou realizar outro pedido?")
    if se == "1":
        barista()

        # for coisa in completo:
        #     print(mesa,"-", coisa)
    elif se=="2":
        mesa=input("Qual mesa fez o pedido?")
        cardapio(bebidas,esc,pedido)
        # ped.append(pedido)
        