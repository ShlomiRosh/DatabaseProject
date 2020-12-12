from tkinter import *
import tkinter as tk
from View import AutocompleteSearch as acs
from View import AddPlacePage as app
from Controller import SearchController as sc

location_id = None
sub_cutegory = ''

#autocompleteList = sc.get_locations()
# arye
# דיךםצן dddddddddddddddd
# shalom ggh
class SearchPage(tk.Frame):

    def __init__(self, parent, controller):
        pass
        tk.Frame.__init__(self, parent)
        self.background()
        self.input()
        self.buttons(controller)


    def background(self):

        self.img = tk.PhotoImage(file='..\Pic\\searchpagePic1.png')
        panel = tk.Label(self, image=self.img)
        panel.place(bordermode=OUTSIDE)


    def input(self):
        pass
        #entry = acs.AutocompleteEntry(autocompleteList, self, listboxLength=8, width=50, matchesFunction=acs.matches)
        #entry.place(bordermode=OUTSIDE, height=30, x=25, y=25)


        # namel = tk.Label(self, text='User Name:', bg='black', bd=0, fg='blue', font=FONT_OUTPUT)
        # namel.place(bordermode=OUTSIDE, x=305, y=15)
        # self.ename = Entry(self)
        # self.ename.place(bordermode=OUTSIDE, x=305, y=35, width=150, height=25)
        #
        # passwordl = tk.Label(self, text='Password:', bg='black', bd=0, fg='blue', font=FONT_OUTPUT)
        # passwordl.place(bordermode=OUTSIDE, x=465, y=15)
        # self.epassword = Entry(self)
        # self.epassword.place(bordermode=OUTSIDE, x=465, y=35, width=150, height=25)


    def buttons(self, controller):
        C1 = Checkbutton(self, text="Music",
                         onvalue=1, offvalue=0, bg='grey', fg='blue')
        C1.place(bordermode=OUTSIDE, x=20, y=275)
        # self.b1_img = PhotoImage(file='..\Pic\\logo.png')
        # b1 = tk.Button(self, image=self.b1_img, borderwidth=0, background='black'
        #                 , command=lambda : controller.show_frame(StartPage))
        # b1.place(bordermode=OUTSIDE, x=20, y=20)
        #
        # self.login_img = PhotoImage(file='..\Pic\\blogin.png')
        # login = tk.Button(self, image=self.login_img, borderwidth=0, background='black'
        #                   , command = lambda: self.login_button(controller))
        # login.place(bordermode=OUTSIDE, x=625, y=30)
        #
        # self.register_img = PhotoImage(file='..\Pic\\bregister.png')
        # register = tk.Button(self, image=self.register_img, borderwidth=0, background='black')
        # register.place(bordermode=OUTSIDE, x=500, y=350)
        #
        # self.guest_img = PhotoImage(file='..\Pic\\bguest.png')
        # guest = tk.Button(self, image=self.guest_img, borderwidth=0, background='black')
        # guest.place(bordermode=OUTSIDE, x=500, y=410)
#####################################################################################################

        self.test = tk.Button(self, text='hi_test', borderwidth=0, background='yellow'
                              , command=lambda: self.test_only(controller))
        self.test.place(bordermode=OUTSIDE, x=300, y=80)

    def test_only(self, controller):
        if app.AddPlacePage not in controller.frames:
            controller.add_frame(app.AddPlacePage)
        controller.show_frame(app.AddPlacePage)

####################################################################### TEST ONLY

    def login_button(self, controller):

        # if len(self.ename.get()) < 6 or len(self.epassword.get()) < 6 \
        #         or not sql.has_record(self.ename.get(), self.epassword.get()):
        #
        #     invalid = tk.Label(self, text='Invalid username or password.'
        #                        , bg='black', bd=0, fg='red', font=FONT_OUTPUT)
        #     invalid.place(bordermode=OUTSIDE, x=305, y=65)
        #
        # else:
        #
        #     global registered, username, password
        #     registered = True
        #     username = self.ename.get()
        #     password = self.epassword.get()
        #     #controller.show_frame(sp.....)
        pass
