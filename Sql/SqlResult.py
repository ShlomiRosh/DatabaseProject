from Sql import SqlConnection as sc

# This class performs queries for the class ResultController.
class SqlResult:

    def __init__(self, place_id):
        self.connection = sc.SqlConnection()
        self.place_id = place_id

    def get_place_record(self):
        if self.connection.connection_state == 'Connected':
            try:
                sql = "SELECT * FROM Places WHERE Places.`Place ID` LIKE %s"
                adr = (self.place_id,)
                self.connection.my_cursor.execute(sql, adr)
                res = self.connection.my_cursor.fetchone()
                self.connection.close()
                return res
            except:
                return 'Error'
        return 'Error'

    def insert_place_description(self, description):
        if self.connection.connection_state == 'Connected':
            try:
                sql = "UPDATE TripleA.Places SET Places.Description = %s WHERE Places.`Place ID` = %s"
                adr = (description, self.place_id)
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