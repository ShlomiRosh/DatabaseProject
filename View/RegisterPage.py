from tkinter import *
import tkinter as tk
import re
import random
import string
from View import StartPage as st
from View import OverViewButtons as ovb
from View import UserPage as up
from Sql import SqlConnection as sc

FONT_CREATE = ("Ariel", 16, "bold")
FONT_OUTPUT = ("Ariel", 9)
FONT_NOTE = ("Ariel", 10, "bold", "underline")
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

class RegisterPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.background()
        self.input_output()
        self.buttons(controller)

    def background(self):

        self.img = tk.PhotoImage(file='..\Pic\\‏‏registerPic1.png')
        panel = tk.Label(self, image=self.img)
        panel.place(bordermode=OUTSIDE)

        create_account = tk.Label(self, text='Create Your Account:', bg='black', bd=0, fg='white', font=FONT_CREATE)
        create_account.place(bordermode=OUTSIDE, x=450, y=15)
        ###### TO CHECK
        num_of_registered_users = sc.total_users()
        total = tk.Label(self, text='Total of ' + str(num_of_registered_users) + ' registered users'
                         , bg='black', bd=0, fg='white', font=FONT_OUTPUT)
        total.place(bordermode=OUTSIDE, x=480, y=40)


    def input_output(self):

        note = tk.Label(self, text='Note here!', bg='black', bd=0, fg='blue', font=FONT_NOTE)
        note.place(bordermode=OUTSIDE, x=415, y=65)
        ovb.CreateToolTip(note, text='Username and password must be\n''at least 6 characters long.')

        namel = tk.Label(self, text='User Name:', bg='black', bd=0, fg='white', font=FONT_OUTPUT)
        namel.place(bordermode=OUTSIDE, x=420, y=100)
        self.ename = Entry(self)
        self.ename.place(bordermode=OUTSIDE, x=510, y=95, width=200, height=25)

        passwordl = tk.Label(self, text='Password:', bg='black', bd=0, fg='white', font=FONT_OUTPUT)
        passwordl.place(bordermode=OUTSIDE, x=420, y=150)
        self.epassword = Entry(self)
        self.epassword.place(bordermode=OUTSIDE, x=510, y=145, width=200, height=25)

        first_namel = tk.Label(self, text='First Name:', bg='black', bd=0, fg='white', font=FONT_OUTPUT)
        first_namel.place(bordermode=OUTSIDE, x=420, y=200)
        self.efirst_name = Entry(self)
        self.efirst_name.place(bordermode=OUTSIDE, x=510, y=195, width=200, height=25)

        last_namel = tk.Label(self, text='Last Name:', bg='black', bd=0, fg='white', font=FONT_OUTPUT)
        last_namel.place(bordermode=OUTSIDE, x=420, y=250)
        self.elast_name = Entry(self)
        self.elast_name.place(bordermode=OUTSIDE, x=510, y=245, width=200, height=25)

        emaill = tk.Label(self, text='Email:', bg='black', bd=0, fg='white', font=FONT_OUTPUT)
        emaill.place(bordermode=OUTSIDE, x=420, y=300)
        self.eemail = Entry(self)
        self.eemail.place(bordermode=OUTSIDE, x=510, y=295, width=200, height=25)


    def buttons(self, controller):

        self.register_img = PhotoImage(file='..\Pic\\bregister.png')
        b1 = tk.Button(self, image=self.register_img, borderwidth=0, background='black'
                       , command=lambda: self.register_button(controller))
        b1.place(bordermode=OUTSIDE, x=470, y=350)

        self.home_img = PhotoImage(file='..\Pic\\bhome.png')
        register = tk.Button(self, image=self.home_img, borderwidth=0, background='black'
                             , command=lambda: controller.show_frame(st.StartPage))
        register.place(bordermode=OUTSIDE, x=470, y=410)


    def register_button(self, controller):

        try:
            self.invalid.destroy()
        except:
            pass

        if len(self.ename.get()) < 6:
            self.invalid_notes(510, 120, 'Username must be at\n''least 6 characters long.')
        elif sc.is_exists_user(self.ename.get()):
            self.handle_existing_username()
        elif len(self.epassword.get()) < 6:
            self.invalid_notes(510, 170, 'Password must be at\n''least 6 characters long.')
        elif len(self.efirst_name.get()) == 0:
            self.invalid_notes(510, 220, 'First name cannot be empty.\n')
        elif len(self.elast_name.get()) == 0:
            self.invalid_notes(510, 270, 'Last name cannot be empty.\n')
        elif not re.search(regex, self.eemail.get()):
            self.invalid_notes(510, 320, 'Invalid email.\n')
        else:
            controller.show_frame(up.UserPage)


    def invalid_notes(self, p_x, p_y, message):

        self.invalid = tk.Label(self, text='Note here!'
                           , bg='black', bd=0, fg='red', font=FONT_NOTE)
        self.invalid.place(bordermode=OUTSIDE, x=p_x, y=p_y)
        ovb.CreateToolTip(self.invalid, text=message)


    def handle_existing_username(self):

        suggestion1 = suggestion2 = self.ename.get()

        while sc.is_exists_user(suggestion1):
            suggestion1 = suggestion1 + random.choice(string.ascii_letters)

        while sc.is_exists_user(suggestion2):
            suggestion2 = suggestion2 + str(random.randint(0, 9999))

        self.invalid_notes(510, 120, 'Username Taken try:\n' + suggestion1 + ' or ' + suggestion2)


# def tryd():
#     print(st.password + '   ' + st.username + '     ' + str(st.registered))