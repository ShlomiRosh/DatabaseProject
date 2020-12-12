from Sql import SqlAddPlace as sap
from Controller import Entities as e

def place_exists(place_name, address):

    res = sap.SqlAddPlace().has_place(place_name, address)
    if res == 'Error':
        return 'Error Connection'
    return True if res[0][0] != 0 else False

def insert_place(name, addr, longitude, latitude, description, link, sub_cut, loca_id):

    place = e.Place()
    place.place_name = name
    place.address = addr
    place.longitude = longitude
    place.latitude = latitude
    place.description = description
    place.link = link
    place.sub_category = sub_cut
    place.location_id = loca_id
    res = sap.SqlAddPlace().insert_place_record(place)

    return 'Error Connection' if res == 'Error' else 'Inserted'