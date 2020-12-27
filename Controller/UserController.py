from Sql import SqlUser as su
from Controller import Entities as e

# This module is responsible for the page user.
class UserController:

    def __init__(self, username):
        self.username = username
        self.places = []

    # Turns to SQL gets the user information and puts it into a suitable entity.
    def get_user(self):
        raw_data = su.SqlUser(self.username).get_user_record()[0]
        if raw_data == 'Error':
            return 'Error Connection'
        user = e.User(raw_data[0], raw_data[1], raw_data[2], raw_data[3], raw_data[4])
        return user

    # Turns to SQL asks for the user's favorite places list, puts them in a suitable entity,
    # returns this list to the display page.
    def get_user_places(self):
        raw_data = su.SqlUser(self.username).get_user_places()
        if raw_data == 'Error':
            return 'Error Connection'
        for place in raw_data:
            ins_place = e.Place(place[0], place[1], place[2], place[3], place[4], place[5],
                                place[6], place[7], place[8])
            self.places.append(ins_place)
        return self.places

    # Turns to SQL and asks to remove a place from a particular user's place list.
    def remove_place(self, place_id):
        res = su.SqlUser(self.username).del_places_record(place_id)
        return 'Deleted' if res == 'Deleted' else 'Error Connection'
