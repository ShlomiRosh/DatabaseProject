from tkinter import *
import tkinter as tk
from View import AutocompleteSearch as acs
from Sql import SqlConnection as sql

autocompleteList = ['Dora Lyons (7714)', 'Hannah Golden (6010)', 'Walker Burns (9390)', 'Dieter Pearson (6347)',
                        'Allen Sullivan (9781)', 'Warren Sullivan (3094)', 'Genevieve Mayo (8427)',
                        'Igor Conner (4740)', 'Ulysses Shepherd (8116)', 'Imogene Bullock (6736)',
                        'Dominique Sanchez (949)', 'Sean Robinson (3784)', 'Diana Greer (2385)',
                        'Arsenio Conrad (2891)', 'Sophia Rowland (5713)', 'Garrett Lindsay (5760)', 'Lacy Henry (4350)',
                        'Tanek Conley (9054)', 'Octavia Michael (5040)', 'Kimberly Chan (1989)',
                        'Melodie Wooten (7753)', 'Winter Beard (3896)', 'Callum Schultz (7762)',
                        'Prescott Silva (3736)', 'Adena Crane (6684)', 'Ocean Schroeder (2354)', 'Aspen Blevins (8588)',
                        'Allegra Gould (7323)', 'Penelope Aguirre (7639)', 'Deanna Norman (1963)',
                        'Herman Mcintosh (1776)', 'August Hansen (547)', 'Oscar Sanford (2333)', 'Guy Vincent (1656)',
                        'Indigo Frye (3236)', 'Angelica Vargas (1697)', 'Bevis Blair (4354)', 'Trevor Wilkinson (7067)',
                        'Kameko Lloyd (2660)', 'Giselle Gaines (9103)', 'Phyllis Bowers (6661)', 'Patrick Rowe (2615)',
                        'Cheyenne Manning (1743)', 'Jolie Carney (6741)', 'Joel Faulkner (6224)',
                        'Anika Bennett (9298)', 'Clayton Cherry (3687)', 'Shellie Stevenson (6100)',
                        'Marah Odonnell (3115)', 'Quintessa Wallace (5241)', 'Jayme Ramsey (8337)',
                        'Kyle Collier (8284)', 'Jameson Doyle (9258)', 'Rigel Blake (2124)', 'Joan Smith (3633)',
                        'Autumn Osborne (5180)', 'Renee Randolph (3100)', 'Fallon England (6976)',
                        'Fallon Jefferson (6807)', 'Kevyn Koch (9429)', 'Paki Mckay (504)', 'Connor Pitts (1966)',
                        'Rebecca Coffey (4975)', 'Jordan Morrow (1772)', 'Teegan Snider (5808)',
                        'Tatyana Cunningham (7691)', 'Owen Holloway (6814)', 'Desiree Delaney (272)',
                        'Armand Snider (8511)', 'Wallace Molina (4302)', 'Amela Walker (1637)', 'Denton Tillman (201)',
                        'Bruno Acevedo (7684)', 'Slade Hebert (5945)', 'Elmo Watkins (9282)', 'Oleg Copeland (8013)',
                        'Vladimir Taylor (3846)', 'Sierra Coffey (7052)', 'Holmes Scott (8907)',
                        'Evelyn Charles (8528)', 'Steel Cooke (5173)', 'Roth Barrett (7977)', 'Justina Slater (3865)',
                        'Mara Andrews (3113)', 'Ulla Skinner (9342)', 'Reece Lawrence (6074)', 'Violet Clay (6516)',
                        'Ainsley Mcintyre (6610)', 'Chanda Pugh (9853)', 'Brody Rosales (2662)', 'Serena Rivas (7156)',
                        'Henry Lang (4439)', 'Clark Olson (636)', 'Tashya Cotton (5795)', 'Kim Matthews (2774)',
                        'Leilani Good (5360)', 'Deirdre Lindsey (5829)', 'Macy Fields (268)', 'Daniel Parrish (1166)',
                        'Talon Winters (8469)']

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

        entry = acs.AutocompleteEntry(autocompleteList, self, listboxLength=10, width=50, matchesFunction=acs.matches)
        entry.place(bordermode=OUTSIDE, height=30, x=25, y=25)
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
                         onvalue=1, offvalue=0, bg='black', fg='blue')
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
