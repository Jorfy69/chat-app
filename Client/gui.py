import tkinter 
import tkinter.filedialog
import ttkbootstrap as ttk
from ttkbootstrap.constants import * # type: ignore
import time

class Gui:
    def __init__(self,theme,geo,Title):
        self.root = ttk.Window(themename=theme)
        self.root.geometry(f'{geo[0]}x{geo[1]}')
        self.root.title(Title)
    def button(self,buttonname, command,side=tkinter.LEFT,padding={"x":10,"y":10}):
        BN = ttk.Button(self.root, text=buttonname, command=lambda: command())
        BN.pack(side=side, padx=padding["x"], pady=padding["y"])
    def entry(self, width=20, side=tkinter.LEFT, padding={"x": 10, "y": 10}):
        var = tkinter.StringVar()
        EN = ttk.Entry(self.root, textvariable=var, width=width)
        #text_leng = len(var.get()) + 1
        #var.trace_add("write", EN.config(width=max(width, text_leng)))
        EN.pack(side=side, padx=padding["x"], pady=padding["y"])
        return var 
    def run(self):
        self.root.mainloop()