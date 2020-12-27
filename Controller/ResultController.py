from Sql import SqlResult as sr
from Controller import Entities as e
from mediawiki import MediaWiki
import wikipedia

# This module is responsible for the page result.
class ResultController:

    def __init__(self, place_id):
        self.place_id = place_id
        self.complete_place = self.init_place_rec()

    def init_place_rec(self):
        #sro = sr.SqlResult(self.place_id)
        raw_data = sr.SqlResult(self.place_id).get_place_record()
        if raw_data == 'Error':
            return 'Error Connection'
        ins_place = e.Place(raw_data[0], raw_data[1], raw_data[2], raw_data[3], raw_data[4], raw_data[5],
                            raw_data[6], raw_data[7], raw_data[8])
        # If the place description does not exist, create it and enter into the database.
        if raw_data[6] == '':
            ins_place.description = self.init_description(ins_place)
            res = sr.SqlResult(self.place_id).insert_place_description(ins_place.description)
            if res  == 'Error':
                return 'Error Connection'
        # Get all the other information about the place.
        raw_location = sr.SqlResult(self.place_id).get_location(raw_data[7])
        if raw_location == 'Error':
            return 'Error Connection'
        print(raw_location)
        city, state = raw_location[0], raw_location[1]

        raw_category = sr.SqlResult(self.place_id).get_category(raw_data[8])
        if raw_category == 'Error':
            return 'Error Connection'
        print(raw_category)
        category = raw_category[0]

        complete_place = e.CompletePlace(ins_place, city, state, category)
        return complete_place

    # Try to get a description of the place by contacting Wikipedia.
    def init_description(self, place):
        wiki = MediaWiki()
        try:
            summary = wikipedia.summary(place.place_name, sentences=2)
        except:
            try:
                summary = wiki.geosearch(place.latitude, place.longitude)
                if type(summary) == list:
                    summary = summary[0]
                summary = wikipedia.summary(summary, sentences=2)
            except:
                summary = ''
        print(summary)
        # TODO Resize the description column in the database to 520 characters!!!
        # The description column in the database must be at most 520 characters long.
        if summary == '':
            description = 'No description available.'
        else:
            description = (summary[:500] + '...[wiki summary]') if len(summary) > 500 else summary + '...[wiki summary]'
        return description
