# class database
import mysql.connector

class MysqlConnect:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.cnn = None

    def connect(self):
        self.cnn = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database
        )

    def close(self):
        if self.cnn is not None:
            self.cnn.close()
    
    def execute_query(self, query, data = None):
        cursor = self.cnn.cursor()
        cursor.execute(query, data)
        result = cursor.fetchall()
        cursor.close()

        return result

    def execute_sprocedure(self, sp_name, *args):
        try:
            cursor = self.cnn.cursor()
            cursor.callproc(sp_name, args)
            self.cnn.commit()
            result = 1
        except mysql.connector.Error as error:
            result = 0
            print(error)
        finally:
            cursor.close()

        return result

# settings for mysql connection
mysql_cnn = MysqlConnect(
    host = "localhost",
    user = "root",
    password = "$holtech123",
    database = "db_sales"
)
