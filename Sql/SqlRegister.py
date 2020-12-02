from Sql import SqlConnection as sc

class SqlRegister:

    def __init__(self):

        self.connection = sc.SqlConnection()
        self.mycursor = self.connection.mydb.cursor()


    def total_users(self):

        self.mycursor.execute("select count(*) from users")
        return self.mycursor.fetchall()

    def record_exist(self, name):

        sql = "SELECT username FROM users WHERE users.username LIKE %s"
        # sql = "SELECT COUNT(username) FROM users WHERE username LIKE %s AND password LIKE %s"
        adr = (name,)
        self.mycursor.execute(sql,adr)

        return self.mycursor.fetchall()

    def insert_user_record(self, name, password, first_name, last_name, mail):

        sql = "INSERT INTO users (username, firstname, lastname, email, password) VALUES (%s, %s, %s, %s, %s)"
        val = (name, first_name, last_name, mail, password)
        self.mycursor.execute(sql, val)
        self.connection.mydb.commit()

