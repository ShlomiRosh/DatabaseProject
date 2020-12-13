import mysql.connector
from mysql.connector import pooling

try:
    connection_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="pynative_pool",
                                                                  pool_size=5,
                                                                  pool_reset_session=True,
                                                                  host='localhost',
                                                                  database='TripleA',
                                                                  user='root',
                                                                  password='5678910')

except:
    print('Error while connecting to MySQL using Connection pool')

class SqlConnection:

    def __init__(self):

        self.connection_state = ''
        try:
            self.mydb = connection_pool.get_connection()
            if self.mydb.is_connected():
                self.connection_state = 'Connected'
                self.my_cursor = self.mydb.cursor()
        except:
            self.connection_state = 'Not Connected'

    def close(self):

        try:
            if self.mydb.is_connected():
                self.my_cursor.close()
                self.mydb.close()
        except:
            pass


