from tkinter import *
import tkinter as tk
from View import SearchPage as sp
from View import StartPage as st
from Controller import UserController as uc

FONT_OUTPUT = ("Ariel", 10)


class UserPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.background()
        self.input_output()
        self.buttons(controller)


    def background(self):

        self.img = tk.PhotoImage(file='..\Pic\\userpagePic1.png')
        panel = tk.Label(self, image=self.img)
        panel.place(bordermode=OUTSIDE)


    def input_output(self):

        user = uc.UserController(st.username).get_user()

        str1 = 'First Name: ' + user.first_name
        first_namel = tk.Label(self, text=str1, bg='black', bd=0, fg='blue', font=FONT_OUTPUT)
        first_namel.place(bordermode=OUTSIDE, x=50, y=225)

        str2 = 'Last Name: ' + user.last_name
        last_namel = tk.Label(self, text=str2, bg='black', bd=0, fg='blue', font=FONT_OUTPUT)
        last_namel.place(bordermode=OUTSIDE, x=50, y=255)

        str3 = 'Username: ' + user.username
        usernamel = tk.Label(self, text=str3, bg='black', bd=0, fg='blue', font=FONT_OUTPUT)
        usernamel.place(bordermode=OUTSIDE, x=50, y=285)

        str4 = 'Email: ' + user.email
        emaill = tk.Label(self, text=str4, bg='black', bd=0, fg='blue', font=FONT_OUTPUT)
        emaill.place(bordermode=OUTSIDE, x=50, y=315)


    def buttons(self, controller):

        self.search_img = PhotoImage(file='..\Pic\\bsearch.png')
        b1 = tk.Button(self, image=self.search_img, borderwidth=0, background='black'
                       , command=lambda: self.search_button(controller))
        b1.place(bordermode=OUTSIDE, x=65, y=370)

        self.logout_img = PhotoImage(file='..\Pic\\blogout.png')
        register = tk.Button(self, image=self.logout_img, borderwidth=0, background='black'
                             , command=lambda: self.log_out(controller))
        register.place(bordermode=OUTSIDE, x=65, y=430)

        self.hide_img = PhotoImage(file='..\Pic\\bhide.png')
        self.hide_listb = tk.Button(self, image=self.hide_img, borderwidth=0, background='black'
                                      , command=self.hide_list_box)
        self.hide_listb.place(bordermode=OUTSIDE, x=515, y=35)

        self.show_img = PhotoImage(file='..\Pic\\bshow.png')
        self.show_listb = tk.Button(self, image=self.show_img, borderwidth=0, background='black'
                                    , command=self.show_list_box)
        self.show_listb.place(bordermode=OUTSIDE, x=515, y=35)


    def search_button(self, controller):

        if sp.SearchPage not in controller.frames:
            controller.add_frame(sp.SearchPage)
        controller.show_frame(sp.SearchPage)


    def log_out(self, controller):

        st.password = ''
        st.username = ''
        st.registered = False
        controller.show_frame(st.StartPage)


    def show_list_box(self):

        # TO DO GET DATA FROM DATABASE
        self.show_listb.place_forget()

        self.listbox = Listbox(self, bg='black', activestyle='dotbox',
                          font="Helvetica", fg="yellow")
        self.listbox.place(bordermode=OUTSIDE, x=320, y=100, height=350, width=400)
        scrollbar = Scrollbar(self.listbox, orient="vertical")
        scrollbar.config(command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=scrollbar.set)

        self.hide_listb.place(bordermode=OUTSIDE, x=515, y=35)


    def hide_list_box(self):

        self.hide_listb.place_forget()
        self.listbox.place_forget()
        self.show_listb.place(bordermode=OUTSIDE, x=515, y=35)

