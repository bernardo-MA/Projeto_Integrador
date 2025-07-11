import pymysql

class conecta:
    def mysqlconnect():
        # To connect MySQL database
        conn = pymysql.connect(
            host='127.0.0.1',
            user='root', 
            password = "",
            db='cafeteria',
            )
        
        cur = conn.cursor()
        
        # Select query
        cur.execute("select * from ordem")
        output = cur.fetchall()
        
        for a,b,c,d in output:
            print(f"ID:{a}")
            print(f"Mesa:{b}")
            print(f"Pedido:{c}")
            print(f"Data:{d}")
            print("--------------------------")
        
        # To close the connection
        conn.close()

    # Driver Code
    if __name__ == "_main_" :
        mysqlconnect()