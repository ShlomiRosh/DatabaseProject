from tkinter import *
import tkinter as tk


class Category:
    def __init__(self, controller, frame, name_code):
        self.check_var = tk.IntVar()
        self.name = name_code[1]
        self.code = name_code[0]
        self.parent_frame = frame
        self.check_button = Checkbutton(self.parent_frame, text=self.name, onvalue=1, offvalue=0, bg='grey', fg='blue',
                                        command=lambda: self.on_click(controller),
                                        variable=self.check_var)

    def on_click(self, controller):
        if self.check_var.get():
            print(self.name + " is checked")
        else:
            print(self.name + " not checked")
