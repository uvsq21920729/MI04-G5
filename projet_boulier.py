##################################################
# groupe MI TD04                                 #
# Bonnardot  Arthure                     22106864#
# Guo  Xu Xin                            21920729#
# Le Brun  Maxence                       22101714#
# https://github.com/uvsq21920729/MI04-G5        #
##################################################
from tkinter import *

tickspeed = 40
askedRange = 23
encounter = 1
ovals_bis = []
op = []
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
    global ovals,ovals_bis,askedRange,encounter
    if ovals_bis:
        if len(ovals)*len(ovals[0])!=len(ovals_bis):
            askedRange = len(ovals_bis)//5
            canvas.delete('all')
            canvas.create_rectangle(0, 0, 1400, 400, fill = "#3e280f")
            canvas.create_rectangle(10, 10, 1390, 390, fill = "#bbbbbb", outline = "#bbbbbb")
            canvas.create_rectangle(10, 120, 1390, 144, fill = "#3e280f")
            encounter += 2
            ovals = []
            for a in range(askedRange):
                ovals.append([[canvas.create_oval(1380/askedRange*a+15+int((23-askedRange)*a*0.3), 10, 1380/askedRange*a+15+44+int((23-askedRange)*a*0.3), 54, fill = "#b36d1e", state = "normal", activefill = "black"),0,0,0]])
                for b in range(4):
                    ovals[a].append([canvas.create_oval(1380/askedRange*a+15+int((23-askedRange)*a*0.3), 210+b*44, 1380/askedRange*a+15+44+int((23-askedRange)*a*0.3), 210+b*44+44, fill = "#b36d1e", state = "normal", activefill = "black"),0,0])
        for a in range(len(ovals)):
            for b in range(len(ovals[a])):
                if ovals[a][b][1]!=ovals_bis[a*5+b]:
                    if ovals_bis[a*5+b] == 3:
                        ovals[a][b][1] = 1
                    if ovals_bis[a*5+b] == 0:
                        ovals[a][b][1] = 2
        ovals_bis = []
    else:
        for a in range(len(ovals)):
            for b in range(len(ovals[a])):
                ovals_bis.append(ovals[a][b][1])
    
def speed():
    global tickspeed
    if tickspeed%2:
        tickspeed = 80
    tickspeed/=2
