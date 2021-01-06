from Db import SqlConnection as sc

# This class performs queries for the module AddPlaceController.
class SqlAddPlace:

    def __init__(self):
        self.connection = sc.SqlConnection()

    def has_place(self, place_name, address):
        if self.connection.connection_state == 'Connected':
            try:
                sql = "SELECT COUNT(*) FROM Places WHERE `Name` = %s AND `Address` = %s"
                adr = (place_name, address)
                self.connection.my_cursor.execute(sql, adr)
                res = self.connection.my_cursor.fetchall()
                self.connection.close()
                return res
            except:
                return 'Error'
        return 'Error'

    def insert_place_record(self, place):
        if self.connection.connection_state == 'Connected':
            try:
                sql = "INSERT INTO Places(`Name`, `Address`, `Latitude`, `Longitude`, `Link`,\
                `Description`, `Location ID`, `Sub Category`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                adr = (place.place_name, place.address, place.latitude, place.longitude, place.link,
                       place.description, place.location_id, place.sub_category)
                self.connection.my_cursor.execute(sql, adr)
                self.connection.mydb.commit()
                self.connection.close()
                return 'Inserted'
            except:
                return 'Error'
        return 'Error'
