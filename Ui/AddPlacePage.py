from tkinter import *
import tkinter as tk
from tkinter import ttk
from Ui import SearchPage as sep
from Core import AddPlaceController as apc
from Core import Entities as e
from Ui import OverViewButtons as ovb

FONT_OUTPUT = ("Ariel", 10, "underline")
FONT_TY = ("Ariel", 15, "bold")

# This class is responsible for displaying the Add Place page.
class AddPlacePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.go_back_img = PhotoImage(file='..\Pic\\bgoback.png')
        self.add_img = PhotoImage(file='..\Pic\\badd.png')
        self.img = tk.PhotoImage(file='..\Pic\\addPlace1.png')
        self.invalid = None
        # In these functions I will create & place all of the components
        # in the appropriate places, and run logic according to the user's requirements.
        self.background()
        # Init vars of input_output
        self.places_namee, self.addresse, self.latitudee, self.longitudee, self.linke \
            , self.descriptione, self.sub_cut = self.input_output()
        self.buttons(controller)


    def background(self):
        panel = tk.Label(self, image=self.img)
        panel.place(bordermode=OUTSIDE)


    def input_output(self):
        places_namel = tk.Label(self, text='Place Name:', bg='white', bd=0, fg='blue', font=FONT_OUTPUT)
        places_namel.place(bordermode=OUTSIDE, x=30, y=30)
        places_namee = Entry(self, bg='#fdeca6', fg='blue', bd=0)
        places_namee.place(bordermode=OUTSIDE, x=30, y=50, width=200, height=25)

        addressl = tk.Label(self, text='Place Address:', bg='white', bd=0, fg='blue', font=FONT_OUTPUT)
        addressl.place(bordermode=OUTSIDE, x=30, y=80)
        addresse = Entry(self, bg='#fdeca6', fg='blue', bd=0)
        addresse.place(bordermode=OUTSIDE, x=30, y=100, width=200, height=25)

        latitudel = tk.Label(self, text='Place Latitude:', bg='white', bd=0, fg='blue', font=FONT_OUTPUT)
        latitudel.place(bordermode=OUTSIDE, x=270, y=30)
        latitudee = Entry(self, bg='#fdeca6', fg='blue', bd=0)
        latitudee.place(bordermode=OUTSIDE, x=270, y=50, width=200, height=25)

        longitudel = tk.Label(self, text='Place Longitude:', bg='white', bd=0, fg='blue', font=FONT_OUTPUT)
        longitudel.place(bordermode=OUTSIDE, x=270, y=80)
        longitudee = Entry(self, bg='#fdeca6', fg='blue', bd=0)
        longitudee.place(bordermode=OUTSIDE, x=270, y=100, width=200, height=25)

        linkl = tk.Label(self, text='Link (Optional):', bg='white', bd=0, fg='blue', font=FONT_OUTPUT)
        linkl.place(bordermode=OUTSIDE, x=510, y=30)
        linke = Entry(self, bg='#fdeca6', fg='blue', bd=0)
        linke.place(bordermode=OUTSIDE, x=510, y=50, width=200, height=25)

        descriptionl = tk.Label(self, text='Description (Optional):', bg='white', bd=0, fg='blue', font=FONT_OUTPUT)
        descriptionl.place(bordermode=OUTSIDE, x=510, y=80)
        descriptione = Entry(self, bg='#fdeca6', fg='blue', bd=0)
        descriptione.place(bordermode=OUTSIDE, x=510, y=100, width=200, height=25)

        sub_catl = tk.Label(self, text='Choose Category:', bg='white', bd=0, fg='blue', font=FONT_OUTPUT)
        sub_catl.place(bordermode=OUTSIDE, x=30, y=130)
        sub_cat = ttk.Combobox(self, values=list(e.get_sub_category_dict().values()))
        sub_cat.place(bordermode=OUTSIDE, x=30, y=150, width=200, height=25)
        return places_namee, addresse, latitudee, longitudee, linke, descriptione, sub_cat


    def buttons(self, controller):
        add = tk.Button(self, image=self.add_img, borderwidth=0, background='black'
                          , command = lambda: self.add_button(controller))
        add.place(bordermode=OUTSIDE, x=535, y=150)
        back = tk.Button(self, image=self.go_back_img, borderwidth=0, background='white'
                             , command=lambda: self.go_back_button(controller))
        back.place(bordermode=OUTSIDE, x=20, y=450)


    # Check the place the user has entered whether it already exists in the system or not, display
    # appropriate messages. Contact the controller who will add the place if it is really new and thank the user.
    def add_button(self, controller):
        if self.invalid is not None:
            self.invalid.destroy()
        pe = apc.place_exists(self.places_namee.get(), self.addresse.get())
        if pe == 'Error Connection':
            self.invalid = ovb.create_msg(self, 575, 200, 'Error occurred while\n''accessing database.')
        elif pe:
            self.invalid = ovb.create_msg(self, 575, 200, 'Place is already exists.\n')
        elif len(self.places_namee.get()) == 0:
            self.invalid = ovb.create_msg(self, 575, 200, 'Places Name cannot be empty.\n')
        elif len(self.addresse.get()) == 0:
            self.invalid = ovb.create_msg(self, 575, 200, 'Address cannot be empty.\n')
        elif len(self.latitudee.get()) == 0:
            self.invalid = ovb.create_msg(self, 575, 200, 'Latitude cannot be empty.\n')
        elif len(self.longitudee.get()) == 0:
            self.invalid = ovb.create_msg(self, 575, 200, 'Longitude cannot be empty.\n')
        elif len(self.sub_cut.get()) == 0:
            self.invalid = ovb.create_msg(self, 575, 200, 'Category cannot be empty.\n')
        else:
            ip = apc.insert_place(self.places_namee.get(), self.addresse.get(), float(self.longitudee.get()),
                                  float(self.latitudee.get()), self.descriptione.get(), self.linke.get(),
                                  self.sub_cut.get(), sep.location_id)
            if ip == 'Inserted':
                msg = 'The place was added successfully,\n''thanks for the cooperation.'
                self.clean_entrys()
            else:
                msg = 'Error occurred while\n''accessing database.'
            thanks = tk.Label(self, text=msg, bg='white', bd=0, fg='blue', font=FONT_TY)
            thanks.place(bordermode=OUTSIDE, x=35, y=180)


    def go_back_button(self, controller):
        self.clean_entrys()
        controller.manage_frame(sep.SearchPage)


    def clean_entrys(self):
        try:
            self.places_namee.delete(0, 'end')
            self.addresse.delete(0, 'end')
            self.latitudee.delete(0, 'end')
            self.longitudee.delete(0, 'end')
            self.linke.delete(0, 'end')
            self.descriptione.delete(0, 'end')
            self.invalid.destroy()
        except:
            pass





