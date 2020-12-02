import mysql.connector


class SqlConnection:

    def __init__(self):

        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="5678910",
            database="sql_invoicing"
        )
