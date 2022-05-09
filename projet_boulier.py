##################################################
# groupe MI TD04                                 #
# Guo  Xu Xin                                    #
# Le Brun  Maxence                               #
#
# https://github.com/uvsq21920729/MI04-G5        #
##################################################
from tkinter import *

tickspeed = 40
askedRange = 13

root = Tk()

def key(event):
    print("pressed"), repr(event.char)

def callback(event):
    n=-1
    for a in range(askedRange*5):
        if canvas.itemconfig(ovals[0][0][0]+a)["tags"][-1] == "current":
            n = a
            break
    if n >= 0:
        mouvement(n)
def reset():
    global ovals
    for a in range(len(ovals)):
        for b in range(len(ovals[a])):
            if ovals[a][b][1]!=2 and ovals[a][b][1]!=0:
                ovals[a][b][1] = 2
                if ovals[a][b][2]:
                    ovals[a][b][2] = 65 - ovals[a][b][2]
def save_or_load():
    pass
def speed():
    global tickspeed
    if tickspeed%2:
        tickspeed = 80
    tickspeed/=2
def space():
    global askedRange
    root_bis = Tk()
    root_bis.title('Choisissez vos colonnes')
    root_bis.geometry('200x200')
    
    def setSpace():
        global askedRange
        askedRange = int(name_Tf.get())
        reset()
        root_bis.destroy()
    Label(root_bis, text="Nombres de colonnes").pack()
    name_Tf = Entry(root_bis)
    name_Tf.pack()
    
    Button(root_bis, text="Cliquez IcI", command=setSpace).pack()
    
    root_bis.mainloop()
def mouvement(n):
    global ovals
    if ovals[n//5][n%5][1] == 0:
        if n%5 == 0:
            ovals[n//5][n%5][1] = 1
        else:
            for N in range(n//5*5,n//5*5+n%5):
                if ovals[(N+1)//5][(N+1)%5][1] == 0:
                    ovals[(N+1)//5][(N+1)%5][1] = 1
    if ovals[n//5][n%5][1] == 3:
        if n%5 == 0:
            ovals[n//5][n%5][1] = 2
        else:
            for N in range(n//5*5+n%5,(n//5+1)*5):
                if ovals[N//5][N%5][1] == 3:
                    ovals[N//5][N%5][1] = 2
def move():
    global ovals,tickspeed
    for a in range(len(ovals)):
        for b in range(len(ovals[a])):
            if ovals[a][b][2] >= 65:
                if ovals[a][b][1] == 1:
                    ovals[a][b][1] = 3
                elif ovals[a][b][1] == 2:
                    ovals[a][b][1] = 0
                ovals[a][b][2]=0
            if (ovals[a][b][0]+1)%5 == 0:
                if ovals[a][b][1] == 1 and ovals[a][b][2] < 65:
                    canvas.move(ovals[a][b][0],0,1)
                    ovals[a][b][2] += 1
                if ovals[a][b][1] == 2 and ovals[a][b][2] < 65:
                    canvas.move(ovals[a][b][0],0,-1)
                    ovals[a][b][2] += 1
            else:
                if ovals[a][b][1] == 1 and ovals[a][b][2] < 65:
                    canvas.move(ovals[a][b][0],0,-1)
                    ovals[a][b][2] += 1
                if ovals[a][b][1] == 2 and ovals[a][b][2] < 65:
                    canvas.move(ovals[a][b][0],0,1)
                    ovals[a][b][2] += 1
    canvas.after(int(tickspeed),move)

canvas = Canvas(root, width=1400, height=400)
canvas.grid()

menu_bar = Menu()

menu_bar.add_command(label = "Vitesse", command = speed)
menu_bar.add_command(label = "Save/Load", command = save_or_load)
menu_bar.add_command(label = "Réinitialiser", command = reset)
menu_bar.add_command(label = "Nbrs collones", command = space)

root.config(menu=menu_bar)
ovals = []

canvas.create_rectangle(0, 0, 1400, 400, fill = "#3e280f")
canvas.create_rectangle(10, 10, 1390, 390, fill = "#bbbbbb", outline = "#bbbbbb")
canvas.create_rectangle(10, 120, 1390, 144, fill = "#3e280f")
for a in range(askedRange):
    ovals.append([[canvas.create_oval(15+60*a, 10, 15+60*a+44, 54, fill = "#b36d1e", state = "normal", activefill = "black"),0,0,0]])
    for b in range(4):
        ovals[a].append([canvas.create_oval(15+60*a, 210+b*44, 15+60*a+44, 210+b*44+44, fill = "#b36d1e", state = "normal", activefill = "black"),0,0])

move()

canvas.bind("<Key>", key)
canvas.bind("<Button-1>", callback)
canvas.pack()
root.mainloop()
