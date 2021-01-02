from tkinter import *
import tkinter as tk
from View import SearchPage as sp
from Controller import ResultController as rc

FONT_NOTE = ("Ariel", 10, "bold", "underline")


class ResultPage(tk.Frame):

    def __init__(self, parent, controller):
        self.main_frame = tk.Frame.__init__(self, parent)
        self.background()
        self.buttons(controller)
        self.place_id = sp.place_id
        self.complete_place = rc.ResultController().get_place_all_recorde(self.place_id)
        print("place id from result page is: " + str(self.place_id))
        self.show_results()

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

    def show_results(self):
        self.results_frame = tk.Frame(self.main_frame, bg="RED", borderwidth=2)

        Grid.columnconfigure(self.results_frame, 0, weight=0)
        Grid.columnconfigure(self.results_frame, 1, weight=0)
        Grid.columnconfigure(self.results_frame, 2, weight=3)
        Grid.columnconfigure(self.results_frame, 3, weight=3)

        for y in range(4):
            Grid.rowconfigure(self.results_frame, y, weight=1)
        tk.Label(self.results_frame, text="Name: " + self.complete_place.place.place_name, borderwidth=1).grid(row=0, column=0, columnspan=4, sticky=N + S + E + W,
                                                                   padx=5, pady=5)
        tk.Label(self.results_frame, text="State:\n" + self.complete_place.state, borderwidth=1).grid(row=1, column=0, columnspan=1, sticky=N + S + E + W,
                                                                   padx=5, pady=5)
        tk.Label(self.results_frame, text="City:\n" + self.complete_place.city, borderwidth=1).grid(row=2, column=0, columnspan=1, sticky=N + S + E + W,
                                                                   padx=5, pady=5)
        tk.Label(self.results_frame, text="Adress:\n" + self.complete_place.place.address, borderwidth=1,
wraplength=300, justify="center").grid(row=3, column=0, columnspan=1, sticky=N + S + E + W,
                                                                   padx=5, pady=5)
        tk.Label(self.results_frame, text="Description:\n" + self.complete_place.place.description , borderwidth=1,
wraplength=300, justify="center").grid(row=1, column=1, columnspan=1, sticky=N + S + E + W,
                                                                   padx=5, pady=5)

        tk.Label(self.results_frame, text="Rank The Place", borderwidth=1).grid(row=2, column=1, columnspan=1, sticky=N + S + E + W,
                                                                   padx=5, pady=5)
        tk.Label(self.results_frame, text="Average Rank Of the Place", borderwidth=1).grid(row=3, column=1, columnspan=1, sticky=N + S + E + W,
                                                                   padx=5, pady=5)
        tk.Label(self.results_frame, text="MAP", borderwidth=1).grid(row=1, column=2, columnspan=2, rowspan=3,
                                                                     sticky=N + S + E + W, padx=5, pady=5)

        self.results_frame.place(bordermode=OUTSIDE, x=20, y=20, height=400, width=710)

    # ----------------------------------------------- click handlers --------------------------------------------------
    def go_back_on_click(self, controller):
        self.clear_page()
        # load next frame (user page)
        if sp.SearchPage in controller.frames:
            controller.remove_frame(sp.SearchPage)
        controller.add_frame(sp.SearchPage)
        controller.show_frame(sp.SearchPage)

    def clear_page(self):
        self.results_frame.place_forget()
