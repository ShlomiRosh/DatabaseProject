import tkinter as tk
from View import StartPage as sp
from View import RegisterPage as rp
from View import SearchPage as sep
from View import UserPage as up

WIN_SIZE = '750x500+50+20'
TITLE = 'TripleA'

class TripleAapp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side = 'top', fill = 'both', expand = True)
        #container.place(width=750, height=550)

        self.frames = {}
        # For every page that you want to show you need to add it hear
        for f in (sp.StartPage, rp.RegisterPage, sep.SearchPage, up.UserPage):

            frame = f(container, self)
            self.frames[f] = frame
            frame.place(width=750,height=550)

        self.show_frame(sp.StartPage)

    def show_frame(self, con):

        frame = self.frames[con]
        frame.tkraise()




application = TripleAapp()
application.geometry(WIN_SIZE)
application.resizable(False, False)
application.title(TITLE)
application.iconbitmap('..\Pic\\family.ico')
application.mainloop()