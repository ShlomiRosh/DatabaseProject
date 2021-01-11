import mysql.connector
from mysql.connector import pooling

# Open the configuration file and take the data to connect with to MYSQL.
file_configuration_name = '..\configuration.txt'
file = open(file_configuration_name, 'r')
lines = tuple(file)
file.close()
map_configuration = {}
# Add to the dict the content of the file, key = host, database, user, password.
for line in lines:
    data = line.strip().split('=')
    if len(data) == 2:
        map_configuration[data[0]] = data[1]
# Create an a connection pool for the SQL modules to preform on.
try:
    connection_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="pynative_pool",
                                                                  pool_size=5,
                                                                  pool_reset_session=True,
                                                                  host=map_configuration['host'],
                                                                  database=map_configuration['database'],
                                                                  user=map_configuration['user'],
                                                                  password=map_configuration['password'])
except:
    print('Error while connecting to MySQL using Connection pool')

# All modules in the SQL folder will hold an object of this class type. This class will
# maintain a connection to the database for them, create a connection, close it according to needs.
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
            print('Error while close Connection')


