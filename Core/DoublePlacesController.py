from Db import SqlDoublePlaces as sdp
from Db import SqlUser as su
from Core import Entities as e
from sklearn.neighbors import NearestCentroid
import pandas as pd


# This module is responsible for the DoublePlacesPage.
class DoublePlacesController:

    def __init__(self, username):
        self.username = username
        self.nearest_places = []

    def get_neighbors(self):
        # Get raw data for the NearestCentroid algorithm.
        raw_user_places = su.SqlUser(self.username).get_user_places()
        if raw_user_places == 'Error':
            return 'Error Connection'
        raw_rest_places = sdp.SqlDoublePlaces(self.username).get_specific_places()
        if raw_rest_places == 'Error':
            return 'Error Connection'
        # Prepare the data for the NearestCentroid algorithm.
        ind = ['Place ID', 'Name', 'Address', 'Latitude', 'Longitude', 'Link', 'Description'
            , 'Location ID', 'Sub Category']
        df_raw_up = pd.DataFrame(raw_user_places, columns=ind)
        df_raw_rp = pd.DataFrame(raw_rest_places, columns=ind)
        user_places = df_raw_up.drop(['Place ID', 'Name', 'Address', 'Link', 'Description'], axis=1, inplace=False)
        rest_places = df_raw_rp.drop(['Name', 'Address', 'Link', 'Description'], axis=1)
        '''This line will leave in the list rest_places only places where the user's subcategories are same.
         The original intention was to give the user all closest places to the places he has on his favorites list,
         not necessarily from the same sub-category, but the terrible runtime of the machine learning algorithm
         doesn't allow that. If the program runs on computers with an NVIDIA GPU card, you can definitely turn
         this line into a note and run all the data! on the GPU in a reasonable amount of time.'''
        rest_places = rest_places[rest_places['Sub Category'].isin(list(dict.fromkeys(user_places['Sub Category'].tolist())))]
        user_places["Sub Category"] = user_places["Sub Category"].map(e.sub_category_to_num)
        rest_places["Sub Category"] = rest_places["Sub Category"].map(e.sub_category_to_num)
        rest_places = rest_places.groupby('Sub Category').head(3500)
        # Prepare the parameters for the algorithm and run it.
        features = list(rest_places.drop('Place ID', axis=1, inplace=False))
        y = rest_places["Place ID"]
        X = rest_places[features]
        clf = NearestCentroid()
        clf.fit(X, y)
        # Prediction of the places that closest to the user's places [close by distance and in categories].
        raw_nearest_places = clf.predict(user_places)
        raw_nearest_places = list(dict.fromkeys(raw_nearest_places))
        for i in raw_nearest_places:
            ins_place = e.Place(df_raw_rp.iloc[i][ind[0]], df_raw_rp.iloc[i][ind[1]], df_raw_rp.iloc[i][ind[2]]
                            , df_raw_rp.iloc[i][ind[3]], df_raw_rp.iloc[i][ind[4]], df_raw_rp.iloc[i][ind[5]]
                            , df_raw_rp.iloc[i][ind[6]], df_raw_rp.iloc[i][ind[7]], df_raw_rp.iloc[i][ind[8]])
            self.nearest_places.append(ins_place)
        return self.nearest_places
