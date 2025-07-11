import os
import time

class Termbarista:
    def __init__(self):
        self.op = ["Expresso","Cappuccino", "Latte", "Moca", "Torta Chocolate", "Torta Morango", "Pão de Queijo", "Pastel"]
        self.bebidas=[]
        self.pedido = []
        self.ped=[]
        self.completo=[]
        self.mesa= None


    def cardapio(self):
        os.system("CLS")
        self.mesa =input("\nQual mesa fez o pedido? ")


        while True:
            print("-------------CARDAPIO-------------")
            for i, item in enumerate(self.op, 1):
                print(f"{i} -- {item}")


            esc = int(input("\nQual deseja? "))
            self.pedido.append(self.op[esc-1])
            print(self.pedido[-1], "adicionado")


            print("--------------------")
            print("\nPedido atual:")
            for item in self.pedido:
                print(item)
            print("\n--------------------")


            print("\nDeseja:")
            print("1 - Adicionar ao pedido")
            print("2 - Finalizar")
            t = int(input(""))
            os.system("CLS")

            if t==2:
                self.ped.append((self.mesa, list(self.pedido)))
                self.pedido.clear()
                break




    def barista(self):
        print("-------------PEDIDOS PARA BARISTA-------------")
        for mesa, pedido in self.ped:
            itens_formatados = ", ".join(pedido)
            print(f"{mesa} | {itens_formatados}")


if __name__ =="__main__":
    app=Termbarista()

    app.cardapio()

    while True:
        print("1- Finalizar e enviar ao barista")
        print("2- Adicionar pedido de outra mesa")
        se=input("")


        if se == "1":
            app.barista()
        elif se=="2":
            app.cardapio()
    