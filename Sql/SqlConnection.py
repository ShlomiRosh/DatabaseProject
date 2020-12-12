import mysql.connector


class SqlConnection:

    def __init__(self):

        self.connection_state = ''
        try:
            self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="5678910",
                database="TripleA"
            )
            self.connection_state = 'Connected'
            self.my_cursor = self.mydb.cursor()
        except:
            self.connection_state = 'Not Connected'

    def close(self):

        try:
            self.mydb.close()
        except:
            pass
