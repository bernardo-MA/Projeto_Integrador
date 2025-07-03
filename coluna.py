import pymysql as sql
from pymysql import Error
def conectar():
    try:
        conexao=sql.connect(
            host="", #ip do pc
            port="", #porta de wifi (usar a padrao mas no pc do senac usa 3306 ou 8080)
            user="", #usuario (root)
            password="", #senha do usuario (deixar vazio)
            database="", #nome do db pra conectar
        )
        print("Conexão realizada")
        return conexao
    except Error as e:
        print(f"Erro: {e}")
        return None 
        

def cadastrar():
    con=conectar()
    if con:
        try:
            cursor = con.cursor()
            cursor.execute("SHOW TABLES")
            tabelas= cursor.fetchall()
            print("as tabelas são:")
            for tabela in tabelas:
                print(f"{tabela[0]}")
        except Error as e:
            print(f"{e}")
        finally:
            con.close()
            print("Conexão encerrada")
