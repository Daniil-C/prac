from tkinter import *

class App(Frame):
    def __init__(self, master=None, Title="Application", **kwargs):
        Frame.__init__(self, master, **kwargs)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.master.title(Title)
        self.grid(sticky="NEWS")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.S = StringVar()
        self.S.set("Hello")
        self.E = Entry(self, textvariable=self.S)
        self.E.grid(sticky="NEWS")
        self.E1 = Entry(self, textvariable=self.S)
        self.E1.grid(sticky="NEWS")
        self.L = Label(self)
        self.L.grid(sticky="NEWS")
        self.E.bind("<ButtonRelease>", self.touch)

    def touch(*a, **p):
        if A.E.select_present():
            A.L["text"] = A.E.selection_get()
        return True        


A = App()
A.mainloop()
