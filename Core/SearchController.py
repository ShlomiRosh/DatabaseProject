from Db import SqlSearch as sse
from Core import Entities as e


def get_locations():
    locations = []
    raw_data = sse.SqlSearch().get_locations_schema()
    for location in raw_data:
        locations.append(location[1] + ', ' + location[2])
    return locations


def get_location_id(state, city):
    print(state + " from ctrl")
    print(city + " from ctrl")
    id = sse.SqlSearch().get_location_id(state, city)
    print("result:")
    print(id)
    return id


def get_places(loc_id, sub_dict, categories_arr):
    places = sse.SqlSearch().get_places_query(loc_id, sub_dict, categories_arr)
    print(places)
    places_entities = []
    for place in places:
        places_entities.append(e.Place(place[0], place[1], place[2], place[3], place[4], place[5],
                                       place[6], place[7], place[8]))
    return places_entities
