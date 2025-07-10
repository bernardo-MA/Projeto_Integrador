from Conexao import Conexao

conexao=Conexao('cafeteria', '127.0.0.1')
if not conexao.Iniciar():
    print("Não foi possível conectar!")
    quit