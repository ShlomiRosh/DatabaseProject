import MySQLdb
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
    def get_places_query(self, loc_id, sub_dict, categories_arr):
        if self.connection.connection_state == 'Connected':
            print("the connection status is connected from search sql")
            try:
                # TODO check if only main category is checked
                sql = "SELECT * FROM Places WHERE Places.`Location ID` LIKE %s"
                adr = []
                adr.append(loc_id)
                for cat_check in categories_arr:
                    for sub_check in cat_check.sub_checks_arr:
                        if sub_check and sub_check.check_var.get():
                            sql += " AND Places.`Sub Category` LIKE %s"
                            adr.append(sub_check.code)
                print(sql)
                print(adr)
                self.connection.my_cursor.execute(sql, adr)
                res = self.connection.my_cursor.fetchall()
                self.connection.close()
                return res
            except (MySQLdb.Error, MySQLdb.Warning) as e:
                print(e)
                return 'Error'
        return 'Error'
