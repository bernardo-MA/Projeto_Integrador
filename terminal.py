bebidas=[]
pedido = []
esc = 0
def cardapio(op,esc,pedido):
    op = ["Expresso","Cappuccino", "Latte"]
    t = 1
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
cardapio(bebidas,esc,pedido)