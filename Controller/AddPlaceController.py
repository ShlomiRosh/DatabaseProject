from Sql import SqlAddPlace as sap
from Controller import Entities as e
# This module is responsible for the page Add Place.

# Gets a place name, communicates with the SQL and returns an answer depending on the result.
def place_exists(place_name, address):
    res = sap.SqlAddPlace().has_place(place_name, address)
    if res == 'Error':
        return 'Error Connection'
    return True if res[0][0] != 0 else False


# The function gets a place and details about it, puts it in the appropriate entity and sends it to
# SQL to put it into the database.
def insert_place(name, addr, longitude, latitude, description, link, sub_cut, loca_id):
    place = e.Place(name, addr, longitude, latitude, description, link, sub_cut, loca_id)
    res = sap.SqlAddPlace().insert_place_record(place)
    return 'Error Connection' if res == 'Error' else 'Inserted'