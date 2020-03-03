import tkinter as tk
import random
window = tk.Tk()
H = 300
W = 300
B_x = W/2
B_y = H/2


def fun(e): 
    Bx = (e.widget.winfo_x()+60*random.choice([-1, 1])) % (W-20)
    By = (e.widget.winfo_y()+60*random.choice([-1, 1])) % (H-20)
    e.widget.place(x=Bx, y=By)

def close_window (): 
    window.destroy()



window.geometry("{}x{}".format(W, H))
window.resizable(0, 0)
window.overrideredirect(1)

B=tk.Button(text="Close", command=close_window, width=2, height=2)
B.place(x=150, y=150)

B.bind("<Enter>", fun)
#B.bind("<Leave>", lambda e: e.widget.config(text="Close"))
window.mainloop()
