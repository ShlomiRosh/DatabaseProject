from Sql import SqlConnection as sc

# This class performs queries for the class UserController.
class SqlUser:

    def __init__(self, username):
        self.connection = sc.SqlConnection()
        self.username = username

    def get_user_record(self):
        if self.connection.connection_state == 'Connected':
            try:
                sql = "SELECT * FROM Users WHERE Users.`User Name` LIKE %s"
                adr = (self.username,)
                self.connection.my_cursor.execute(sql, adr)
                res = self.connection.my_cursor.fetchall()
                self.connection.close()
                return res
            except:
                return 'Error'
        return 'Error'

    def get_user_places(self):
        if self.connection.connection_state == 'Connected':
            try:
                sql = "SELECT DISTINCT Places.*  FROM Places JOIN `Users Places` USING(`Place ID`) "" \
                      ""WHERE `Users Places`.`User Name` = %s"
                adr = (self.username,)
                self.connection.my_cursor.execute(sql, adr)
                res = self.connection.my_cursor.fetchall()
                self.connection.close()
                return res
            except:
                return 'Error'
        return 'Error'

    def del_places_record(self, place_id):
        if self.connection.connection_state == 'Connected':
            try:
                sql = "DELETE FROM `Users Places` WHERE `Place ID` = %s"
                adr = (place_id,)
                self.connection.my_cursor.execute(sql, adr)
                self.connection.mydb.commit()
                self.connection.close()
                return 'Deleted'
            except:
                return 'Error'
        return 'Error'