from Sql import SqlConnection as sc

class SqlRegister:

    def __init__(self):

        self.connection = sc.SqlConnection()

    def total_users(self):

        if self.connection.connection_state == 'Connected':
            try:
                self.connection.my_cursor.execute("SELECT COUNT(*) FROM Users")
                res = self.connection.my_cursor.fetchall()
                self.connection.close()
                return res
            except:
                return 'Error'
        return 'Error'

    def record_exist(self, name):

        if self.connection.connection_state == 'Connected':
            try:
                sql = "SELECT `User Name` FROM Users WHERE Users.`User Name` LIKE %s"
                adr = (name,)
                self.connection.my_cursor.execute(sql, adr)
                res = self.connection.my_cursor.fetchall()
                self.connection.close()
                return res
            except:
                return 'Error'
        return 'Error'

    def insert_user_record(self, name, password, first_name, last_name, mail):

        if self.connection.connection_state == 'Connected':
            try:
                sql = "INSERT INTO Users (`User Name`, `First Name`, `Last Name`, `Email`, `Password`) \
                      VALUES (%s, %s, %s, %s, %s)"
                adr = (name, first_name, last_name, mail, password)
                self.connection.my_cursor.execute(sql, adr)
                self.connection.mydb.commit()
                self.connection.close()
                return 'Inserted'
            except:
                return 'Error'
        return 'Error'

