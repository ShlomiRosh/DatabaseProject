from Sql import SqlSearch as sse


def get_locations():
    pass
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
    return places
