from tkinter import *

root = Tk()

def key(event):
    print("pressed"), repr(event.char)

def callback(event):
    n=-1
    for a in range(23*5):
        if canvas.itemconfig(ovals[0][0][0]+a)["tags"][-1] == "current":
            n = a
            break
    if n>0:
        mouvement(n)
def mouvement(n):
    print(ovals[n//5][n%5][1], n)
    if ovals[n//5][n%5][1] == 0:
        if n%5 == 0:
            canvas.move(ovals[n//5][n%5][0],0,15)
            ovals[n//5][n%5][1] = 1
        else:
            for N in range(n//5*5,n//5*5+n%5):
                print(n,N+1)
                if ovals[(N+1)//5][(N+1)%5][1] == 0:
                    canvas.move(ovals[(N+1)//5][(N+1)%5][0],0,-15)
                    ovals[(N+1)//5][(N+1)%5][1]+=1
    else:
        if n%5 == 0:
            canvas.move(ovals[n//5][n%5][0],0,-15)
            ovals[n//5][n%5][1] = 0
        else:
            for N in range(n//5*5+n%5,(n//5+1)*5):
                print(n,N)
                if ovals[N//5][N%5][1] == 1:
                    canvas.move(ovals[N//5][N%5][0],0,15)
                    ovals[N//5][N%5][1] = 0
def move():
    pass
        

canvas = Canvas(root, width=1400, height=300)
canvas.grid()
canvas.create_rectangle(0, 0, 1400, 300, fill = "#3e280f")
canvas.create_rectangle(10, 10, 1390, 290, fill = "#bbbbbb", outline = "#bbbbbb")
canvas.create_rectangle(10, 72, 1390, 86, fill = "#3e280f")

ovals = []
for a in range(23):
    if (a+1)%2 == 0:
        pass
    ovals.append([[canvas.create_oval(15+60*a, 10, 15+60*a+44, 54, fill = "#dd8624", state = "normal", activefill = "black"),0]])
    for b in range(4):
        ovals[a].append([canvas.create_oval(15+60*a, 114+b*44, 15+60*a+44, 114+b*44+44, fill = "#dd8624", state = "normal", activefill = "black"),0])
canvas.bind("<Key>", key)
canvas.bind("<Button-1>", callback)
canvas.pack()
#test()
root.mainloop()
