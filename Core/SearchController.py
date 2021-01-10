from Db import SqlSearch as sse
from Core import Entities as e


def get_locations():
    locations = []
    raw_data = sse.SqlSearch().get_locations_schema()
    if raw_data == 'Error':
        return 'Error Connection'
    for location in raw_data:
        locations.append(location[1] + ', ' + location[2])
    return locations


def get_location_id(state, city):
    id = sse.SqlSearch().get_location_id(state, city)
    return id if id != 'Error' else 'Error Connection'


def get_places(loc_id, sub_dict, categories_arr):
    # prepare the sub categories to check
    subs_adr = []
    for cat_check in categories_arr:
        if cat_check and cat_check.check_var.get():
            only_main = True
        else:
            only_main = False
        for sub_check in cat_check.sub_checks_arr:
            if sub_check and sub_check.check_var.get():
                only_main = False
                tmp = sub_check.code
                tmp = "'%s'" % tmp
                subs_adr.append(tmp)
        # if only main category is checked - get all subs
        if only_main and cat_check.check_var.get():
            only_main = False
            for sub_check in cat_check.sub_checks_arr:
                tmp = sub_check.code
                tmp = "'%s'" % tmp
                subs_adr.append(tmp)
    # if nothing is checked, search for all sub categories!
    if len(subs_adr) == 0:
        for cat_check in categories_arr:
            for sub_check in cat_check.sub_checks_arr:
                tmp = sub_check.code
                tmp = "'%s'" % tmp
                subs_adr.append(tmp)
    # prepare the string for IN query
    adr_string = ','.join(subs_adr)
    places = sse.SqlSearch().get_places_query(loc_id, adr_string)
    if places == 'Error':
        return 'Error Connection'
    places_entities = []
    for place in places:
        places_entities.append(e.Place(place[0], place[1], place[2], place[3], place[4], place[5],
                                       place[6], place[7], place[8]))
    return places_entities


def get_statistics(location_id):
    raw_statistics = sse.SqlSearch().get_statistics(location_id)
    if raw_statistics == 'Error':
        return 'Error Connection'
    statistics = ''
    dict_sc = e.get_sub_category_dict()
    for tup in raw_statistics:
        statistics += str(tup[1]) + ' places of ' + dict_sc[tup[0]] + '\n'
    return statistics