from Conexao import Conexao
from termbarista import Termbarista

app = Termbarista()
app.cardapio()

conexao = Conexao('nome db', '127.0.0.1')

        
if not conexao.Iniciar():
    print("Não foi possível conectar!")
    quit

conexao.Executar('acao sql do balaco bacoooooooo sexo')

conexao.Fechar()