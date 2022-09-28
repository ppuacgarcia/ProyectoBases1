import mariadb
class conexion:

    def __init__(self):
            try:
                self.conn=mariadb.connect(
                    host="localhost",
                    user="root",
                    #password="123456789",
                    password="Kamado_Tanjiro_12",
                    database="iglesia",
                    autocommit=False
                )
            except mariadb.Error as e:
                print("Error al conectarse a la bd",e)
    
    def consultaBD(self,query):
        try:
            with open('Query.txt', 'a') as f:
                f.write(query+"\n")
        except FileNotFoundError:
                print("The 'docs' directory does not exist")
        try:
            cur = self.conn.cursor()
            id2=cur.execute(query)
            print(str(id2))
            return cur
        except mariadb.Error as e:
                    print(e)
                    self.consultaRollback()
                    try:
                        with open('Query.txt', 'a') as f:
                            f.write("rollback to identifier\n")
                    except FileNotFoundError:
                        print("The 'docs' directory does not exist")
        
            
    def consultaRollback(self):
        try:
            curs = self.conn.cursor()
            id2=curs.execute('rollback to identifier')
            self.autocommit=False
            try:
                with open('Query.txt', 'a') as f:
                            f.write("START TRANSACTION\n")
            except FileNotFoundError:
                        print("The 'docs' directory does not exist")
            return curs
        except mariadb.Error as e:
            print("error ")
            print(e)
        
    def commit(self):
        self.conn.commit()
        try:
            with open('Query.txt', 'a') as f:
                f.write("Commit \n")
        except FileNotFoundError:
                print("The 'docs' directory does not exist")