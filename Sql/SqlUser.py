from Sql import SqlConnection as sc

class SqlRegister:

    def __init__(self, username):

        self.connection = sc.SqlConnection()
        self.mycursor = self.connection.mydb.cursor()
        self.username = username

    def get_user_record(self):

        sql = "SELECT * FROM users WHERE users.username LIKE %s"
        # sql = "SELECT COUNT(username) FROM users WHERE username LIKE %s AND password LIKE %s"
        adr = (self.username,)
        self.mycursor.execute(sql, adr)

        return self.mycursor.fetchall()
