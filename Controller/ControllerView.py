import tkinter as tk
from View import StartPage as sp

WIN_SIZE = '750x500+50+20'
TITLE = 'TripleA'

class TripleAapp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        self.container = tk.Frame(self)
        self.container.pack(side = 'top', fill = 'both', expand = True)
        #container.place(width=750, height=550)

        self.frames = {}
        frame = sp.StartPage(self.container, self)
        self.frames[sp.StartPage] = frame
        frame.place(width=750, height=550)
        self.show_frame(sp.StartPage)


    def show_frame(self, con):

        frame = self.frames[con]
        frame.tkraise()


    def add_frame(self, con):

        frame = con(self.container, self)
        self.frames[con] = frame
        frame.place(width=750, height=550)


    def remove_frame(self, con):

        self.frames.pop(con)




application = TripleAapp()
application.geometry(WIN_SIZE)
application.resizable(False, False)
application.title(TITLE)
application.iconbitmap('..\Pic\\family.ico')
application.mainloop()