from tkinter import *
import tkinter as tk
from tkinter import ttk
from View import SearchPage as sep
from Controller import AddPlaceController as apc
from View import OverViewButtons as ovb

FONT_OUTPUT = ("Ariel", 10, "underline")
FONT_TY = ("Ariel", 15, "bold")
stop = True

class AddPlacePage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.background()
        self.input_output()
        self.buttons(controller)


    def background(self):

        self.img = tk.PhotoImage(file='..\Pic\\addPlace1.png')
        panel = tk.Label(self, image=self.img)
        panel.place(bordermode=OUTSIDE)


    def input_output(self):

        places_namel = tk.Label(self, text='Place Name:', bg='white', bd=0, fg='blue', font=FONT_OUTPUT)
        places_namel.place(bordermode=OUTSIDE, x=30, y=30)
        self.places_namee = Entry(self, bg='#fdeca6', fg='blue', bd=0)
        self.places_namee.place(bordermode=OUTSIDE, x=30, y=50, width=200, height=25)

        addressl = tk.Label(self, text='Place Address:', bg='white', bd=0, fg='blue', font=FONT_OUTPUT)
        addressl.place(bordermode=OUTSIDE, x=30, y=80)
        self.addresse = Entry(self, bg='#fdeca6', fg='blue', bd=0)
        self.addresse.place(bordermode=OUTSIDE, x=30, y=100, width=200, height=25)

        latitudel = tk.Label(self, text='Place Latitude:', bg='white', bd=0, fg='blue', font=FONT_OUTPUT)
        latitudel.place(bordermode=OUTSIDE, x=270, y=30)
        self.latitudee = Entry(self, bg='#fdeca6', fg='blue', bd=0)
        self.latitudee.place(bordermode=OUTSIDE, x=270, y=50, width=200, height=25)

        longitudel = tk.Label(self, text='Place Longitude:', bg='white', bd=0, fg='blue', font=FONT_OUTPUT)
        longitudel.place(bordermode=OUTSIDE, x=270, y=80)
        self.longitudee = Entry(self, bg='#fdeca6', fg='blue', bd=0)
        self.longitudee.place(bordermode=OUTSIDE, x=270, y=100, width=200, height=25)

        linkl = tk.Label(self, text='Link (Optional):', bg='white', bd=0, fg='blue', font=FONT_OUTPUT)
        linkl.place(bordermode=OUTSIDE, x=510, y=30)
        self.linke = Entry(self, bg='#fdeca6', fg='blue', bd=0)
        self.linke.place(bordermode=OUTSIDE, x=510, y=50, width=200, height=25)

        descriptionl = tk.Label(self, text='Description (Optional):', bg='white', bd=0, fg='blue', font=FONT_OUTPUT)
        descriptionl.place(bordermode=OUTSIDE, x=510, y=80)
        self.descriptione = Entry(self, bg='#fdeca6', fg='blue', bd=0)
        self.descriptione.place(bordermode=OUTSIDE, x=510, y=100, width=200, height=25)


    def buttons(self, controller):

        self.add_img = PhotoImage(file='..\Pic\\badd.png')
        add = tk.Button(self, image=self.add_img, borderwidth=0, background='black'
                          , command = lambda: self.add_button(controller))
        add.place(bordermode=OUTSIDE, x=535, y=150)

        self.go_back_img = PhotoImage(file='..\Pic\\bgoback.png')
        back = tk.Button(self, image=self.go_back_img, borderwidth=0, background='white'
                             , command=lambda: self.go_back_button(controller))
        back.place(bordermode=OUTSIDE, x=20, y=450)


    def add_button(self, controller):

        try:
            self.invalid.destroy()
        except:
            pass

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
            self.invalid = ovb.create_msg(self, 575, 200, 'longitude cannot be empty.\n')
        else:
            ip = apc.insert_place(self.places_namee.get(), self.addresse.get(), float(self.longitudee.get()),
                                  float(self.latitudee.get()), self.descriptione.get(), self.linke.get(),
                                  sep.sub_cutegory, sep.location_id)
            if ip == 'Inserted':
                msg = 'The place was added successfully,\n''thanks for the cooperation.'
                thanks = tk.Label(self, text=msg, bg='white', bd=0, fg='blue', font=FONT_TY)
                thanks.place(bordermode=OUTSIDE, x=40, y=150)
                self.clean_entrys()
            #self.go_back_button(controller)


    def go_back_button(self, controller):

        self.clean_entrys()
        if sep.SearchPage in controller.frames:
            controller.remove_frame(sep.SearchPage)
        controller.add_frame(sep.SearchPage)
        controller.show_frame(sep.SearchPage)


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

    # def anim(self):
    #
    #     animations = ['|', '/', '-', '\\',]
    #     i = 0
    #     cal = tk.Label(self, text=animations[0], font=FONT_TY, fg='blue')
    #     cal.place(bordermode=OUTSIDE, x=550, y=170)
    #     while stop:
    #         cal.destroy()
    #         time.sleep(1)
    #         cal = tk.Label(self, text=animations[(i)%4], font=FONT_TY, fg='blue')
    #         cal.place(bordermode=OUTSIDE, x=550, y=170)




