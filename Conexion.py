import mariadb
class conexion:

    def __init__(self):
            try:
                self.conn=mariadb.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    #password="Kamado_Tanjiro_12",
                    database="iglesia",
                    autocommit=False
                )
            except mariadb.Error as e:
                print("Error al conectarse a la bd",e)
    
    def consultaBD(self,query):
        try:
            cur = self.conn.cursor()
            id2=cur.execute(query)
            print(str(id2))
            return cur
        except mariadb.Error as e:
                    print(e)
                    self.consultaRollback()
        
            
    def consultaRollback(self):
        try:
            curs = self.conn.cursor()
            id2=curs.execute('rollback to identifier')
            print("rollback ")
            self.autocommit=False
            return curs
        except mariadb.Error as e:
            print("error ")
            print(e)
        
    def commit(self):
        self.conn.commit()