def space():
    global askedRange,ovals,encounter
    root_bis = Tk()
    root_bis.title('Choisissez vos colonnes')
    root_bis.geometry('200x200')
    
    def setSpace():
        global askedRange,ovals,encounter
        askedRange = int(name_Tf.get())
        canvas.delete('all')
        canvas.create_rectangle(0, 0, 1400, 400, fill = "#3e280f")
        canvas.create_rectangle(10, 10, 1390, 390, fill = "#bbbbbb", outline = "#bbbbbb")
        canvas.create_rectangle(10, 120, 1390, 144, fill = "#3e280f")
        encounter += 2
        ovals = []
        for a in range(askedRange):
            ovals.append([[canvas.create_oval(1380/askedRange*a+15+int((23-askedRange)*a*0.3), 10, 1380/askedRange*a+15+44+int((23-askedRange)*a*0.3), 54, fill = "#b36d1e", state = "normal", activefill = "black"),0,0,0]])
            for b in range(4):
                ovals[a].append([canvas.create_oval(1380/askedRange*a+15+int((23-askedRange)*a*0.3), 210+b*44, 1380/askedRange*a+15+44+int((23-askedRange)*a*0.3), 210+b*44+44, fill = "#b36d1e", state = "normal", activefill = "black"),0,0])
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
    print(ovals)
    for a in range(len(ovals)):
        for b in range(len(ovals[a])):
            if ovals[a][b][2] >= 65:
                if ovals[a][b][1] == 1:
                    ovals[a][b][1] = 3
                elif ovals[a][b][1] == 2:
                    ovals[a][b][1] = 0
                ovals[a][b][2]=0
            if (ovals[a][b][0]+encounter)%5 == 0:
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
def operation():
    global askedRange,ovals,encounter,op
    root_bis = Tk()
    root_bis.title('Mode Opératoire')
    root_bis.geometry('400x200')
    op = ["0","+"]
    def add():
        global op
        op = [str(eval(op[0]+op[1]+str(name_Tf.get()))),"+"]
        name_Tf.delete(0,len(name_Tf.get()))
    def sub():
        global op
        op = [str(eval(op[0]+op[1]+str(name_Tf.get()))),"-"]
        name_Tf.delete(0,len(name_Tf.get()))
    def mul():
        global op
        op = [str(eval(op[0]+op[1]+str(name_Tf.get()))),"*"]
        name_Tf.delete(0,len(name_Tf.get()))
    def div():
        global op
        op = [str(eval(op[0]+op[1]+str(name_Tf.get()))),"/"]
        name_Tf.delete(0,len(name_Tf.get()))
    def show():
        global askedRange,ovals,encounter,op
        op = eval(op[0]+op[1]+str(name_Tf.get()))
        askedRange = len(str(op))
        canvas.delete('all')
        canvas.create_rectangle(0, 0, 1400, 400, fill = "#3e280f")
        canvas.create_rectangle(10, 10, 1390, 390, fill = "#bbbbbb", outline = "#bbbbbb")
        canvas.create_rectangle(10, 120, 1390, 144, fill = "#3e280f")
        encounter += 2
        ovals = []
        for a in range(askedRange):
            ovals.append([[canvas.create_oval(1380/askedRange*a+15+int((23-askedRange)*a*0.3), 10, 1380/askedRange*a+15+44+int((23-askedRange)*a*0.3), 54, fill = "#b36d1e", state = "normal", activefill = "black"),0,0,0]])
            for b in range(4):
                ovals[a].append([canvas.create_oval(1380/askedRange*a+15+int((23-askedRange)*a*0.3), 210+b*44, 1380/askedRange*a+15+44+int((23-askedRange)*a*0.3), 210+b*44+44, fill = "#b36d1e", state = "normal", activefill = "black"),0,0])
        x = [1]
        alterne = [2,5]
        n = 1
        while op%(n*alterne[-1]) != op:
            n*=alterne[-1]
            x.append(n)
            alterne.reverse()
        op = list(str(op))
        for a in range(len(op)):
            #ovals[a][int(op[0])%5][1]=1
            print(int(op[0])%5)
            if int(op[0])%5:
                for b in range(int(op[0])%5):
                    ovals[a][b+1][1]=1
            if int(op[0])//5 > 0:
                ovals[-1][0][1]=1
            op.pop(0)
        print(ovals)
        close()
    def close():
        root_bis.destroy()
    Label(root_bis, text="Opération a efféctuer").pack()
    name_Tf = Entry(root_bis)
    name_Tf.pack()
    
    Button(root_bis, text = " + ", command = add).pack()
    Button(root_bis, text = " - ", command = sub).pack()
    Button(root_bis, text = " x ", command = mul).pack()
    Button(root_bis, text = " / ", command = div).pack()
    Button(root_bis, text = " = ", command =show).pack()
    
    root_bis.mainloop()
    
canvas = Canvas(root, width=1400, height=400)
canvas.grid()

menu_bar = Menu()

menu_bar.add_command(label = "Vitesse", command = speed)
menu_bar.add_command(label = "Save/Load", command = save_or_load)
menu_bar.add_command(label = "Réinitialiser", command = reset)
menu_bar.add_command(label = "Nbrs collones", command = space)
menu_bar.add_command(label = "Mode Opératoire", command = operation)

root.config(menu=menu_bar)
ovals = []

canvas.create_rectangle(0, 0, 1400, 400, fill = "#3e280f")
canvas.create_rectangle(10, 10, 1390, 390, fill = "#bbbbbb", outline = "#bbbbbb")
canvas.create_rectangle(10, 120, 1390, 144, fill = "#3e280f")
for a in range(askedRange):
    ovals.append([[canvas.create_oval(15+60*a, 10, 15+60*a+44, 54, fill = "#b36d1e", state = "normal", activefill = "black"),0,0,0]])
    for b in range(4):
        ovals[a].append([canvas.create_oval(15+60*a, 210+b*44, 15+60*a+44, 210+b*44+44, fill = "#b36d1e", state = "normal", activefill = "black"),0,0])

canvas.bind("<Key>", key)
canvas.bind("<Button-1>", callback)
canvas.pack()
move()
root.mainloop()
