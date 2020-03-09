from tkinter import *  
import subprocess
  
def clicked():  
    res = "wc"
    args = lbl["text"].split(" ")
    args.append(txt.get())
    out = subprocess.run(args, stdout=subprocess.PIPE, encoding="utf-8")
    lbl_res.configure(justify=LEFT, text=out.stdout)
    txt.delete(0, END)

def fce(myC):
    def chk_but(c=myC):
        if c not in lbl["text"]:
            lbl_txt = "{} {}".format(lbl["text"], c)
        else:
            lbl_txt = lbl["text"].replace(" " + c, "")
        lbl.configure(text=lbl_txt)
    return chk_but

window = Tk()
window.title("WC GUI")
window.geometry('700x400')
lbl = Label(window, text="wc")
lbl.grid(column=0, row=0)
txt = Entry(window,width=50)
txt.grid(column=1, row=0, sticky=W)
btn = Button(window, text="Enter", command=clicked)  
btn.grid(column=2, row=0, sticky=W)
chk_state_c = BooleanVar()  
chk_state_c.set(False) 
chk_c = Checkbutton(window, text="-c", var=chk_state_c, command=fce("-c"))  
chk_c.grid(column=0, row=1, sticky=W)

lbl_c = Label(window, text="напечатать количество байт")
lbl_c.grid(column=1, row=1, sticky=W)

chk_state_m = BooleanVar()  
chk_state_m.set(False) 
chk_m = Checkbutton(window, text="-m", var=chk_state_m, command=fce("-m"))  
chk_m.grid(column=0, row=2, sticky=W)

lbl_m = Label(window, text="напечатать количество символов")
lbl_m.grid(column=1, row=2, sticky=W)

chk_state_l = BooleanVar()  
chk_state_l.set(False)  
chk_l = Checkbutton(window, text="-l", var=chk_state_l, command=fce("-l"))  
chk_l.grid(column=0, row=3, sticky=W)

lbl_l = Label(window, text="напечатать количество новых строк")
lbl_l.grid(column=1, row=3, sticky=W)

chk_state_L = BooleanVar()  
chk_state_L.set(False)  
chk_L = Checkbutton(window, text="-L", var=chk_state_L, command=fce("-L"))  
chk_L.grid(column=0, row=4, sticky=W)

lbl_L = Label(window, text="напечатать максимальной число строк по ширине экрана")
lbl_L.grid(column=1, row=4, sticky=W)

chk_state_w = BooleanVar()  
chk_state_w.set(False)  
chk_w = Checkbutton(window, text="-w", var=chk_state_w, command=fce("-w"))  
chk_w.grid(column=0, row=5, sticky=W)

lbl_w = Label(window, text="напечатать количество слов")
lbl_w.grid(column=1, row=5, sticky=W)

chk_state_ff = BooleanVar()  
chk_state_ff.set(False)  
chk_ff = Checkbutton(window, text="--files0-from=Ф", var=chk_state_ff, command=fce("--files0-from="))  
chk_ff.grid(column=0, row=6, sticky=W)

lbl_ff = Label(window, justify=LEFT, text="читать ввод из файлов, имена которых\n(завершённые нулем) перечислены в файле Ф;\nЕсли Ф равно -, то читать имена файлов из\nстандартного ввода")
lbl_ff.grid(column=1, row=6, sticky=W)

chk_state_h = BooleanVar()  
chk_state_h.set(False)  
chk_h = Checkbutton(window, text="--help", var=chk_state_h, command=fce("--help"))  
chk_h.grid(column=0, row=7, sticky=W)

lbl_h = Label(window, text="показать эту справку и выйти")
lbl_h.grid(column=1, row=7, sticky=W)

chk_state_v = BooleanVar()  
chk_state_v.set(False)  
chk_v = Checkbutton(window, text="--version", var=chk_state_v, command=fce("--version"))  
chk_v.grid(column=0, row=8, sticky=W)

lbl_v = Label(window, justify=LEFT, text="показать информацию о версии и выйти")
lbl_v.grid(column=1, row=8, sticky=W)

lbl_res = Label(window, text="")
lbl_res.place(x=10, y=300)
#lbl_res.grid(column=1, row=9, sticky="NEWS")

window.mainloop()
