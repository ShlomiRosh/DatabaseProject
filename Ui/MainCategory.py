from tkinter import *
import tkinter as tk
from Ui.Category import Category
from Ui.SubCategory import SubCategory


class MainCategory(Category):
    def __init__(self, controller, frame, name, subs):
        Category.__init__(self, controller, frame, name)
        self.sub_categories_names_arr = subs
        self.sub_checks_arr = []
        self.sub_frame = tk.Frame(width="90", height="500")

    def initialize_sub_categories(self, controller):
        for sub_name_code_tuple in self.sub_categories_names_arr:
            new_sub = SubCategory(controller, self.sub_frame, sub_name_code_tuple)
            self.sub_checks_arr.append(new_sub)

    def on_click(self, controller):
        if self.check_var.get():
            print(self.name + " is checked")
            x_dictionary = {"Nature":20, "History":100, "Financial":180, "Museums":270, "Fun":360, "Transportation":430, "Commercial":550, "Religion":650}
            lv_x = x_dictionary[self.name]
            lv_y = 135
            self.sub_frame.place(bordermode=OUTSIDE, x=lv_x, y=lv_y)
            for sub_category in self.sub_checks_arr:
                sub_category.check_button.pack(side=BOTTOM, fill=BOTH, expand=True)
        else:
            print(self.name + " not checked")
            self.clear()

    def clear_sub_checks(self):
        self.sub_frame.place_forget()
        for sub_check in self.sub_checks_arr:
            sub_check.check_var.set(0)

    def clear_main_check(self):
        self.check_var.set(0)

    def clear(self):
        self.clear_sub_checks()
        self.clear_main_check()