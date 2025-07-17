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
        try:
            self.conn = pymysql.connect(
                host='127.0.0.1',
                user='root', 
                password = "",
                db='cafeteria',
                )
            
            self.cur = self.conn.cursor()
            
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
                try:
                    sql=("insert into barista (pedido) VALUES (%s)")
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
        self.conn.ping(reconnect=True)
        print("-------------PEDIDOS PARA BARISTA-------------")
        self.cur.execute ('select pedido from barista')
        bar = self.cur.fetchall()
        for a in (bar):
            itens = "".join(a)
            print(itens)
 
    def mostrar_notinhas(self):
            self.conn.ping(reconnect=True)
            while True:
                os.system("CLS")
                print("-------------NOTINHAS-------------")
                print("1 - Ver todas as notinhas")
                print("2 - Procurar")
                print("3 - Voltar")
                op = input("Escolha uma opção: ")

                if op == "1":
                    os.system("CLS")
                    print("-------- HISTÓRICO DE NOTINHAS --------")
                    self.cur.execute('select * from notinhas')
                    output = self.cur.fetchall()
                    for a,b,c in output:
                        print(f"ID:{a}")
                        print(f"Pedido:{b}")
                        print(f"Data:{c}")
                        print("--------------------------")
                    input("\nPressione Enter para voltar...")

                elif op == "2":
                    print("por favor indique a data que deseja procurar(AAAA-MM-DD)")
                    ano = input("Ano: ")
                    mes = input("Mês: ")
                    dia = input("Dia: ")
                    self.cur.execute(f"select * from notinhas where hora like '{ano}-{mes}-{dia}%'")
                    info = self.cur.fetchall()
                    for a,b,c in info:
                        print(f"ID:{a}")
                        print(f"Pedido:{b}")
                        print(f"Data:{c}")
                        print("--------------------------") 
                    input("\nPressione Enter para voltar...")

                elif op == "3":
                    break
                else:
                    print("Opção inválida.")
    def concluir(self):
        self.conn.ping(reconnect=True)
        self.cur.execute('select id,pedido from barista')
        info = self.cur.fetchall()
        for a,b in info:
            print(f"id:{a} | {b}")
        print("-------------------------------")
        print("| 1 - Apagar pedido concluido |")
        print("| 2 - Apagar todos os pedidos |")
        print("-------------------------------")
        esc = int(input())
        if esc == 1:
            x = (input("Qual deseja apagar? "))
            self.cur.execute(f'delete from barista where id = {x}')
        elif esc == 2:
            print("Você tem certeza?")
            print("1 - Sim")
            print("2 - Não")
            sure = int(input(""))
            if sure == 1:
                self.cur.execute('truncate table barista') 
            else:
                print("Cancelando operação e voltando para o menu...")
                time.sleep(1)
                os.system("CLS")

    def menu(self):
        while True:
            print("----------------------------------")
            print("| 1 - Ver pedidos não concluidos |")
            print("| 2 - Adicionar novo pedido      |")
            print("| 3 - Concluir pedido            |")
            print("| 4 - Ver Notas                  |")
            print("----------------------------------")
            se=input("")

            if se == "1":
                app.barista()
            elif se=="2":
                app.cardapio()
            elif se=="3":
                app.concluir()
            elif se=="4":
                app.mostrar_notinhas()
            
if __name__ =="__main__":
    app=Termbarista()
    app.mysqlconnect()
    app.menu()
