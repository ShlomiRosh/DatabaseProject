import asyncio
from Db import SqlConnection as sc


class SqlSearch:
    def __init__(self):
        self.connection = sc.SqlConnection()
        self.mycursor = self.connection.mydb.cursor()

    def get_locations_schema(self):
        sql = "SELECT * FROM locations"
        self.mycursor.execute(sql)
        results = self.mycursor.fetchall()
        return results

    def get_location_id(self, state, city):
        if self.connection.connection_state == 'Connected':
            try:
                sql = "SELECT `Location ID` FROM Locations WHERE Locations.`State` LIKE %s AND Locations.`City/Region` LIKE %s"
                adr = (state, city,)
                self.connection.my_cursor.execute(sql, adr)
                res = self.connection.my_cursor.fetchall()
                self.connection.close()
                return res
            except:
                return 'Error'
        return 'Error'

    # basic query for places
    def get_places_query(self, loc_id, adr_string):
        if self.connection.connection_state == 'Connected':
            try:
                adr = (loc_id,)
                sql = "SELECT * FROM Places WHERE Places.`Location ID` LIKE %s AND Places.`Sub Category` IN ("+adr_string+")"
                self.connection.my_cursor.execute(sql, adr)
                res = self.connection.my_cursor.fetchall()
                self.connection.close()
                return res
            except Exception as e:
                print(e)
                return 'Error'
        return 'Error'

    def get_statistics(self, location_id):
        if self.connection.connection_state == 'Connected':
            try:
                sql = "SELECT Places.`Sub Category`,COUNT(*) FROM Places WHERE Places.`Location ID` = %s GROUP BY Places.`Sub Category`"
                adr = (location_id,)
                self.connection.my_cursor.execute(sql, adr)
                res = self.connection.my_cursor.fetchall()
                self.connection.close()
                print(res)
                return res
            except:
                return 'Error'
        return 'Error'
        pass
