from Sql import SqlSearch as sse

def get_locations():

    pass
    locations = []
    raw_data = sse.SqlSearch().get_locations_schema()

    for location in raw_data:

        locations.append(location[1] + ', ' + location[2])

    return locations