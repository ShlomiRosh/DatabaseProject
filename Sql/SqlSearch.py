from Sql import SqlConnection as sc

class SqlSearch:

    def __init__(self):

        self.connection = sc.SqlConnection()
        self.mycursor = self.connection.mydb.cursor()

    def get_locations_schema(self):

        sql = "SELECT * FROM locations"
        self.mycursor.execute(sql)

        return self.mycursor.fetchall()