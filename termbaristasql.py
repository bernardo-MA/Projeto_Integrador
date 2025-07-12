import os
import time
import pymysql
from pymysql import Error
from Conexao import Conexao

conexao=Conexao('cafeteria', '127.0.0.1')
if not conexao.Iniciar():
    print("Não foi possível conectar!")
    quit

class Termbarista:
    from Conexao import Conexao

    conexao=Conexao('cafeteria', '127.0.0.1')
    if not conexao.Iniciar():
        print("Não foi possível conectar!")
        quit




    def __init__(self):
        self.op = ["Expresso","Cappuccino", "Latte", "Moca", "Torta Chocolate", "Torta Morango", "Pão de Queijo", "Pastel"]
        self.bebidas=[]
        self.pedido = []
        self.ped=[]
        self.completo=[]
        self.mesa= None
        self.garcom=("INSERT INTO ordem (mesa, pedido) VALUES (%s, %s)")


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
            print("--------------------")


            print("\nDeseja:")
            print("1 - Adicionar ao pedido")
            print("2 - Finalizar")
            t = int(input(""))
            os.system("CLS")

            if t==2:
                self.ped.append((self.mesa, list(self.pedido)))
                val=self.ped
                conexao.Executar(f"INSERT INTO ordem (mesa, pedido) VALUES ({val})")
                self.pedido.clear()
                break
        




    def barista(self):
        print("-------------PEDIDOS PARA BARISTA-------------")
        for mesa, pedido in self.ped:
            print(f"{mesa} | {pedido}")  


if __name__ =="__main__":
    app=Termbarista()


    while True:
        print("1- Barista")
        print("2- Garçom")
        se=input("Deseja ver a tabela do barista? ou realizar outro pedido? ")


        if se == "1":
            app.barista()
        elif se=="2":
            app.cardapio()
    