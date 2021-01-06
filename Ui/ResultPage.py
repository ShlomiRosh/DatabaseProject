from tkinter import *
import tkinter as tk
from tkinter import ttk
from Ui import SearchPage as sp
from Ui import StartPage as stp
from Core import ResultController as rc
from Ui import OverViewButtons as ovb
from Core import Entities as entities
import webbrowser

FONT_NOTE = ("Ariel", 10, "bold", "underline")


class ResultPage(tk.Frame):

    def __init__(self, parent, controller):
        self.main_frame = tk.Frame.__init__(self, parent)
        self.background()
        self.buttons(controller)
        self.place_id = sp.place_id
        self.categories_dictionary = entities.categories_dictionary
        self.complete_place = rc.ResultController().get_place_all_recorde(self.place_id)
        self.show_results(controller)

    # ----------------------------------------------- initialization --------------------------------------------------

    def background(self):
        self.img = tk.PhotoImage(file='..\Pic\\searchpagePic.png')
        panel = tk.Label(self, image=self.img)
        panel.place(bordermode=OUTSIDE)

    def buttons(self, controller):
        # go back button
        self.go_back_img = PhotoImage(file='..\Pic\\bgoback.png')
        back = tk.Button(self, image=self.go_back_img, borderwidth=0, background='black'
                         , command=lambda: self.go_back_on_click(controller))
        back.place(bordermode=OUTSIDE, x=20, y=450)
        # save place button
        self.save_place_img = PhotoImage(file='..\Pic\\bsaveplace.png')
        save_place = tk.Button(self, image=self.save_place_img, borderwidth=0, background='black'
                               , command=lambda: self.save_place_on_click(controller))
        save_place.place(bordermode=OUTSIDE, x=530, y=445)

    def show_results(self, controller):
        # results main container (grid)
        self.results_frame = tk.Frame(self.main_frame, bg="RED", borderwidth=2)
        Grid.columnconfigure(self.results_frame, 0, weight=0)
        Grid.columnconfigure(self.results_frame, 1, weight=1)
        Grid.columnconfigure(self.results_frame, 2, weight=1)

        Grid.rowconfigure(self.results_frame, 0, weight=0)
        Grid.rowconfigure(self.results_frame, 1, weight=1)
        Grid.rowconfigure(self.results_frame, 2, weight=1)
        Grid.rowconfigure(self.results_frame, 3, weight=1)
        Grid.rowconfigure(self.results_frame, 4, weight=1)

        # results frames
        # ------ name -------
        self.name_frame = tk.Frame(self.results_frame, borderwidth=2)
        tk.Label(self.name_frame, text="Name Of Place: " + self.complete_place.place.place_name, borderwidth=1,
                 font="verdana 13 bold").pack(padx=2,
                                              pady=2)
        category=""
        sub_category=""
        for key in self.categories_dictionary:
            if self.complete_place.category == key[0]:
                category=key[1]
                for sub in self.categories_dictionary[key]:
                    if sub[0] == self.complete_place.place.sub_category:
                        sub_category = sub[1]
        tk.Label(self.name_frame, text="Category: " + category + ", Sub Category: " + sub_category, borderwidth=1,
                 font="verdana 8 bold").pack(padx=2,
                                              pady=2)
        self.name_frame.grid(row=0,
                             column=0,
                             columnspan=3,
                             sticky=N + S + E + W,
                             padx=5,
                             pady=5)

        # ------ add -------
        self.state_city_adress_map_frame = tk.Frame(self.results_frame, borderwidth=2)
        tk.Label(self.state_city_adress_map_frame, text="State:", borderwidth=1, font="verdana 13 bold").pack(
            padx=2,
            pady=2)
        tk.Label(self.state_city_adress_map_frame, text=self.complete_place.state, borderwidth=1).pack()
        tk.Label(self.state_city_adress_map_frame, text="City:", borderwidth=1, font="verdana 13 bold").pack(padx=2,
                                                                                                             pady=2)
        tk.Label(self.state_city_adress_map_frame, text=self.complete_place.city, borderwidth=1).pack()
        tk.Label(self.state_city_adress_map_frame, text="Adress:", borderwidth=1, font="verdana 13 bold").pack(padx=2,
                                                                                                               pady=2)
        tk.Label(self.state_city_adress_map_frame, text=self.complete_place.place.address, borderwidth=1,
                 wraplength=300, justify="center").pack()
        tk.Label(self.state_city_adress_map_frame, text="Click For Google Map:", borderwidth=1,
                 font="verdana 13 bold").pack(padx=2,
                                              pady=2)
        # map
        coordinates = (self.complete_place.place.latitude, self.complete_place.place.longitude)
        # option 2 - button to google maps...
        self.map_image = PhotoImage(file='..\Pic\\map.png')
        # PIL_img.save(filename_wo_extension+".jpg", "JPEG") # save as jpeg
        tk.Button(self.state_city_adress_map_frame, image=self.map_image, borderwidth=2,
                  command=lambda: self.open_map(controller, coordinates)).pack(padx=2,
                                                                               pady=2)
        self.state_city_adress_map_frame.grid(row=1, column=0,
                                              columnspan=1,
                                              rowspan=4,
                                              sticky=N + S + E + W,
                                              padx=5, pady=5)

        # ------ desc -------
        self.description_frame = tk.Frame(self.results_frame, borderwidth=2)
        tk.Label(self.description_frame, text="Description:", borderwidth=1, font="verdana 13 bold").pack(padx=2,
                                                                                                          pady=2)
        tk.Label(self.description_frame, text=self.complete_place.place.description, borderwidth=1,
                 wraplength=400, justify="center").pack(padx=2,
                                                        pady=2)
        tk.Button(self.description_frame, text="Google Search Link", borderwidth=2,
                  command=lambda: self.google_link(controller, coordinates)).pack(padx=2,
                                                                                  pady=2)
        self.description_frame.grid(row=1, column=1,
                                    columnspan=2,
                                    rowspan=2,
                                    sticky=N + S + E + W,
                                    padx=5, pady=5)

        # ------ rank -------
        self.rank_frame = tk.Frame(self.results_frame, borderwidth=2)
        tk.Label(self.rank_frame, text="Rank The Place (1-10)", borderwidth=1, font="verdana 13 bold").pack(padx=2,
                                                                                                            pady=2)
        self.user_rank = ttk.Combobox(self.rank_frame,
                                      values=[
                                          "1",
                                          "2",
                                          "3",
                                          "4", "5", "6", "7", "8", "9", "10"])
        self.user_rank.pack(padx=2, pady=2)
        self.user_rank.bind("<<ComboboxSelected>>", self.get_rank())
        tk.Button(self.rank_frame, text="Rank!", borderwidth=2,
                  command=lambda: self.rank_on_click(controller)).pack(padx=2,
                                                                       pady=2)
        tk.Label(self.rank_frame, text="Average Rank Of the Place",
                 borderwidth=1, font="verdana 13 bold").pack(padx=2,
                                                             pady=2)
        tk.Label(self.rank_frame, text=self.complete_place.rating,
                 borderwidth=1).pack()
        self.rank_frame.grid(row=3, column=1, columnspan=2, rowspan=2,
                             sticky=N + S + E + W,
                             padx=5, pady=5)
        self.results_frame.place(bordermode=OUTSIDE, x=20, y=20, height=420, width=710)

    # ----------------------------------------------- click handlers --------------------------------------------------
    def go_back_on_click(self, controller):
        self.clear_page()
        # load next frame (user page)
        if sp.SearchPage in controller.frames:
            controller.remove_frame(sp.SearchPage)
        controller.add_frame(sp.SearchPage)
        controller.show_frame(sp.SearchPage)

    def save_place_on_click(self, controller):
        user = stp.username
        if user != None and user != "":
            print(user)
            print("saving")
            result = rc.ResultController().add_places_to_user_places(self.complete_place.place.place_id, user)
            print(result)
        else:
            ovb.create_msg(self, 100, 450, 'only registered users can save places')

    def rank_on_click(self, controller):
        # TODO check if user listed
        user = stp.username
        if self.get_rank():
            print("the rank is ranking now is: " + self.get_rank())
            result = rc.ResultController().rank_place(self.get_rank(), self.complete_place.place.place_id, user)
            print(result)
        else:
            ovb.create_msg(self, 200, 450, 'please select a rank first between 1-10')

    def open_map(self, controller, coordinates):
        request = "http://maps.google.com/maps?q="
        request += str(coordinates[0])
        request += ","
        request += str(coordinates[1])
        webbrowser.open_new(request)

    def google_link(self, controller, coordinates):
        request = self.complete_place.place.link
        webbrowser.open_new(request)

    def clear_page(self):
        self.results_frame.place_forget()

    def get_rank(self):
        return self.user_rank.get()


