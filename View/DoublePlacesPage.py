from tkinter import *
import tkinter as tk
import time
from View import StartPage as sp
from View import UserPage as up
from Controller import DoublePlacesController as dpc
from Controller import ResultController as rc
import asyncio
from View import OverViewButtons as ovb

FONT_LIST = ("Ariel", 10, "bold", "underline")
FONT_OUTPUT = ("Ariel", 15, "bold")


# This class is responsible for displaying the start page.
class DoublePlacesPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.addf_img = PhotoImage(file='..\Pic\\badd.png')
        self.goback_img = PhotoImage(file='..\Pic\\bgoback.png')
        self.img = tk.PhotoImage(file='..\Pic\\dpback.png')
        self.invalid = None
        # In these functions I will create & place all of the components
        # in the appropriate places, and run logic according to the user's requirements.
        self.canvas = self.background()
        self.listbox = self.input_output()
        self.buttons(controller)


    def background(self):
        # create the canvas, size in pixels
        canvas = tk.Canvas(self, width=1000, height=1000)
        canvas.place(bordermode=INSIDE, x=0, y=0)
        canvas.create_image(0, 0, image=self.img, anchor=tk.NW)
        return canvas


    def input_output(self):
        self.canvas.create_text(535, 45, fill="red", font=FONT_OUTPUT,
                                text="- Please wait it may take a few moments.")

        self.canvas.create_text(535, 65, fill="red", font=FONT_OUTPUT,
                                text="- Please wait it may take a few moments.")
        self.canvas.create_text(535, 95, fill="red", font=FONT_OUTPUT,
                                text="- Please wait it may take a few moments.")

        #data1 = asyncio.run(dpc.DoublePlacesController(sp.username).get_neighbors())
        data = dpc.DoublePlacesController(sp.username).get_neighbors()
        listbox = Listbox(self,selectmode=MULTIPLE, activestyle='dotbox',
                               font=FONT_LIST)
        listbox.place(bordermode=OUTSIDE, x=30, y=30, height=400, width=310)

        # Fill the listbox with items
        for item in data:
            listbox.insert(END, 'Place ID:' + ' ' + str(item.place_id) + ' '
                                + item.place_name.upper())
        return listbox



    def buttons(self, controller):
        add = tk.Button(self, image=self.addf_img, borderwidth=0, background='black'
                          , command = lambda: self.add_button(controller))
        add.place(bordermode=OUTSIDE, x=30, y=450)
        go_back = tk.Button(self, image=self.goback_img, borderwidth=0, background='black'
                             , command=lambda: self.goback_button(controller))
        go_back.place(bordermode=OUTSIDE, x=190, y=450)


    def goback_button(self, controller):
        controller.manage_frame(up.UserPage)


    def add_button(self, controller):
        id_list = []
        seleccion = self.listbox.curselection()
        for i in seleccion:
            entrada = self.listbox.get(i)
            id_list.append(int(entrada.split(' ')[2].strip()))
        if not id_list:
            self.invalid = ovb.create_msg(self, 30, 430, 'Please select places\n''from the list box.')
        else:
            add = rc.ResultController().add_places_to_user_places(id_list, sp.username)
            if add == 'Error':
                self.invalid = ovb.create_msg(self, 30, 430, 'Error occurred while\n''accessing database.')
            else:
                controller.manage_frame(up.UserPage)
