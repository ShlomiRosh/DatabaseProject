from tkinter import *
import tkinter as tk
from Ui import StartPage as sp
from Ui import UserPage as up
from Core import DoublePlacesController as dpc
from Core import ResultController as rc
from tkinter import ttk
from Ui import OverViewButtons as ovb
import threading

FONT_LIST = ("Ariel", 10, "bold", "underline")
FONT_OUTPUT = ("Ariel", 15, "bold")


# This class is responsible for displaying the DoublePlacesPage.
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
        self.listbox, self.progressbar = self.input_output()
        self.add, self.go_back = self.buttons(controller)


    def background(self):
        # create the canvas, size in pixels
        canvas = tk.Canvas(self, width=1000, height=1000)
        canvas.place(bordermode=INSIDE, x=0, y=0)
        canvas.create_image(0, 0, image=self.img, anchor=tk.NW)
        return canvas


    def input_output(self):
        listbox = Listbox(self,selectmode=MULTIPLE, activestyle='dotbox', font=FONT_LIST)
        pb = ttk.Progressbar(self, orient='horizontal', mode='indeterminate')
        pb.place(bordermode=OUTSIDE, x=415, y=410, height=30, width=250)
        pb.start()
        x = threading.Thread(target=self.thread_function)
        x.setDaemon(True)
        x.start()
        return listbox, pb

    
    def thread_function(self):
        data = dpc.DoublePlacesController(sp.username).get_neighbors()
        # Fill the listbox with items
        for item in data:
            self.listbox.insert(END, 'Place ID:' + ' ' + str(item.place_id) + ' '
                           + item.place_name.upper())
        self.listbox.place(bordermode=OUTSIDE, x=30, y=47, height=385, width=310)
        self.go_back.place(bordermode=OUTSIDE, x=190, y=450)
        self.add.place(bordermode=OUTSIDE, x=30, y=450)
        self.progressbar.destroy()


    def buttons(self, controller):
        add = tk.Button(self, image=self.addf_img, borderwidth=0, background='black'
                          , command = lambda: self.add_button(controller))
        go_back = tk.Button(self, image=self.goback_img, borderwidth=0, background='black'
                             , command=lambda: self.goback_button(controller))
        return add, go_back


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
