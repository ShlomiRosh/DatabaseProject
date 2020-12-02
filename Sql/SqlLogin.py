from Sql import SqlConnection as sc

class SqlLogin:

    def __init__(self, user, password):

        self.connection = sc.SqlConnection()
        self.user = user
        self.password = password

    def has_record(self):

        mycursor = self.connection.mydb.cursor()
        sql = "SELECT username, COUNT(*) FROM users WHERE username = %s AND password = %s GROUP BY username"
        adr = (self.user, self.password)
        mycursor.execute(sql, adr)

        return mycursor.fetchall()