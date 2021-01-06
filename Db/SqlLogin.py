from Db import SqlConnection as sc

# This class performs queries for the module LoginController.
class SqlLogin:

    def __init__(self, user, password):
        self.connection = sc.SqlConnection()
        self.user = user
        self.password = password

    def has_record(self):
        if self.connection.connection_state == 'Connected':
            try:
                sql = "SELECT COUNT(*) FROM Users WHERE `User Name` = %s AND Password = %s"
                adr = (self.user, self.password)
                self.connection.my_cursor.execute(sql, adr)
                res = self.connection.my_cursor.fetchall()
                self.connection.close()
                return res
            except:
                return 'Error'
        return 'Error'