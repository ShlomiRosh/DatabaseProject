from Sql import SqlSearch as sse

def get_locations():

    locations = []
    raw_data = sse.SqlSearch().get_locations_schema()

    for location in raw_data:

        locations.append(location[0] + ' ' + location[1])

    return locations