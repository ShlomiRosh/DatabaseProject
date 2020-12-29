from Sql import SqlConnection as sc

# This class performs queries for the class DoublePlacesController.
class SqlDoublePlaces:

    def __init__(self, username):
        self.connection = sc.SqlConnection()
        self.username = username

    # Returns all places except those that are in the user's favorite places list.
    def get_specific_places(self):
        if self.connection.connection_state == 'Connected':
            try:
                # param_num = ','.join(["%s"]*len(places_id))
                # sql = "SELECT Places.* FROM Places WHERE Places.`Place ID` not IN(" + param_num + ")"
                # TODO Check if this query is complex....
                sql = "SELECT Places.* FROM Places WHERE `Place ID` NOT IN(SELECT `Place ID` " \
                       "FROM `Users Places` WHERE `Users Places`.`User Name` LIKE %s)"
                adr = (self.username,)
                self.connection.my_cursor.execute(sql, adr)
                res = self.connection.my_cursor.fetchall()
                self.connection.close()
                return res
            except:
                return 'Error'
        return 'Error'
