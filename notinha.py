#tarefa 1:gerar notas fiscais
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
        self.notinhas = []

    def cardapio(self):
        os.system("CLS" if os.name == "nt" else "clear")
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
            print("1 - Adicionar outro pedido")
            print("2 - Finalizar")
            t = int(input(""))
            os.system("CLS" if os.name == "nt" else "clear")

            if t==2:
                self.ped.append((self.mesa, list(self.pedido)))
                self.pedido.clear()
                break

    def barista(self):
        while True:
            os.system("CLS" if os.name == "nt" else "clear")
            print("=============== PEDIDOS PARA BARISTA =============")

            if not self.ped:
                print("\nNenhum pedido pendente.")
                time.sleep(1.5)
                break

            print(f"{'Nº':<5} {'MESA':<10} {'ITENS'}")
            print("-" * 50)
            for i, (mesa, pedido) in enumerate(self.ped, 1):
                itens_formatados = ", ".join(pedido)
                print(f"{i:<5} {mesa:<10} {itens_formatados}")

            print("\nDigite o número do pedido que deseja finalizar.")
            print("")
            print("Ou digite 0 para voltar ao menu principal.")
            escolha = input("Pedido: ")

            if not escolha.isdigit():
                print("Digite um número válido.")
                time.sleep(1)
                continue

            escolha = int(escolha)

            if escolha == 0:
                break
            elif 1 <= escolha <= len(self.ped):
                mesa, pedido = self.ped.pop(escolha - 1)
                itens_formatados = ", ".join(pedido)
                nota = f"Mesa {mesa}: {itens_formatados}"
                self.notinhas.append(nota)
                print(f"Pedido da Mesa {mesa} finalizado.")
                time.sleep(1.5)
            else:
                print("Número inválido.")
                time.sleep(1)

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
                if not self.notinhas:
                    print("Nenhuma notinha salva.")
                else:
                    for nota in self.notinhas:
                        print(nota)
                input("\nPressione Enter para voltar...")

            elif op == "2":
                self.notinhas.clear()
                print("Notinhas apagadas com sucesso.")
                time.sleep(1)

            elif op == "3":
                break

            else:
                print("Opção inválida.")
                time.sleep(1)

if __name__ == "__main__":
    app = Termbarista()
    app.cardapio()

    while True:
        print("1 - Finalizar e enviar ao barista")
        print("2 - Adicionar pedido de outra mesa")
        print("3 - Notinhas")
        se = input("")

        if se == "1":
            app.barista()
            app.mostrar_notinhas()
        elif se == "2":
            app.cardapio()
        elif se == "3":
            app.mostrar_notinhas()

