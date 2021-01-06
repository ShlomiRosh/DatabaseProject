import threading
from tkinter import *
import tkinter as tk
from tkinter import ttk

from Ui import AutocompleteSearch as acs
from Ui import AddPlacePage as app
from Core import SearchController as sc
from Ui import UserPage as up
from Ui import ResultPage as rp
from Ui import OverViewButtons as ovb
from Ui.MainCategory import MainCategory
from Core import Entities as entities

place_id = None
location_id = None
FONT_OUTPUT = ("Ariel", 10)
FONT_LIST = ("Ariel", 10, "bold", "underline")
autocompleteList = sc.get_locations()


class SearchPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.categories_dictionary = entities.categories_dictionary
        self.categories_arr = []
        self.load_background()
        self.initialize_search_bar()
        self.initialize_categories(controller)
        self.initialize_user_buttons(controller)
        self.listbox = None

    # ----------------------------------------------- initialization --------------------------------------------------
    def load_background(self):
        pass
        self.img = tk.PhotoImage(file='..\Pic\\searchpagePic.png')
        panel = tk.Label(self, image=self.img)
        panel.place(bordermode=OUTSIDE)

    def initialize_search_bar(self):
        search_state_label = tk.Label(self, text="Enter State \ City (Auto-Fill):", bg='black', bd=0, fg='yellow',
                                      font=FONT_OUTPUT)
        search_state_label.place(bordermode=OUTSIDE, x=20, y=25)
        self.state_city = acs.AutocompleteEntry(autocompleteList, self, listboxLength=8, width=50,
                                                matchesFunction=acs.matches)
        self.state_city.place(bordermode=OUTSIDE, height=35, x=20, y=45)

    def initialize_categories(self, controller):
        # -------------------------------- frame for check boxes for main category ------------------------------------
        main_ctg_label = tk.Label(self, text='Choose Main Category Of Interest:', bg='black', bd=0, fg='yellow',
                                  font=FONT_OUTPUT)
        main_ctg_label.place(bordermode=OUTSIDE, x=20, y=85)
        category_frame = tk.Frame(self)
        category_frame.place(bordermode=OUTSIDE, x=20, y=105, width=710, height=25)
        # ----------------------------------------- create the categories :) ------------------------------------------
        for main_category_name_code in self.categories_dictionary:
            new_main = MainCategory(controller, category_frame, main_category_name_code,
                                    self.categories_dictionary[main_category_name_code])
            self.categories_arr.append(new_main)
        # pack
        for main_category in self.categories_arr:
            main_category.check_button.pack(side=LEFT, fill=BOTH, expand=True)
            main_category.initialize_sub_categories(controller)

    def initialize_user_buttons(self, controller):
        # ---------------------------------------------- user butons -------------------------------------------------
        # search button
        self.search_img = PhotoImage(file='..\Pic\\bsearch1.png')
        self.search_data = tk.Button(self, image=self.search_img, borderwidth=0, background='black'
                                     , command=lambda: self.search_data_on_click(controller))
        self.search_data.place(bordermode=OUTSIDE, x=340, y=45)
        # add place button
        self.add_img = PhotoImage(file='..\Pic\\badd.png')
        self.add_place = tk.Button(self, image=self.add_img, borderwidth=0, background='black'
                                   , command=lambda: self.add_place_on_click(controller))
        self.add_place.place(bordermode=OUTSIDE, x=580, y=450)
        add_info_label = tk.Label(self, text="Add Places You Couldn't Find by Pressing Add", bg='black', bd=0,
                                  fg='yellow',
                                  font=FONT_OUTPUT, wraplength=200, justify='center')
        add_info_label.place(bordermode=OUTSIDE, x=530, y=45)
        # go back button
        self.go_back_img = PhotoImage(file='..\Pic\\bgoback.png')
        back = tk.Button(self, image=self.go_back_img, borderwidth=0, background='black'
                         , command=lambda: self.go_back_on_click(controller))
        back.place(bordermode=OUTSIDE, x=20, y=450)

    # ----------------------------------------------- user buttons! ---------------------------------------------------

    def add_place_on_click(self, controller):
        self.clear_page()
        if app.AddPlacePage not in controller.frames:
            controller.add_frame(app.AddPlacePage)
        controller.show_frame(app.AddPlacePage)

    def go_back_on_click(self, controller):
        self.clear_page()
        # load next frame (user page)
        if up.UserPage in controller.frames:
            controller.remove_frame(up.UserPage)
        controller.add_frame(up.UserPage)
        controller.show_frame(up.UserPage)

    def show_info(self, controller):
        self.progress_bar_result = ttk.Progressbar(self, orient='horizontal', mode='indeterminate')
        self.progress_bar_result.place(bordermode=OUTSIDE, x=415, y=410, height=30, width=250)
        self.progress_bar_result.start()
        self.thread_load_place_info = threading.Thread(target=lambda: self.thread_function_load_result_page(controller))
        self.thread_load_place_info.start()

    def thread_function_load_result_page(self, controller):
        global place_id
        place_id = int(self.listbox.get(ANCHOR).split(' ')[2].strip()) if self.listbox.get(ANCHOR) != '' else None
        # user has not selected any place to show
        if place_id is None:
            self.invalid = ovb.create_msg(self, 310, 455, 'Please select place\n''from the list box.')
        else:
            # move to result page
            if rp.ResultPage in controller.frames:
                controller.remove_frame(rp.ResultPage)
            controller.add_frame(rp.ResultPage)
            controller.show_frame(rp.ResultPage)
        self.progress_bar_result.destroy()

    # -------------------------------------------------- search! ------------------------------------------------------
    def search_data_on_click(self, controller):
        # message of loading?
        # self.clean_entrys()
        # check if the input is valid location in autocomplete places...
        if not self.state_city.get() in autocompleteList:
            ovb.create_msg(self, 200, 450, 'this place is not in our data base, please try again...')
            return
        self.progress_bar = ttk.Progressbar(self, orient='horizontal', mode='indeterminate')
        self.progress_bar.place(bordermode=OUTSIDE, x=415, y=410, height=30, width=250)
        self.progress_bar.start()
        # TODO add another complex query of group by
        self.thread_basic_search = threading.Thread(target=lambda: self.thread_function_basic_search(controller))
        self.thread_basic_search.start()

    def thread_function_basic_search(self, controller):
        # get the city and state id
        state_city_strings = self.state_city.get().split(', ')
        state = state_city_strings[0]
        city = state_city_strings[1]
        # get category id
        location_id = sc.get_location_id(state, city)[0][0]
        # send to controller to search
        places = sc.get_places(location_id, self.categories_dictionary, self.categories_arr)
        self.clear_checks()

        self.show_list_box(controller, places)

    def show_list_box(self, controller, places):
        self.create_listbox()
        self.insert_data_to_listbox(places)
        self.create_listbox_buttons(controller)


    def hide_list_box(self):
        if self.listbox:
            self.listbox.place_forget()
            self.information_itemb.place_forget()

    def create_listbox(self):
        self.listbox = Listbox(self, bg='black', activestyle='dotbox',
                               font=FONT_LIST, fg="yellow")

        scrollbar = Scrollbar(self.listbox, orient="vertical")
        scrollbar.config(command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=scrollbar.set)

    def create_listbox_buttons(self, controller):
        self.showp_img = PhotoImage(file='..\Pic\\binfo.png')
        self.information_itemb = tk.Button(self, image=self.showp_img, borderwidth=0, background='black'
                                           , command=lambda: self.show_info(controller))
        self.information_itemb.place(bordermode=OUTSIDE, x=300, y=420)

    def insert_data_to_listbox(self, places):
        for item in places:
            self.listbox.insert(END, 'Place ID:' + ' ' + str(item.place_id) + ' '
                                + item.place_name.upper())
        self.listbox.place(bordermode=OUTSIDE, x=20, y=140, height=270, width=710)
        self.progress_bar.destroy()

    def clear_checks(self):
        # clear categories check boxes
        for main in self.categories_arr:
            main.clear()

    def clear_page(self):
        self.clear_checks()
        # clear List
        self.hide_list_box()
