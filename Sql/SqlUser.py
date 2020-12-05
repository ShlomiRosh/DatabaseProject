from Sql import SqlConnection as sc

class SqlUser:

    def __init__(self, username):

        self.connection = sc.SqlConnection()
        self.mycursor = self.connection.mydb.cursor()
        self.username = username

    def get_user_record(self):

        sql = "SELECT * FROM users WHERE users.username LIKE %s"
        adr = (self.username,)
        self.mycursor.execute(sql, adr)

        return self.mycursor.fetchall()

    def get_user_places(self):

        # *** Complex query Number 1 ***
        sql = "SELECT * FROM places WHERE place_id "" \
        ""IN (SELECT place_id from users_places where username = %s)"
        adr = (self.username,)
        self.mycursor.execute(sql, adr)

        return self.mycursor.fetchall()

    def del_places_record(self, place_id):

        sql = "DELETE FROM users_places WHERE place_id = %s"
        adr = (place_id,)
        self.mycursor.execute(sql, adr)
        self.connection.mydb.commit()