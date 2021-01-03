from Sql import SqlConnection as sc

# This class performs queries for the class ResultController.
class SqlResult:

    def __init__(self):
        self.connection = sc.SqlConnection()

    def get_place_record(self, place_id):
        if self.connection.connection_state == 'Connected':
            try:
                sql = "SELECT * FROM Places WHERE Places.`Place ID` LIKE %s"
                adr = (place_id,)
                self.connection.my_cursor.execute(sql, adr)
                res = self.connection.my_cursor.fetchone()
                self.connection.close()
                return res
            except:
                return 'Error'
        return 'Error'

    def insert_place_description(self, description, place_id):
        if self.connection.connection_state == 'Connected':
            try:
                sql = "UPDATE TripleA.Places SET Places.Description = %s WHERE Places.`Place ID` = %s"
                adr = (description, place_id)
                self.connection.my_cursor.execute(sql, adr)
                self.connection.mydb.commit()
                self.connection.close()
                return 'Inserted'
            except:
                return 'Error'
        return 'Error'

    def get_location(self, location_id):
        if self.connection.connection_state == 'Connected':
            try:
                sql = "SELECT Locations.`State`, Locations.`City/Region` FROM Locations WHERE Locations.`Location ID` LIKE %s"
                adr = (location_id,)
                self.connection.my_cursor.execute(sql, adr)
                res = self.connection.my_cursor.fetchone()
                self.connection.close()
                return res
            except:
                return 'Error'
        return 'Error'

    def get_category(self, sub_category):
        if self.connection.connection_state == 'Connected':
            try:
                sql = "SELECT `Category` FROM Categories WHERE Categories.`Sub Category` LIKE %s"
                adr = (sub_category,)
                self.connection.my_cursor.execute(sql, adr)
                res = self.connection.my_cursor.fetchone()
                self.connection.close()
                return res
            except:
                return 'Error'
        return 'Error'

    def insert_places_(self, places, username):
        if self.connection.connection_state == 'Connected':
            try:
                # param_num = '%s'
                # if type(places) == list:
                #     param_num = ','.join(["%s"] * len(places))
                sql = "INSERT INTO `users places`(`User Name`, `Place ID`) VALUES (%s, %s)"
                val = []
                if type(places) == list:
                    for i in places:
                        val.append((username, i))
                else:
                    val = (username, places)
                print(sql)
                print(val)
                self.connection.my_cursor.executemany(sql, val)
                self.connection.mydb.commit()
                self.connection.close()
                return 'Inserted'
            except:
                return 'Error'
        return 'Error'

    # Complex query, get average place ratings.
    def get_rating(self, location_id):
        if self.connection.connection_state == 'Connected':
            try:
                sql = "SELECT AVG(Rating) FROM `users places` WHERE `Place ID` = %s"
                adr = (location_id,)
                self.connection.my_cursor.execute(sql, adr)
                res = self.connection.my_cursor.fetchone()
                self.connection.close()
                return res
            except:
                return 'Error'
        return 'Error'
