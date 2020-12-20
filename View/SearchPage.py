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
        self.buttons(controller)

    def background(self):
        pass
        self.img = tk.PhotoImage(file='..\Pic\\searchpagePic.png')
        panel = tk.Label(self, image=self.img)
        panel.place(bordermode=OUTSIDE)

    # self.configure(background='blue')

    def input(self):
        pass
        entry = acs.AutocompleteEntry(autocompleteList, self, listboxLength=8, width=50, matchesFunction=acs.matches)
        entry.place(bordermode=OUTSIDE, height=30, x=20, y=25)

    def buttons(self, controller):

        frame = tk.Frame(self)
        frame.place(bordermode=OUTSIDE, x=20, y=100, width=710, height=25)

        # main categories check buttons
        nature_check = Checkbutton(frame, text="Nature", onvalue=1, offvalue=0, bg='grey', fg='blue')
        financial_check = Checkbutton(frame, text="Financial", onvalue=1, offvalue=0, bg='grey', fg='blue')
        history_check = Checkbutton(frame, text="History", onvalue=1, offvalue=0, bg='grey', fg='blue')
        religion_check = Checkbutton(frame, text="Religion", onvalue=1, offvalue=0, bg='grey', fg='blue')
        commercial_check = Checkbutton(frame, text="Commercial", onvalue=1, offvalue=0, bg='grey', fg='blue')
        transportation_check = Checkbutton(frame, text="Transportation", onvalue=1, offvalue=0, bg='grey', fg='blue')
        fun_check = Checkbutton(frame, text="Fun", onvalue=1, offvalue=0, bg='grey', fg='blue')
        museums_check = Checkbutton(frame, text="Museums", onvalue=1, offvalue=0, bg='grey', fg='blue')
        nature_check.pack(side=LEFT, fill=BOTH, expand=True)
        financial_check.pack(side=LEFT, fill=BOTH, expand=True)
        history_check.pack(side=LEFT, fill=BOTH, expand=True)
        religion_check.pack(side=LEFT, fill=BOTH, expand=True)
        commercial_check.pack(side=LEFT, fill=BOTH, expand=True)
        transportation_check.pack(side=LEFT, fill=BOTH, expand=True)
        fun_check.pack(side=LEFT, fill=BOTH, expand=True)
        museums_check.pack(side=LEFT, fill=BOTH, expand=True)

        # search button
        self.search_img = PhotoImage(file='..\Pic\\bsearch.png')
        self.search_data = tk.Button(self, image=self.search_img, borderwidth=0, background='black'
                                     , command=lambda: self.search_data_button(controller))
        self.search_data.place(bordermode=OUTSIDE, x=20, y=350)

        # add place button
        self.add_img = PhotoImage(file='..\Pic\\badd.png')
        self.add_place = tk.Button(self, image=self.add_img, borderwidth=0, background='black'
                                   , command=lambda: self.add_place_button(controller))
        self.add_place.place(bordermode=OUTSIDE, x=20, y=400)

        # go back button
        self.go_back_img = PhotoImage(file='..\Pic\\bgoback.png')
        back = tk.Button(self, image=self.go_back_img, borderwidth=0, background='black'
                         , command=lambda: self.go_back_button(controller))
        back.place(bordermode=OUTSIDE, x=20, y=450)

    def add_place_button(self, controller):
        if app.AddPlacePage not in controller.frames:
            controller.add_frame(app.AddPlacePage)
        controller.show_frame(app.AddPlacePage)

    def go_back_button(self, controller):
        # self.clean_entrys()
        if up.UserPage in controller.frames:
            controller.remove_frame(up.UserPage)
        controller.add_frame(up.UserPage)
        controller.show_frame(up.UserPage)

    def search_data_button(self, controller):
        # self.clean_entrys()
        if up.UserPage in controller.frames:
            controller.remove_frame(up.UserPage)
        controller.add_frame(up.UserPage)
        controller.show_frame(up.UserPage)
