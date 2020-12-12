from tkinter import *
import tkinter as tk
from View import RegisterPage as rp
from View import SearchPage as sep
from View import UserPage as up
from Controller import LoginCotroller as lc

FONT_OUTPUT = ("Ariel", 10)
registered = False
username = ''
password = ''

class AddPlacePage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.background()
        self.input_output()
        self.buttons(controller)


    def background(self):

        self.img = tk.PhotoImage(file='..\Pic\\addPlace.png')
        panel = tk.Label(self, image=self.img)
        panel.place(bordermode=OUTSIDE)

        canvas = tk.Canvas(self, height=500, width=750)
        canvas.pack()
        bg_label = canvas.create_image((0, 0), image=self.img, anchor=tk.N + tk.W)

        label_msg = canvas.create_text((410, 120), text="Earth Hour Countdown:", font="MSGothic 50 bold",
                                       fill="#652828")

    def input_output(self):
        pass
        # namel = tk.Label(self, text='User Name:', bg='black', bd=0, fg='yellow', font=FONT_OUTPUT)
        # namel.place(bordermode=OUTSIDE, x=305, y=15)
        # self.ename = Entry(self)
        # self.ename.place(bordermode=OUTSIDE, x=305, y=35, width=150, height=25)
        #
        # passwordl = tk.Label(self, text='Password:', bg='black', bd=0, fg='yellow', font=FONT_OUTPUT)
        # passwordl.place(bordermode=OUTSIDE, x=465, y=15)
        # self.epassword = Entry(self)
        # self.epassword.place(bordermode=OUTSIDE, x=465, y=35, width=150, height=25)


    def buttons(self, controller):
        pass
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
        # register = tk.Button(self, image=self.register_img, borderwidth=0, background='black'
        #                      , command=lambda: self.register_button(controller))
        # register.place(bordermode=OUTSIDE, x=500, y=350)
        #
        # self.guest_img = PhotoImage(file='..\Pic\\bguest.png')
        # guest = tk.Button(self, image=self.guest_img, borderwidth=0, background='black'
        #                   , command=lambda: self.as_guest_button(controller))
        # guest.place(bordermode=OUTSIDE, x=500, y=410)


    def as_guest_button(self, controller):
        pass
        # if sep.SearchPage not in controller.frames:
        #     controller.add_frame(sep.SearchPage)
        # controller.show_frame(sep.SearchPage)


    def register_button(self, controller):
        pass
        # if rp.RegisterPage not in controller.frames:
        #     controller.add_frame(rp.RegisterPage)
        # controller.show_frame(rp.RegisterPage)


    def login_button(self, controller):
        pass
        # if len(self.ename.get()) < 6 or len(self.epassword.get()) < 6 \
        #         or not lc.LoginController(self.ename.get(), self.epassword.get()).has_user():
        #
        #     self.invalid = tk.Label(self, text='Invalid username or password.'
        #                        , bg='black', bd=0, fg='red', font=FONT_OUTPUT)
        #     self.invalid.place(bordermode=OUTSIDE, x=305, y=65)
        #
        # else:
        #
        #     global registered, username, password
        #     registered = True
        #     username = self.ename.get()
        #     password = self.epassword.get()
        #     self.clean_entrys()
        #
        #     if up.UserPage in controller.frames:
        #         controller.remove_frame(up.UserPage)
        #     controller.add_frame(up.UserPage)
        #     controller.show_frame(up.UserPage)


    def clean_entrys(self):
        pass
        # self.ename.delete(0, 'end')
        # self.epassword.delete(0, 'end')
        # try:
        #     self.invalid.destroy()
        # except:
        #     pass




