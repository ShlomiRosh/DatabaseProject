from tkinter import *
import tkinter as tk
from View import AutocompleteSearch as acs
from View import AddPlacePage as app
from Controller import SearchController as sc
from View import UserPage as up

from View import StartPage as st
from View import ResultPage as rp
from Controller import UserController as uc
from View import OverViewButtons as ovb

place_id = None
location_id = None
sub_cutegory = ''
FONT_OUTPUT = ("Ariel", 10)
FONT_LIST = ("Ariel", 10, "bold", "underline")

autocompleteList = sc.get_locations()


class SearchPage(tk.Frame):
    def __init__(self, parent, controller):
        pass
        tk.Frame.__init__(self, parent)
        self.sub_categories_dict = {
            "BCH": False,
            "BCHS": False,
            "CST": False,
            "FISH": False,
            "FLLS": False,
            "LGN": False,
            "LK": False,
            "ML": False,
            "MT": False,
            "OBPT": False,
            "PRK": False,
            "RESF": False,
            "RESN": False,
            "RESW": False,
            "RF": False,
            # --------------
            "CH": False,
            "MSQE": False,
            # --------------
            "AIRP": False,
            "BDG": False,
            "PKLT": False,
            "RFU": False,
            # --------------
            "BOT": False,
            "CMU": False,
            "GMU": False,
            "HSC": False,
            "HST": False,
            "NAT": False,
            "SCI": False,
            "ZAW": False,
            # -------------
            "GHSE": False,
            "HSP": False,
            "HTL": False,
            "MALL": False,
            "MKT": False,
            "REST": False,
            "RHSE": False,
            # --------------
            "ATM" : False,
            "BANK" : False,
            "PO" : False,
            # --------------
            "RECG" : False,
            "STDM" : False,
            "THTR" : False,
            # --------------
            "ANS" : False,
            "ART" : False,
            "CSTL" : False,
            "MNMT" : False,
            "SCH" : False,
            "TMPL" : False
        }
        self.background()
        self.input()
        self.initialize_buttons(controller)

    def background(self):
        pass
        self.img = tk.PhotoImage(file='..\Pic\\searchpagePic.png')
        panel = tk.Label(self, image=self.img)
        panel.place(bordermode=OUTSIDE)

    def input(self):
        search_state_label = tk.Label(self, text="Enter State \ City (Auto-Fill):", bg='black', bd=0, fg='yellow',
                                      font=FONT_OUTPUT)
        search_state_label.place(bordermode=OUTSIDE, x=20, y=25)
        self.state_city = acs.AutocompleteEntry(autocompleteList, self, listboxLength=8, width=50,
                                                matchesFunction=acs.matches)
        self.state_city.place(bordermode=OUTSIDE, height=35, x=20, y=45)

    def initialize_buttons(self, controller):
        # -------------------------------- frame for check boxes for main category ------------------------------------
        main_ctg_label = tk.Label(self, text='Choose Main Category Of Interest:', bg='black', bd=0, fg='yellow',
                                  font=FONT_OUTPUT)
        main_ctg_label.place(bordermode=OUTSIDE, x=20, y=85)
        category_frame = tk.Frame(self)
        category_frame.place(bordermode=OUTSIDE, x=20, y=105, width=710, height=25)

        # -----------------------------------main categories check buttons vars----------------------------------------
        self.nature_check_var = tk.IntVar()
        self.financial_check_var = tk.IntVar()
        self.history_check_var = tk.IntVar()
        self.religion_check_var = tk.IntVar()
        self.commercial_check_var = tk.IntVar()
        self.transportation_check_var = tk.IntVar()
        self.fun_check_var = tk.IntVar()
        self.museums_check_var = tk.IntVar()

        # main categories check buttons
        self.nature_check = Checkbutton(category_frame, text="Nature", onvalue=1, offvalue=0, bg='grey', fg='blue',
                                        command=lambda: self.nature_check_box_on_click(controller),
                                        variable=self.nature_check_var)
        self.financial_check = Checkbutton(category_frame, text="Financial", onvalue=1, offvalue=0, bg='grey',
                                           fg='blue',
                                           command=lambda: self.financial_check_box_on_click(controller),
                                           variable=self.financial_check_var)
        self.history_check = Checkbutton(category_frame, text="History", onvalue=1, offvalue=0, bg='grey', fg='blue',
                                         command=lambda: self.history_check_box_on_click(controller),
                                         variable=self.history_check_var)
        self.religion_check = Checkbutton(category_frame, text="Religion", onvalue=1, offvalue=0, bg='grey', fg='blue',
                                          command=lambda: self.religion_check_box_on_click(controller),
                                          variable=self.religion_check_var)
        self.commercial_check = Checkbutton(category_frame, text="Commercial", onvalue=1, offvalue=0, bg='grey',
                                            fg='blue',
                                            command=lambda: self.commercial_check_box_on_click(controller),
                                            variable=self.commercial_check_var)
        self.transportation_check = Checkbutton(category_frame, text="Transportation", onvalue=1, offvalue=0, bg='grey',
                                                fg='blue',
                                                command=lambda: self.transportation_check_box_on_click(controller),
                                                variable=self.transportation_check_var)
        self.fun_check = Checkbutton(category_frame, text="Fun", onvalue=1, offvalue=0, bg='grey', fg='blue',
                                     command=lambda: self.fun_check_box_on_click(controller),
                                     variable=self.fun_check_var)
        self.museums_check = Checkbutton(category_frame, text="Museums", onvalue=1, offvalue=0, bg='grey', fg='blue',
                                         command=lambda: self.museums_check_box_on_click(controller),
                                         variable=self.museums_check_var)

        # pack them in their frame
        self.nature_check.pack(side=LEFT, fill=BOTH, expand=True)
        self.financial_check.pack(side=LEFT, fill=BOTH, expand=True)
        self.history_check.pack(side=LEFT, fill=BOTH, expand=True)
        self.religion_check.pack(side=LEFT, fill=BOTH, expand=True)
        self.commercial_check.pack(side=LEFT, fill=BOTH, expand=True)
        self.transportation_check.pack(side=LEFT, fill=BOTH, expand=True)
        self.fun_check.pack(side=LEFT, fill=BOTH, expand=True)
        self.museums_check.pack(side=LEFT, fill=BOTH, expand=True)

        # -----------------------------------main categories check buttons vars----------------------------------------
        # -----------------------------------main categories check buttons vars----------------------------------------
        # -----------------------------------main categories check buttons vars----------------------------------------
        # -------------------------------------------religion sub category---------------------------------------------
        self.religion_frame = tk.Frame(self)
        self.church_check_var = tk.IntVar()
        self.mosque_check_var = tk.IntVar()
        self.church_check = Checkbutton(self.religion_frame, text="Church", onvalue=1, offvalue=0, bg='grey', fg='blue',
                                        variable=self.church_check_var)
        self.mosque_check = Checkbutton(self.religion_frame, text="Mosque", onvalue=1, offvalue=0, bg='grey', fg='blue',
                                        variable=self.mosque_check_var)
        self.church_check.pack(side=BOTTOM, fill=BOTH, expand=True)
        self.mosque_check.pack(side=BOTTOM, fill=BOTH, expand=True)
        self.religion_frame.place(bordermode=OUTSIDE, x=270, y=135)
        self.religion_frame.place_forget()
        # -----------------------------------main categories check buttons vars----------------------------------------
        # -----------------------------------main categories check buttons vars----------------------------------------
        # -----------------------------------main categories check buttons vars----------------------------------------
        # -----------------------------------main categories check buttons vars----------------------------------------

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

        # go back button
        self.go_back_img = PhotoImage(file='..\Pic\\bgoback.png')
        back = tk.Button(self, image=self.go_back_img, borderwidth=0, background='black'
                         , command=lambda: self.go_back_on_click(controller))
        back.place(bordermode=OUTSIDE, x=20, y=450)

    # ----------------------------------------------- main cat checks handlers ----------------------------------------
    def nature_check_box_on_click(self, controller):
        if self.nature_check_var.get():
            print("nature is checked")
        else:
            print("nature not checked")

    def financial_check_box_on_click(self, controller):
        if self.financial_check_var.get():
            print("financial_check is checked")
        else:
            print("financial_check not checked")

    def history_check_box_on_click(self, controller):
        if self.history_check_var.get():
            print("history is checked")
        else:
            print("history not checked")

    def fun_check_box_on_click(self, controller):
        if self.fun_check_var.get():
            print("fun is checked")
        else:
            print("fun not checked")

    def museums_check_box_on_click(self, controller):
        if self.museums_check_var.get():
            print("museums is checked")
        else:
            print("museums not checked")

    def religion_check_box_on_click(self, controller):
        if self.religion_check_var.get():
            print("religion is checked")
            self.religion_frame.place(bordermode=OUTSIDE, x=270, y=135)
        else:
            print("religion not checked")
            self.church_check_var.set(0)
            self.mosque_check_var.set(0)
            self.religion_frame.place_forget()

    def transportation_check_box_on_click(self, controller):
        if self.transportation_check_var.get():
            print("transportation is checked")
        else:
            print("transportation not checked")

    def commercial_check_box_on_click(self, controller):
        if self.fun_check_var.get():
            print("commercial is checked")
        else:
            print("commercial not checked")

    # -------------------------------------------------- subs checks handlers ----------------------------------------
    def church_check_box_on_click(self, controller):
        if self.church_check_var.get():
            print("church is checked")
            self.sub_categories_dict["CH"] = True
        else:
            print("church not checked")
            self.sub_categories_dict["CH"] = False

    # -----------------------------------------------other buttons----------------------------------------------------
    def add_place_on_click(self, controller):
        if app.AddPlacePage not in controller.frames:
            controller.add_frame(app.AddPlacePage)
        controller.show_frame(app.AddPlacePage)

    def go_back_on_click(self, controller):
        # self.clean_entrys()
        self.hide_list_box()
        if up.UserPage in controller.frames:
            controller.remove_frame(up.UserPage)
        controller.add_frame(up.UserPage)
        controller.show_frame(up.UserPage)

    # -------------------------------------------------- search! ------------------------------------------------------
    def search_data_on_click(self, controller):
        # message of loading?
        # self.clean_entrys()
        print("loading....")
        # get the city and state id
        state_city_strings = self.state_city.get().split(', ')
        state = state_city_strings[0]
        city = state_city_strings[1]
        print(state)
        print(city)
        # get category id
        location_id = sc.get_location_id(state, city)[0][0]
        print(location_id)
        # send to controller to search
        places = sc.get_places(location_id, self.sub_categories_dict)
        self.show_list_box(controller, places)

    def show_list_box(self, controller, places):
        self.create_listbox()
        self.create_listbox_buttons(controller)
        self.insert_data_to_listbox(places)

    def hide_list_box(self):
        self.listbox.place_forget()
        self.information_itemb.place_forget()

    def create_listbox(self):
        self.listbox = Listbox(self, bg='black', activestyle='dotbox',
                               font=FONT_LIST, fg="yellow")
        self.listbox.place(bordermode=OUTSIDE, x=20, y=140, height=270, width=710)
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
            print(item)
            # self.listbox.insert(END, 'Place ID:' + ' ' + str(item.place_id) + ' '
            #                    + item.place_name.upper())

    def show_info(self, controller):
        global place_id
        place_id = int(self.listbox.get(ANCHOR).split(' ')[2].strip()) if self.listbox.get(ANCHOR) != '' else None
        if place_id is None:
            self.invalid = ovb.create_msg(self, 310, 455, 'Please select place\n''from the list box.')
        else:
            if rp.ResultPage in controller.frames:
                controller.remove_frame(rp.ResultPage)
            controller.add_frame(rp.ResultPage)
            controller.show_frame(rp.ResultPage)
