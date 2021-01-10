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

    def __init__(self, place, city, state, category, rating):
        self.place = place
        self.city = city
        self.state = state
        self.category = category
        self.rating = rating


sub_category_to_num = {'AIRP': 51, 'AMUS': 21, 'ANS': 3, 'ART': 22, 'ATM': 15, 'BANK': 16, 'BCH': 32,
                       'BCHS': 44, 'BDG': 53, 'BOT': 24, 'CH': 49, 'CMU': 26, 'CSNO': 20, 'CST': 47, 'CSTL': 6,
                       'FISH': 45, 'FLLS': 38, 'GHSE': 13, 'GMU': 29, 'HSC': 30, 'HSP': 8, 'HST': 23, 'HTL': 11,
                       'LGN': 46, 'LK': 33, 'MALL': 7, 'MKT': 12, 'ML': 48, 'MNMT': 1, 'MSQE': 50, 'MT': 31,
                       'NAT': 27, 'OBPT': 42, 'PKLT': 52, 'PO': 14, 'PRK': 34, 'RECG': 17, 'RESF': 39, 'RESN': 35,
                       'REST': 9, 'RESW': 37, 'RF': 36, 'RFU': 54, 'RHSE': 10, 'RKRY': 43, 'SCH': 40, 'SCI': 25,
                       'STDM': 18, 'THTR': 19, 'TMPL': 2, 'VLC': 41, 'ZAW': 28}

categories_dictionary = {
    ("NTRL", "Nature"): [("BCH", "Beach"), ("BCHS", "Beaches"), ("CST", "Coast"), ("FISH", "Fish"),
                         ("FLLS", "Waterfalls"), ("LGN", "Lagona"), ("LK", "Lake"), ("MT", "Mountain"),
                         ("OBPT", "Obsercation Point"), ("PRK", "Park"), ("RESF", "Forest Reserve"),
                         ("RESN", "Nature Reserve"), ("RESW", "Wildlife Reserve"), ("RF", "Reef"), ("VLC", "Volcano"), ("RKRY", "Birds Colony"), ("ML", "Nature Products")],
    ("HSTRY", "History"): [("ANS", "History Site"), ("ART", "Piece Of Art"), ("CSTL", "Castle"),
                           ("MNMT", "Monument"),
                           ("TMPL", "Temple")],
    ("FNNC", "Financial"): [("ATM", "Atm - Machine"), ("BANK", "Bank"), ("PO", "Post Office")],
    ("MUSE", "Museums"): [("BOT", "Botanical"), ("CMU", "Children's"), ("GMU", "General"),
                          ("HSC", "Preservation"),
                          ("HST", "History"), ("NAT", "Natural"), ("SCI", "Science & Tech"), ("ZAW", "Zoo")],
    ("FUN", "Fun"): [("RECG", "Golf"), ("STDM", "Stadium"), ("THTR", "Theatre"), ("AMUS", "Amusement Park"), ("SCNO", "Casino")],
    ("TRNSPT", "Transportation"): [("AIRP", "Airport"), ("PKLT", "Parking Lot")],
    ("COMRC", "Commercial"): [("GHSE", "Guest House"), ("HSP", "Hospital"), ("HTL", "Hotel"), ("MALL", "Mall"),
                              ("MKT", "Market"), ("REST", "Restaurant"), ("RHSE", "Rest House")],
    ("RELIG", "Religion"): [("CH", "Churches"), ("MSQE", "Mosque")]
}

def get_sub_category_dict():
    sub_category_dict = {}
    for i in categories_dictionary:
        sub_categories = categories_dictionary[i]
        for j in range(len(sub_categories)):
            sub_category = sub_categories[j]
            sub_category_dict[sub_category[0]] =  sub_category[1]
    return sub_category_dict