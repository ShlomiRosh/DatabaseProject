from tkinter import *
import tkinter as tk

FONT_NOTE = ("Ariel", 10, "bold", "underline")

# This class is basically a tool that creates a cool display window for the user, when the
# user moves the mouse to a specified place he will be able to read the particular message according
# to the needs of the app.
class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        # Display text in tooltip window
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def create_tool_tip(widget, text):
    tool_tip = ToolTip(widget)
    def enter(event):
        tool_tip.showtip(text)
    def leave(event):
        tool_tip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

def create_msg(self, p_x, p_y, message, bg_color = 'black', txt_color = 'red'):
    invalid = tk.Label(self, text='Note here!', bg=bg_color, bd=0, fg=txt_color, font=FONT_NOTE)
    if p_y and p_x:
        invalid.place(bordermode=OUTSIDE, x=p_x, y=p_y)
    create_tool_tip(invalid, text=message)
    return invalid