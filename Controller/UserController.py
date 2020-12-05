from Sql import SqlUser as su


class User:

    username = ''
    first_name = ''
    last_name = ''
    email = ''
    password = ''


class Place:

    place_id = 0
    place_name = ''
    state = ''
    city = ''
    address = ''
    sub_category = ''
    longitude = 0.0
    latitude = 0.0
    link = ''
    description = None
    category = ''


class UserController:

    def __init__(self, username):

        self.username = username
        self.user = User()
        #self.place = Place()
        self.places = []

    def get_user(self):

        raw_data = su.SqlUser(self.username).get_user_record()[0]
        self.user.username = raw_data[0]
        self.user.first_name = raw_data[1]
        self.user.last_name = raw_data[2]
        self.user.email = raw_data[3]
        self.user.password = raw_data[4]

        return self.user

    def get_user_places(self):

        raw_data = su.SqlUser(self.username).get_user_places()

        for place in raw_data:

            ins_place = Place()
            ins_place.place_id = place[0]
            ins_place.place_name = place[1]
            ins_place.state = place[2]
            ins_place.city = place[3]
            ins_place.address = place[4]
            ins_place.sub_category = place[5]
            ins_place.latitude = place[6]
            ins_place.longitude = place[7]
            ins_place.link = place[8]
            ins_place.description = place[9]
            ins_place.category = place[10]

            self.places.append(ins_place)

        return self.places

    def remove_place(self, place_id):

        su.SqlUser(self.username).del_places_record(place_id)
