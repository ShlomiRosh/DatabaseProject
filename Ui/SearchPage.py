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
from Ui import StartPage as sp

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

        #------------------ The button should only be created after the user has seen the results.
        # self.add_place = tk.Button(self, image=self.add_img, borderwidth=0, background='black'
        #                            , command=lambda: self.add_place_on_click(controller))
        # self.add_place.place(bordermode=OUTSIDE, x=50, y=440)
        # add_info_label = tk.Label(self, text="Add Places You Couldn't Find by Pressing Add", bg='black', bd=0,
        #                           fg='yellow',
        #                           font=FONT_OUTPUT, wraplength=200, justify='center')
        # add_info_label.place(bordermode=OUTSIDE, x=530, y=45)
        #--------------------------------------------------------------------------------------

        # go back button
        self.go_back_img = PhotoImage(file='..\Pic\\bgoback.png')
        back = tk.Button(self, image=self.go_back_img, borderwidth=0, background='black'
                         , command=lambda: self.go_back_on_click(controller))
        back.place(bordermode=OUTSIDE, x=570, y=450)

    # ----------------------------------------------- user buttons! ---------------------------------------------------

    def add_place_on_click(self, controller):
        self.clear_page()
        # if location_id is not None:
        controller.manage_frame(app.AddPlacePage)
        # else:
        #     self.invalid = ovb.create_msg(self, 310, 455, 'To add place to our DB\n''you need to search first\n'/
        #                                   'to check that it does not exist already.')

    def go_back_on_click(self, controller):
        self.clear_page()
        # load next frame checking where the user came from.
        if sp.username != '':
            controller.manage_frame(up.UserPage)
        else:
            controller.manage_frame(sp.StartPage)

    def show_info(self, controller):
        self.progress_bar_result = ttk.Progressbar(self, orient='horizontal', mode='indeterminate')
        self.progress_bar_result.place(bordermode=OUTSIDE, x=470, y=410, height=30, width=250)
        self.progress_bar_result.start()
        self.thread_load_place_info = threading.Thread(target=lambda: self.thread_function_load_result_page(controller))
        self.thread_load_place_info.setDaemon(True)
        self.thread_load_place_info.start()

    def thread_function_load_result_page(self, controller):
        global place_id
        place_id = int(self.listbox.get(ANCHOR).split(' ')[2].strip()) if self.listbox.get(ANCHOR) != '' else None
        # user has not selected any place to show
        if place_id is None:
            self.invalid = ovb.create_msg(self, 310, 455, 'Please select place\n''from the list box.')
        else:
            # move to result page
            controller.manage_frame(rp.ResultPage)
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
        self.progress_bar.place(bordermode=OUTSIDE, x=470, y=410, height=30, width=250)
        self.progress_bar.start()
        self.thread_basic_search = threading.Thread(target=lambda: self.thread_function_basic_search(controller))
        self.thread_basic_search.setDaemon(True)
        self.thread_basic_search.start()

    def thread_function_basic_search(self, controller):
        # get the city and state id
        state_city_strings = self.state_city.get().split(', ')
        state = state_city_strings[0]
        city = state_city_strings[1]
        # get category id
        global location_id
        location_id = sc.get_location_id(state, city)[0][0]
        # send to controller to search
        # TODO add another complex query of group by
        places = sc.get_places(location_id, self.categories_dictionary, self.categories_arr)
        statistics = sc.get_statistics(location_id)
        print(statistics)
        self.clear_checks()
        self.show_statistics(statistics)
        self.show_list_box(controller, places)

    def show_statistics(self, statistics):
        if statistics == 'Error Connection':
            self.invalid = ovb.create_msg(self, 570, 455, 'Error occurred while\n''accessing database.')
        else:
            txt_label = 'In the country and city you searched\n'' for,' \
                       ' the following data exists in our database\n'' (Number of places available of any kind):'
            self.statistics_label = Label(self, text=txt_label, bg='black', bd=0,
                                  fg='yellow', font=FONT_OUTPUT)
            self.statistics_label.place(bordermode=OUTSIDE, x=460, y=140)
            self.text_statistics = Text(self, width=30, height=12)
            self.text_statistics.insert(INSERT, statistics)
            self.text_statistics.place(bordermode=OUTSIDE, x=470, y=200)


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
        self.information_itemb.place(bordermode=OUTSIDE, x=250, y=430)
        self.add_place = tk.Button(self, image=self.add_img, borderwidth=0, background='black'
                                   , command=lambda: self.add_place_on_click(controller))
        self.add_place.place(bordermode=OUTSIDE, x=70, y=430)
        note = tk.Label(self, text='Note here!', bg='black', bd=0, fg='blue', font=FONT_LIST)
        note.place(bordermode=OUTSIDE, x=70, y=465)
        ovb.create_tool_tip(note, text='Add Places You Couldn\'t\n''Find in the result by Pressing Add.')

    def insert_data_to_listbox(self, places):
        for item in places:
            self.listbox.insert(END, 'Place ID:' + ' ' + str(item.place_id) + ' '
                                + item.place_name.upper())

        self.listbox.place(bordermode=OUTSIDE, x=20, y=140, height=270, width=430)
        self.progress_bar.destroy()

    def clear_checks(self):
        # clear categories check boxes
        for main in self.categories_arr:
            main.clear()

    def clear_page(self):
        self.clear_checks()
        # clear List
        self.hide_list_box()
