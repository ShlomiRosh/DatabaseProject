from Sql import SqlUser as su
from Controller import Entities as e

class UserController:

    def __init__(self, username):

        self.username = username
        self.user = e.User()
        self.places = []

    def get_user(self):

        raw_data = su.SqlUser(self.username).get_user_record()[0]

        if raw_data == 'Error':
            return 'Error Connection'
        self.user.username = raw_data[0]
        self.user.first_name = raw_data[1]
        self.user.last_name = raw_data[2]
        self.user.email = raw_data[3]
        self.user.password = raw_data[4]

        return self.user

    def get_user_places(self):

        raw_data = su.SqlUser(self.username).get_user_places()

        if raw_data == 'Error':
            return 'Error Connection'
        
        for place in raw_data:

            ins_place = e.Place()
            ins_place.place_id = place[0]
            ins_place.place_name = place[1]
            ins_place.address = place[2]
            ins_place.latitude = place[3]
            ins_place.longitude = place[4]
            ins_place.link = place[5]
            ins_place.description = place[6]
            ins_place.location_id = place[7]
            ins_place.sub_category = place[8]

            self.places.append(ins_place)

        return self.places

    def remove_place(self, place_id):

        res = su.SqlUser(self.username).del_places_record(place_id)
        return 'Deleted' if res == 'Deleted' else 'Error Connection'
