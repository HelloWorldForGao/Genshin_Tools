import tkinter as tk
import random as r

win = tk.Tk()

with open("init.txt",mode = "r",encoding = "utf-8") as f:
    code_read = f.read()
    exec(code_read)

win.geometry(geometry)
win.minsize(geometrys[0],geometrys[1])
win.maxsize(geometrys[0],geometrys[1])

win.title(title)

def onquit():
    win.destroy()

label1 = tk.Label(win)
label1.pack()

def change_text():
    global label1
    while(True):
        beixuan = r.choice(yulu)
        if label1["text"] == beixuan:
            pass
        else:
            label1["text"] = beixuan
            break
    win.update()
def cout_text():
    global changeneed
    print(label1["text"])
    if changeneed:
        change_text()
def needchange():
    global changeneed
    if changeneed:
        changeneed = False
        print(disable_cneed)
    else:
        changeneed = True
        print(enabled_cneed)

change_text()

button1 = tk.Button(win,text = buttons[0],command = change_text)
button1.pack()
button2 = tk.Button(win,text = buttons[1],command = cout_text)
button2.pack()
button3 = tk.Button(win,text = buttons[2],command = needchange)
button3.pack()

quit = tk.Button(win,text = when_quit,command = onquit)
quit.pack()

win.mainloop()
