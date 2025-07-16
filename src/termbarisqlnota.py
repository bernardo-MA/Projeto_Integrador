import os
import time
import pymysql
from pymysql import Error
from conexaob import conecta

class Termbarista:

    def __init__(self):
        self.op = ["Expresso","Cappuccino", "Latte", "Moca", "Torta Chocolate", "Torta Morango", "Pão de Queijo", "Pastel"]
        self.bebidas=[]
        self.pedido = []
        self.ped=[]
        self.completo=[]
        self.mesa= None
        self.cur= None
        self.conn= None
        self.notinhas = [] 


    def mysqlconnect(self):
        # To connect MySQL database
        try:
            self.conn = pymysql.connect(
                host='127.0.0.1',
                user='root', 
                password = "",
                db='cafeteria',
                )
            
            self.cur = self.conn.cursor()
            
            # Select query
            # self.cur.execute("select * from ordem")
            # output = self.cur.fetchall()
            
            # for a,b,c in output:
            #     print(f"ID:{a}")
            #     print(f"Pedido:{b}")
            #     print(f"Data:{c}")
            #     print("--------------------------")
            
            # To close the connection
            self.conn.close()
        except pymysql.MySQLError as e:
            print(f"Deu erro porra {e}")
        

    def cardapio(self):
        os.system("CLS")
        self.mesa =str(input("\nQual mesa fez o pedido? "))


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
                self.conn.ping(reconnect=True)
                self.ped.append((self.mesa, list(self.pedido)))
                try:
                    sql=("insert into notinhas (pedido) VALUES (%s)")
                    valor = (f'{self.mesa} - {", ".join(self.pedido)}')
                    valores = (valor,)
                    self.cur.execute(sql, valores)
                    self.conn.commit()
                except  Exception as e:
                    print("Erro ", e)
                self.pedido.clear()
                self.notinhas = valor
                break
                
        
    def barista(self):
        print("-------------PEDIDOS PARA BARISTA-------------")
        for mesa, pedido in self.ped:
            itens_formatados = ", ".join(pedido)
            print(f"{mesa} | {itens_formatados}")
            print("----------------------------------------------") 
            

 
    def mostrar_notinhas(self):
            while True:
                os.system("CLS" if os.name == "nt" else "clear")
                print("-------------NOTINHAS-------------")
                print("1 - Ver todas as notinhas")
                print("2 - Limpar notinhas")
                print("3 - Voltar")
                op = input("Escolha uma opção: ")

                if op == "1":
                    os.system("CLS" if os.name == "nt" else "clear")
                    print("-------- HISTÓRICO DE NOTINHAS --------")
                    self.conn.ping(reconnect=True)
                    self.cur.execute('select * from notinhas')
                    output = self.cur.fetchall()
                    for a,b,c in output:
                        print(f"ID:{a}")
                        print(f"Pedido:{b}")
                        print(f"Data:{c}")
                        print("--------------------------")
                    input("\nPressione Enter para voltar...")
                    # if not self.notinhas:
                    #     print("Nenhuma notinha salva.")
                    # else:
                    #     for nota in self.notinhas:
                    #         print(nota)
                    # input("\nPressione Enter para voltar...")

                elif op == "2":
                    self.notinhas.clear()
                    print("Notinhas apagadas com sucesso.")

                elif op == "3":
                    break

                else:
                    print("Opção inválida.")



if __name__ =="__main__":
    app=Termbarista()
    app.mysqlconnect()

    while True:
        print("----------------------------------")
        print("| 1 - Ver pedidos ja adicionados |")
        print("| 2 - Adicionar novo pedido      |")
        print("| 3 - Ver Notas                  |")
        print("----------------------------------")
        se=input("")


        if se == "1":
            app.barista()
        elif se=="2":
            app.cardapio()
        elif se=="3":
            app.mostrar_notinhas()