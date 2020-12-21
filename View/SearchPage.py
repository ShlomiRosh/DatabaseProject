from tkinter import *
import tkinter as tk
from View import AutocompleteSearch as acs
from View import AddPlacePage as app
from Controller import SearchController as sc
from View import StartPage as st
from View import OverViewButtons as ovb
from View import UserPage as up

location_id = None
sub_cutegory = ''
FONT_OUTPUT = ("Ariel", 10)
FONT_LIST = ("Ariel", 10, "bold", "underline")

autocompleteList = sc.get_locations()


class SearchPage(tk.Frame):
    def __init__(self, parent, controller):
        pass
        tk.Frame.__init__(self, parent)
        self.background()
        self.input()
        self.initialize_buttons(controller)

    def background(self):
        pass
        self.img = tk.PhotoImage(file='..\Pic\\searchpagePic.png')
        panel = tk.Label(self, image=self.img)
        panel.place(bordermode=OUTSIDE)

    # self.configure(background='blue')

    def input(self):
        search_state_label = tk.Label(self, text="Enter State \ City (Auto-Fill):", bg='black', bd=0, fg='yellow',
                                      font=FONT_OUTPUT)
        search_state_label.place(bordermode=OUTSIDE, x=20, y=25)
        self.entry = acs.AutocompleteEntry(autocompleteList, self, listboxLength=8, width=50,
                                           matchesFunction=acs.matches)
        self.entry.place(bordermode=OUTSIDE, height=35, x=20, y=45)

    def initialize_buttons(self, controller):
        # frame for check boxes for main category
        main_ctg_label = tk.Label(self, text='Choose Main Category Of Interest:', bg='black', bd=0, fg='yellow',
                                  font=FONT_OUTPUT)
        main_ctg_label.place(bordermode=OUTSIDE, x=20, y=85)
        frame = tk.Frame(self)
        frame.place(bordermode=OUTSIDE, x=20, y=105, width=710, height=25)

        # main categories check buttons vars
        self.nature_check_var = tk.IntVar()
        self.financial_check_var = tk.IntVar()
        self.history_check_var = tk.IntVar()
        self.religion_check_var = tk.IntVar()
        self.commercial_check_var = tk.IntVar()
        self.transportation_check_var = tk.IntVar()
        self.fun_check_var = tk.IntVar()
        self.museums_check_var = tk.IntVar()

        # main categories check buttons
        self.nature_check = Checkbutton(frame, text="Nature", onvalue=1, offvalue=0, bg='grey', fg='blue',
                                        command=lambda: self.nature_check_box_on_click(controller),
                                        variable=self.nature_check_var)
        self.financial_check = Checkbutton(frame, text="Financial", onvalue=1, offvalue=0, bg='grey', fg='blue',
                                           command=lambda: self.financial_check_box_on_click(controller),
                                           variable=self.financial_check_var)
        self.history_check = Checkbutton(frame, text="History", onvalue=1, offvalue=0, bg='grey', fg='blue',
                                         command=lambda: self.history_check_box_on_click(controller),
                                         variable=self.history_check_var)
        self.religion_check = Checkbutton(frame, text="Religion", onvalue=1, offvalue=0, bg='grey', fg='blue',
                                          command=lambda: self.religion_check_box_on_click(controller),
                                          variable=self.religion_check_var)
        self.commercial_check = Checkbutton(frame, text="Commercial", onvalue=1, offvalue=0, bg='grey', fg='blue',
                                            command=lambda: self.commercial_check_box_on_click(controller),
                                            variable=self.commercial_check_var)
        self.transportation_check = Checkbutton(frame, text="Transportation", onvalue=1, offvalue=0, bg='grey',
                                                fg='blue',
                                                command=lambda: self.transportation_check_box_on_click(controller),
                                                variable=self.transportation_check_var)
        self.fun_check = Checkbutton(frame, text="Fun", onvalue=1, offvalue=0, bg='grey', fg='blue',
                                     command=lambda: self.fun_check_box_on_click(controller),
                                     variable=self.fun_check_var)
        self.museums_check = Checkbutton(frame, text="Museums", onvalue=1, offvalue=0, bg='grey', fg='blue',
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

        # search button
        self.search_img = PhotoImage(file='..\Pic\\bsearch1.png')
        self.search_data = tk.Button(self, image=self.search_img, borderwidth=0, background='black'
                                     , command=lambda: self.search_data_on_click(controller))
        self.search_data.place(bordermode=OUTSIDE, x=20, y=350)

        # add place button
        self.add_img = PhotoImage(file='..\Pic\\badd.png')
        self.add_place = tk.Button(self, image=self.add_img, borderwidth=0, background='black'
                                   , command=lambda: self.add_place_on_click(controller))
        self.add_place.place(bordermode=OUTSIDE, x=20, y=400)

        # go back button
        self.go_back_img = PhotoImage(file='..\Pic\\bgoback.png')
        back = tk.Button(self, image=self.go_back_img, borderwidth=0, background='black'
                         , command=lambda: self.go_back_on_click(controller))
        back.place(bordermode=OUTSIDE, x=20, y=450)

    def nature_check_box_on_click(self, controller):
        print(self.entry.get())
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
        if self.nature_check_var.get():
            print("religion is checked")
        else:
            print("religion not checked")

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

    def add_place_on_click(self, controller):
        if app.AddPlacePage not in controller.frames:
            controller.add_frame(app.AddPlacePage)
        controller.show_frame(app.AddPlacePage)

    def go_back_on_click(self, controller):
        # self.clean_entrys()
        if up.UserPage in controller.frames:
            controller.remove_frame(up.UserPage)
        controller.add_frame(up.UserPage)
        controller.show_frame(up.UserPage)

    def search_data_on_click(self, controller):
        # self.clean_entrys()
        print("loading....")
