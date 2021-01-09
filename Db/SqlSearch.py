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
    def get_places_query(self, loc_id, sub_dict, categories_arr):
        if self.connection.connection_state == 'Connected':
            try:
                adr = (loc_id,)
                subs_adr = []
                for cat_check in categories_arr:
                    only_main = True
                    for sub_check in cat_check.sub_checks_arr:
                        if sub_check and sub_check.check_var.get():
                            only_main = False
                            tmp = sub_check.code
                            tmp = "'%s'" % tmp
                            subs_adr.append(tmp)
                    # if only main category is checked - get all subs
                    if only_main and cat_check.check_var.get():
                        only_main = False
                        for sub_check in cat_check.sub_checks_arr:
                            tmp = sub_check.code
                            tmp = "'%s'" % tmp
                            subs_adr.append(tmp)
                adr_string = ','.join(subs_adr)
                sql = "SELECT * FROM Places WHERE Places.`Location ID` LIKE %s AND Places.`Sub Category` IN ("+adr_string+")"

                print(sql)
                print(adr)

                self.connection.my_cursor.execute(sql, adr)
                res = self.connection.my_cursor.fetchall()
                print (res)
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
