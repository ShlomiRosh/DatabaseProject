from tkinter import *
import tkinter as tk
from View import SearchPage as sp
from View import StartPage as st
from View import ResultPage as rp
from Controller import UserController as uc
from View import OverViewButtons as ovb

FONT_OUTPUT = ("Ariel", 10)
FONT_LIST = ("Ariel", 10, "bold", "underline")
place_id = None

# This class is responsible for displaying the user page.
class UserPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.showp_img = PhotoImage(file='..\Pic\\binfo.png')
        self.remove_img = PhotoImage(file='..\Pic\\bremove.png')
        self.show_img = PhotoImage(file='..\Pic\\bshow.png')
        self.hide_img = PhotoImage(file='..\Pic\\bhide.png')
        self.logout_img = PhotoImage(file='..\Pic\\blogout.png')
        self.search_img = PhotoImage(file='..\Pic\\bsearch.png')
        self.img = tk.PhotoImage(file='..\Pic\\userpagePic2.png')
        # Here I declare the buttons, the widgets that will be on the page,
        # later in the corresponding functions I will initialize them.
        self.invalid, self.listbox, self.remove_itemb\
        , self.information_itemb = None, None, None, None
        # In these functions I will create & place all of the components
        # in the appropriate places, and run logic according to the user's requirements.
        self.background()
        self.input_output()
        self.hide_listb, self.show_listb = self.buttons(controller)


    def background(self):
        panel = tk.Label(self, image=self.img)
        panel.place(bordermode=OUTSIDE)


    def input_output(self):
        # Check if we were able to extract the appropriate data from the data base
        # to display for the user, otherwise the user will be notified of a connection error.
        user = uc.UserController(st.username).get_user()
        if user == 'Error Connection':
            ovb.create_msg(self, 35, 230, 'Error occurred while\n''accessing database.')
        else:
            str1 = 'First Name: ' + user.first_name
            first_namel = tk.Label(self, text=str1, bg='black', bd=0, fg='yellow', font=FONT_OUTPUT)
            first_namel.place(bordermode=OUTSIDE, x=35, y=230)

            str2 = 'Last Name: ' + user.last_name
            last_namel = tk.Label(self, text=str2, bg='black', bd=0, fg='yellow', font=FONT_OUTPUT)
            last_namel.place(bordermode=OUTSIDE, x=35, y=260)

            str3 = 'Username: ' + user.username
            usernamel = tk.Label(self, text=str3, bg='black', bd=0, fg='yellow', font=FONT_OUTPUT)
            usernamel.place(bordermode=OUTSIDE, x=35, y=290)

            str4 = 'Email: ' + user.email
            emaill = tk.Label(self, text=str4, bg='black', bd=0, fg='yellow', font=FONT_OUTPUT)
            emaill.place(bordermode=OUTSIDE, x=35, y=320)


    def buttons(self, controller):
        search_b = tk.Button(self, image=self.search_img, borderwidth=0, background='black'
                       , command=lambda: self.search_button(controller))
        search_b.place(bordermode=OUTSIDE, x=55, y=365)
        logout_b = tk.Button(self, image=self.logout_img, borderwidth=0, background='black'
                             , command=lambda: self.log_out(controller))
        logout_b.place(bordermode=OUTSIDE, x=55, y=425)
        hide_listb = tk.Button(self, image=self.hide_img, borderwidth=0, background='black'
                                      , command=self.hide_list_box)
        hide_listb.place(bordermode=OUTSIDE, x=515, y=35)
        show_listb = tk.Button(self, image=self.show_img, borderwidth=0, background='black'
                                    , command=lambda : self.show_list_box(controller))
        show_listb.place(bordermode=OUTSIDE, x=515, y=35)
        return hide_listb, show_listb


    def search_button(self, controller):
        # If the user wants to go to the search page, we will move it.
        controller.manage_frame(sp.SearchPage)


    def log_out(self, controller):
        # If the user wants to log out, we lod him out and send him back to the start page.
        st.password = ''
        st.username = ''
        st.registered = False
        controller.show_frame(st.StartPage)


    def show_list_box(self, controller):
        # If the user wants to get his list of favorite places,
        # we will create a window that will show him them, the buttons that control the window,
        # we will turn to the controller to get the appropriate information for the window.
        self.show_listb.place_forget()
        self.create_listbox()
        self.create_listbox_buttons(controller)
        self.insert_data_to_listbox()
        self.hide_listb.place(bordermode=OUTSIDE, x=515, y=35)


    def hide_list_box(self):
        if self.invalid is not None:
            self.invalid.place_forget()
        self.hide_listb.place_forget()
        self.listbox.place_forget()
        self.information_itemb.place_forget()
        self.remove_itemb.place_forget()
        self.show_listb.place(bordermode=OUTSIDE, x=515, y=35)


    def create_listbox(self):
        self.listbox = Listbox(self, bg='black', activestyle='dotbox',
                               font=FONT_LIST, fg="yellow")
        self.listbox.place(bordermode=OUTSIDE, x=320, y=100, height=300, width=400)
        scrollbar = Scrollbar(self.listbox, orient="vertical")
        scrollbar.config(command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=scrollbar.set)


    def create_listbox_buttons(self, controller):
        self.remove_itemb = tk.Button(self, image=self.remove_img, borderwidth=0, background='black'
                                      , command=self.remove_item)
        self.remove_itemb.place(bordermode=OUTSIDE, x=525, y=410)
        self.information_itemb = tk.Button(self, image=self.showp_img, borderwidth=0, background='black'
                                      , command=lambda : self.show_info(controller))
        self.information_itemb.place(bordermode=OUTSIDE, x=310, y=410)


    def insert_data_to_listbox(self):
        # Obtain the information from the controller, if you were able to view it otherwise report an error to the user.
        places = uc.UserController(st.username).get_user_places()
        if places == 'Error Connection':
            ovb.create_msg(self, 515, 30, 'Error occurred while\n''accessing database.')
        else:
            for item in places:
                self.listbox.insert(END, 'Place ID:' + ' ' + str(item.place_id) + ' '
                                    + item.place_name.upper())


    def remove_item(self):
        # If user has requested to remove a place from his or her favorites list, contact the controller to do so.
        place_to_remove = self.listbox.get(ANCHOR).split(' ')[2].strip() if self.listbox.get(ANCHOR) != '' else None
        if place_to_remove is None:
            self.invalid = ovb.create_msg(self, 525, 455, 'Please select place\n''from the list box.')
        else:
            res = uc.UserController(st.username).remove_place(int(place_to_remove))
            if res == 'Deleted':
                self.listbox.delete(ANCHOR)
            else:
                self.invalid = ovb.create_msg(self, 525, 455, 'Error occurred while\n''accessing database.')


    def show_info(self, controller):
        # the user wanted to see data about a place in his list, save the place's ID and move it to the appropriate page.
        global place_id
        place_id = int(self.listbox.get(ANCHOR).split(' ')[2].strip()) if self.listbox.get(ANCHOR) != '' else None
        if place_id is None:
            self.invalid = ovb.create_msg(self, 310, 455, 'Please select place\n''from the list box.')
        else:
            controller.manage_frame(rp.ResultPage)
