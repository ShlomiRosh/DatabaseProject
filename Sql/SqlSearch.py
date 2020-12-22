import MySQLdb

from Sql import SqlConnection as sc


class SqlSearch:
    pass

    def __init__(self):
        self.connection = sc.SqlConnection()
        self.mycursor = self.connection.mydb.cursor()

    def get_locations_schema(self):
        sql = "SELECT * FROM locations"
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()

    def get_location_id(self, state, city):
        print(state + " from sql")
        print(city + " from sql")
        if self.connection.connection_state == 'Connected':
            print("the connection status is connected from search sql")
            try:
                sql = "SELECT `Location ID` FROM Locations WHERE Locations.`State` LIKE %s AND Locations.`City/Region` LIKE %s"
                adr = (state, city,)
                self.connection.my_cursor.execute(sql, adr)
                res = self.connection.my_cursor.fetchall()
                self.connection.close()
                return res
            except (MySQLdb.Error, MySQLdb.Warning) as e:
                print(e)
                return 'Error'
        return 'Error'

    # basic query for places
    def get_places_query(self, loc_id, sub_dict):
        if self.connection.connection_state == 'Connected':
            print("the connection status is connected from search sql")
            try:
                sql = "SELECT * FROM Places WHERE Places.`Location ID` LIKE %s"
                adr = []
                adr.append(loc_id)
                for key in sub_dict:
                    if sub_dict[key] == True:
                        sql += " AND Places.`Sub Categoty` LIKE %s"
                        adr.append(key)
                self.connection.my_cursor.execute(sql, adr)
                res = self.connection.my_cursor.fetchall()
                self.connection.close()
                return res
            except (MySQLdb.Error, MySQLdb.Warning) as e:
                print(e)
                return 'Error'
        return 'Error'
