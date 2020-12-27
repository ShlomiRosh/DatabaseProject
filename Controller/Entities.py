# This module holds entities that are used in a number of other modules in the controller.

class User:

    def __init__(self, username, first_name, last_name, email, password):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password


class Place:

    def __init__(self, place_id, place_name, address, latitude, longitude, link, description,
                 location_id, sub_category):
        self.place_id = place_id
        self.place_name = place_name
        self.address = address
        self.latitude = latitude
        self.longitude = longitude
        self.link = link
        self.description = description
        self.location_id = location_id
        self.sub_category = sub_category

class CompletePlace:

    def __init__(self, place, city, state, category):
        self.place = place
        self.city = city
        self.state = state
        self.category = category