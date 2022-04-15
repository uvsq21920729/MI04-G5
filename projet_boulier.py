
from tkinter import *

root = Tk()

def key(event):
    print("pressed"), repr(event.char)

def callback(event):
    print("clicked at"), print(event.x, event.y)
    for a in range(23*5):
        if canvas.itemconfig(7+a)["tags"][-1] == "current":
            print(True, a)
            n = a
            
            

canvas = Canvas(root, width=1400, height=300)
canvas.create_rectangle(0, 0, 1400, 300, fill = "#3e280f")
canvas.create_rectangle(10, 10, 1390, 290, fill = "#bbbbbb", outline = "#bbbbbb")
canvas.create_rectangle(1390//4-36, 10, 1390//4+22, 290, fill = "#3e280f", outline = "#3e280f")
canvas.create_rectangle(1390//4*2-83, 10, 1390//4*2+95, 290, fill = "#3e280f", outline = "#3e280f")
canvas.create_rectangle(1390//4*3-10, 10, 1390//4*3+48, 290, fill = "#3e280f", outline = "#3e280f")
canvas.create_rectangle(10, 72, 1390, 86, fill = "#3e280f")

ovals = []
for a in range(23):
    if (a+1)%2 == 0:
        pass
    ovals.append([canvas.create_oval(10+60*a, 10, 10+60*a+60, 54, fill = "#dd8624", state = "normal", activefill = "black")])
    for b in range(4):
        ovals[a].append(canvas.create_oval(10+60*a, 114+b*44, 10+60*a+60, 114+b*44+44, fill = "#dd8624", state = "normal", activefill = "black"))

canvas.bind("<Key>", key)
canvas.bind("<Button-1>", callback)
canvas.pack()
#test()
root.mainloop()
