from tkinter import *
import time
from math import *
import random
from tkinter import messagebox
root=Tk()
root.geometry('1020x620')
can=Canvas(root,width=1020,height=620)
can.pack()
koord={'x':460,'y1':100,'y2':200,'y3':300,'y4':400,'y5':500}
global cond
global x
global menueee
global auto
global txt
global a
x = 0
a = 0
men = 0
cond = 0
auto = 1
def taskmanage(event):          
    global KNdem
    global KNpom
    global KNzast
    global KNusl
    global KNexit
    x=event.x
    y=event.y
    if (x<=koord['x']+121 and x>=koord['x']-21 and y<=koord['y3']+40 and y>=koord['y3']):
        can.delete('all')
        zast ()
    if (x<=koord['x']+121 and x>=koord['x']-21 and y<=koord['y2']+40 and y>=koord['y2']):
        helpa ()
    if (x<=koord['x']+121 and x>=koord['x']-21 and y<=koord['y1']+40 and y>=koord['y1']):
        demonstration()
    if (x<=koord['x']+121 and x>=koord['x']-21 and y<=koord['y4']+40 and y>=koord['y4']):
        uslovie ()
    if (x<=koord['x']+121 and x>=koord['x']-21 and y<=koord['y5']+40 and y>=koord['y5']):
        vyhod ()
def ris(event):
    global KNdem
    global KNpom
    global KNzast
    global KNusl
    global KNexit
    x=event.x
    y=event.y
    if (x<=koord['x']+121 and x>=koord['x']-21 and y<=koord['y1']+40 and y>=koord['y1']): 
         can.itemconfig(KNdem,outline='deepskyblue')
    else:
         can.itemconfig(KNdem,outline='black')
    if ( x<=koord['x']+121 and x>=koord['x']-21 and y<=koord['y2']+40 and y>=koord['y2']):  
         can.itemconfig(KNpom,outline='orange')
    else:
         can.itemconfig(KNpom,outline='black')
    if ( x<=koord['x']+121 and x>=koord['x']-21 and y<=koord['y3']+40 and y>=koord['y3']):  
         can.itemconfig(KNzast,outline='yellow')
    else:
         can.itemconfig(KNzast,outline='black')
    if ( x<=koord['x']+121 and x>=koord['x']-21 and y<=koord['y4']+40 and y>=koord['y4']):    
         can.itemconfig(KNusl,outline='lime')
    else:
         can.itemconfig(KNusl,outline='black')
    if ( x<=koord['x']+121 and x>=koord['x']-21 and y<=koord['y5']+40 and y>=koord['y5']):    
         can.itemconfig(KNexit,outline='tomato')
    else:
         can.itemconfig(KNexit,outline='black')
def perehod_v_demonstr(event):         
    global KNdem
    global KNpom
    global KNzast
    global KNusl
    global KNexit
    x=event.x
    y=event.y
    demonstration()
def helpa():
    can.delete('all')
    can.unbind('<Button-1>')
    can.unbind('<Motion>')
    can.bind('<Button-1>', menu)
    can.create_text(510, 40, text='Manual', font='Calibri 21', anchor='c', justify='center')
    can.create_text(510, 200, text='1) To access a section from the menu, use Left Mouse Button on the desired item', font='Verdana 18', anchor='c', justify='left')
    can.create_text(510, 250, text='2) Auto-fill is performed by pressing the [Auto-fill] button', font='Verdana 18', anchor='c', justify='left')
    can.create_text(510, 300, text='3) Demonstration can be turned on and off using the buttons', font='Verdana 18', anchor='c', justify='left')
    can.create_text(510, 350, text='4) You can select the grid step using the buttons at the bottom of the screen', font='Verdana 18', anchor='c', justify='left')
    can.create_text(510, 450, text='5) To exit to the menu, use LMB on the screen', font='Verdana 18', anchor='c', justify='left')

def temp_helpa():
    can.delete('all')
    can.unbind('<Button-1>')
    can.unbind('<Motion>')
    can.bind('<Button-1>', menu)
    can.create_text(510, 40, text='Manual', font='Calibri 21', anchor='c', justify='center')
    can.create_text(510, 200, text='1) To access a section from the menu, use Left Mouse Button on the desired item', font='Verdana 18', anchor='c', justify='left')
    can.create_text(510, 250, text='2) Auto-fill is performed by pressing the [Auto-fill] button', font='Verdana 18', anchor='c', justify='left')
    can.create_text(510, 300, text='3) Demonstration can be turned on and off using the buttons', font='Verdana 18', anchor='c', justify='left')
    can.create_text(510, 350, text='4) You can select the grid step using the buttons at the bottom of the screen', font='Verdana 18', anchor='c', justify='left')
    can.create_text(510, 450, text='5) To exit to the menu, use LMB on the screen', font='Verdana 18', anchor='c', justify='left')

def uslovie():
    can.delete('all')
    can.unbind('<Button-1>')
    can.unbind('<Motion>')
    can.bind('<Button-1>', menu)
    can.bind('<Button-3>', helpa)
    can.create_text(510, 40, text='Task', font='Calibri 21', anchor='c', justify='center')
    can.create_text(510, 200, text='Write a program that simulates the construction of ', font='Calibri 18', anchor='c',justify='center')
    can.create_text(510, 250, text='magnetic induction lines of a field created by a torus with current.',font='Calibri 18', anchor='c', justify='center')
    can.create_text(510, 300, text='The values of the currents, coil winding density,', font='Calibri 18', anchor='c',justify='center')
    can.create_text(510, 350, text='outer and inner radius are entered from the keyboard', font='Calibri 18',anchor='c', justify='center')
    can.create_text(510, 400, text='during the dialogue.', font='Calibri 18', anchor='c', justify='center')
    can.create_text(510, 500, text='To return to the menu, click the screen with the mouse', font='Verdana 11',anchor='c', justify='center')
    can.create_line(120,360,120,560,width=5)
    can.create_line(120,560,520,560,width=5)
    can.create_line(500,100,900,100,width=5)
    can.create_line(900,100,900,300,width=5)
def vyhod():
    root.destroy()
def swapto(event):
    x=event.x
    y=event.y
    if cond == 1:
        menu(event)
def secret():
    print("")
def demonstration():
    can.unbind('<Button-1>')
    can.unbind('<Motion>')
    can.delete('all')
    can.create_line(160,0,160,620)    
    can.create_line(160,580,1020,580)
    k = 20
    for i in range(0,43,1):
        can.create_line(160 + k*i, 0, 160 + k*i, 580, width = 1)
    for q in range(0,29,1):
        can.create_line(160, k*q, 1020, k*q, width = 1)
    def shag_setki_UP():
        can.delete('X2')
        k = 10
        for i in range(0,86,1):
            can.create_line(160 + k*i, 0, 160 + k*i, 580, width = 1,tag='X1')
        for q in range(0,58,1):
            can.create_line(160, k*q, 1020, k*q, width = 1,tag='X1')
        k= 20
    def shag_setki_DOWN():
        can.delete('X1')
        for i in range(0,43,1):
            can.create_line(160 + k*i, 0, 160 + k*i, 580, width = 1,tag='X2')
        for q in range(0,29,1):
            can.create_line(160, k*q, 1020, k*q, width = 1,tag='X2')
        k= 20

    def temp_helpa():
        global auto
        can.delete('all')
        can.unbind('<Button-1>')
        can.unbind('<Motion>')
        can.bind('<Button-1>', perehod_v_demonstr)  # bind to function for transitioning to demonstration
        can.create_text(510, 40, text='Manual', font='Calibri 21', anchor='c', justify='center')
        can.create_text(510, 200, text='1) To access a section from the menu, use LMB (Left Mouse Button) on the desired item',font='Verdana 18', anchor='c', justify='left')
        can.create_text(510, 250, text='2) Auto-fill is performed by pressing the [Auto-fill] button',font='Verdana 18', anchor='c', justify='left')
        can.create_text(510, 300, text='3) Demonstration can be turned on and off using the buttons', font='Verdana 18',anchor='c', justify='left')
        can.create_text(510, 350, text='4) You can select the grid step using the buttons at the bottom of the screen',font='Verdana 18', anchor='c', justify='left')
        can.create_text(510, 450, text='5) To return to the demonstration, use the left mouse click on the screen',font='Verdana 18', anchor='c', justify='left')
        tokV.destroy()
        dV.destroy()
        DV.destroy()
        nV.destroy()
        knopka.destroy()
        vyrubay.destroy()
        avto.destroy()
        pomoshh.destroy()
        reboot_button.destroy()
        shagX1.destroy()
        shagX2.destroy()
        stope.destroy()
    global schetchick1
    global t
    global m
    global schetchick2
    global t2
    global schetchick3
    global t3
    global schetchick4
    global t4
    schetchick1 = 0
    t = 0
    m = 0
    schetchick2 = 0
    t2 = 0
    schetchick3 = 0
    t3 = 0
    schetchick4 = 0
    t4 = 0
    if auto == 1:
        schetchick1=1
        schetchick2=3
        schetchick3=3
        schetchick4=4
    w=0;x1=[];y1=[];x2=[];y2=[];TOK1=[];TOK2=[];Rad1=[];Rad2=[];INDUCT1=[];INDUCT2=[];cosinoos1=[];sinoos1=[];cosinoos2=[];sinoos2=[];smesh1=[];smeshy1=[];smesh2=[];smeshy2=[]
    tok=StringVar();d=StringVar();D=StringVar();n=StringVar()
    def proverkapolyavvoda1(e):      
        global schetchick1
        global t
        global m
        if e.keysym == 'period':
            t = t + 1
        if e.keysym == 'minus':
            m = m + 1
        if e.keysym in '0123456789' or e.keysym == 'period' or e.keysym == 'minus':
            schetchick1+=1
        elif e.keysym == 'BackSpace':
            schetchick1-=1
        else:
            tokV.delete(schetchick1, END)
        if t > 1:
            tokV.delete(schetchick1-1, END)
            schetchick1-=1 
            t = 1
        if m > 1:
            tokV.delete(schetchick1-1, END)
            schetchick1-=1 
            m = 1
    def proverkapolyavvoda2(e):
        global schetchick2
        global t2
        if e.keysym == 'period':
            t2 = t2 + 1
        if e.keysym in '0123456789' or e.keysym == 'period':
            schetchick2+=1
        elif e.keysym == 'BackSpace':
            schetchick2-=1
        else:
            dV.delete(schetchick2, END)
        if t2 > 1:
            dV.delete(schetchick2-1, END)
            schetchick2-=1 
            t2 = 1
    def proverkapolyavvoda3(e):
        global schetchick3
        global t3
        if e.keysym == 'period':
            t3 = t3 + 1
        if e.keysym in '0123456789' or e.keysym == 'period':
            schetchick3+=1
        elif e.keysym == 'BackSpace':
            schetchick3-=1
        else:
            DV.delete(schetchick3, END)
        if t3 > 1:
            DV.delete(schetchick3-1, END)
            schetchick3-=1 
            t3 = 1
    def proverkapolyavvoda4(e):
        global schetchick4
        global t4
        if e.keysym == 'period':
            t4 = t4 + 1
        if e.keysym in '0123456789' or e.keysym == 'period':
            schetchick4+=1
        elif e.keysym == 'BackSpace':
            schetchick4-=1
        else:
            nV.delete(schetchick4, END)
        if t3 > 1:
            nV.delete(schetchick4-1, END)
            schetchick4-=1 
            t3 = 1
    def otkl():
        global cond
        tokV.destroy()
        dV.destroy()
        DV.destroy()
        nV.destroy()
        stope.destroy()
        cond = 1
        can.delete('all')
        knopka.destroy()
        vyrubay.destroy()
        avto.destroy()
        pomoshh.destroy()
        reboot_button.destroy()
        shagX1.destroy()
        shagX2.destroy()
        can.create_text(500, 300, text = "Press LMB to return to Menu", anchor = 'c',font='Calibri 20')
        can.delete('temp')
        can.bind('<Button-1>',menu)
    def avtozap():
        global auto
        tokV.delete(0,END)
        dV.delete(0,END)
        DV.delete(0,END)
        nV.delete(0,END)
        tokV.insert(0,'2')
        dV.insert(0,'100')
        DV.insert(0,'200')
        nV.insert(0,'0.02')
        auto = 1
    def stop():
        global cond
        cond = 1
    def reboot():
        global cond
        can.delete('temp')
        cond = 1
    def dema():
        global x
        x = x + 1
        if x == 1:
            linecolor = 'red'
            dotcolor = 'black'
        if x == 2:
            linecolor = 'forestgreen'
            dotcolor = 'forestgreen'
        if x == 3:
            linecolor = 'steelblue'
            dotcolor = 'steelblue'
        if x == 6:
            linecolor = 'orchid'
            dotcolor = 'orchid'
        if x == 5:
            linecolor = 'dodgerblue'
            dotcolor = 'dodgerblue'
        if x == 4:
            linecolor = 'olive'
            dotcolor = 'olive'
        if x == 7:
            x = 1
            linecolor = 'red'
            dotcolor = 'black'
        global cond
        cond = 0
        Xzagr=800
        l = 0.5
        i = float(tokV.get())
        d = float(dV.get())
        D = float(DV.get())
        n = float(nV.get())
        N = int(D*pi*n)
        ugl = 2*pi / N 
        w = abs(i * 10)
        if (i < -3) or (i > 3):
            messagebox.showerror("Invalid value",
                                 "The entered current value must be within the following range: \n [-3 ; 3], i must be an integer")
            cond = 1
            can.delete('temp')
        if (d < 25) or (d > 500):
            messagebox.showerror("Invalid value",
                                 "The entered inner diameter must be within the following range: \n [25 ; 500]")
            cond = 1
            can.delete('temp')
        if (D < 50) or (D > 600):
            messagebox.showerror("Invalid value",
                                 "The entered outer diameter must be within the following range: \n [50 ; 600]")
            cond = 1
            can.delete('temp')
        if (D <= d):
            messagebox.showerror("Invalid value",
                                 "In the context of the task, the inner diameter\nmust be smaller than the outer diameter")
            cond = 1
            can.delete('temp')
        if (n < 0) or (n > 0.05):
            messagebox.showerror("Invalid value",
                                 "The entered coil winding density must be within the following range: \n [0.01 ; 0.05]")
            cond = 1
            can.delete('temp')

        if D / d > 2:
            messagebox.showwarning("Warning, extreme values!",
                                   "The outer diameter exceeds the inner diameter by more than two times! \nIt is recommended to change one of the values")
        if i == 0 or d == 0 or D == 0 or n == 0:
            messagebox.showerror("Error!", "All values must be non-zero for construction")

            cond = 1
            can.delete('temp')
        for k in range (0,N+1):   
            x1.append(0);y1.append(0);TOK1.append(0);Rad1.append(0);smesh1.append(0);smeshy1.append(0);cosinoos1.append(0);sinoos1.append(0);INDUCT1.append(0);x2.append(0);y2.append(0);TOK2.append(0);Rad2.append(0);smesh2.append(0);smeshy2.append(0);cosinoos2.append(0);sinoos2.append(0);INDUCT2.append(0)
            TOK1[k] = i;TOK2[k] = -i
        for k in range(0,N+1):
            x1[k] = 500 + d * sin(ugl*k)*0.5;y1[k] = 300 + d * cos(ugl*k)*0.5
            x2[k] = 500 + D * sin(ugl*k)*0.5;y2[k] = 300 + D * cos(ugl*k)*0.5
            can.create_oval(x1[k]-3,y1[k]-3,x1[k]+3,y1[k]+3, fill=dotcolor,outline='black', tag = 'temp')
            can.create_oval(x2[k]-3,y2[k]-3,x2[k]+3,y2[k]+3, fill=dotcolor,outline='black', tag = 'temp')
            root.update()
        for h in range (1,int(D/10)-1):
            c=0
            xdef = 500;ydef = 300 + d/2 + D/w*h
            x0 = xdef;y0 = ydef;temporx = xdef;tempory = ydef
            while (c < 100 or abs(xdef-x0)>=10 or abs(ydef-y0)>=10) and (cond == 0):
                for k in range (0,N):
                    Rad1[k]=sqrt((xdef-x1[k])**2 + (ydef-y1[k])**2);INDUCT1[k] = TOK1[k]/Rad1[k] * l;sinoos1[k]=(ydef-y1[k])/Rad1[k];cosinoos1[k]=(xdef-x1[k])/Rad1[k]
                    smesh1[k]=INDUCT1[k]*sinoos1[k];smeshy1[k]=INDUCT1[k]*cosinoos1[k]
                    Rad2[k]=sqrt((xdef-x2[k])**2 + (ydef-y2[k])**2);INDUCT2[k] = TOK2[k]/Rad2[k] * l;sinoos2[k]=(ydef-y2[k])/Rad2[k];cosinoos2[k]=(xdef-x2[k])/Rad2[k]
                    smesh2[k]=INDUCT2[k]*sinoos2[k];smeshy2[k]=INDUCT2[k]*cosinoos2[k]
                    temporx = temporx-smesh1[k]-smesh2[k];tempory = tempory+smeshy1[k]+smeshy2[k]
                can.create_line(xdef,ydef,temporx,tempory,fill=linecolor,width=2,tag='temp')
                xdef = temporx;ydef = tempory
                c+=1
                root.update()
            if cond == 0:
                can.create_line(xdef,ydef,x0,y0,fill=linecolor,width=2,tag='temp')
            can.delete('txt1')
    can.create_text(75, 30, text='Current (A)')
    can.create_text(75, 80, text='Inner Diameter (unit)')
    can.create_text(75, 130, text='Outer Diameter (unit)')
    can.create_text(75, 175, text='Number of Turns\n   per unit length')
    can.create_text(75, 520, text='Allowed Values:')
    can.create_text(75, 535, text='Current [-3; 3]')
    can.create_text(75, 550, text='Inner d [25; 500]')
    can.create_text(75, 565, text='Outer d [50; 600]')
    can.create_text(75, 580, text='Winding Density [0.01; 0.05]')
    tokV=Entry(textvariable=tok,justify='center',bd=4)
    tokV.place(x=75,y=50,anchor='c')
    dV=Entry(textvariable=d,justify='center',bd=4)
    dV.place(x=75,y=100,anchor='c')
    DV=Entry(textvariable=D,justify='center',bd=4)
    DV.place(x=75,y=150,anchor='c')
    nV=Entry(textvariable=n,justify='center',bd=4)
    nV.place(x=75,y=200,anchor='c')
    tokV.bind('<KeyRelease>', proverkapolyavvoda1)
    dV.bind('<KeyRelease>', proverkapolyavvoda2)
    DV.bind('<KeyRelease>', proverkapolyavvoda3)
    nV.bind('<KeyRelease>', proverkapolyavvoda4)
    can.create_text(75, 245, text='Grid Cell\nDefault:\n20x20 (unit)', anchor='c', justify='center')
    can.create_text(75, 300, text='COMMANDS', font='Verdana 15')

    knopka = Button(text='Build', command=dema, activebackground='skyblue', bd=4)
    knopka.place(x=75, y=370, anchor='c')

    vyrubay = Button(text='Exit to Menu', command=otkl, activebackground='skyblue', bd=4)
    vyrubay.place(x=75, y=410, anchor='c')

    avto = Button(text='Auto-fill', command=avtozap, activebackground='skyblue', bd=4)
    avto.place(x=75, y=330, anchor='c')

    pomoshh = Button(text='Call Help', command=temp_helpa, activebackground='skyblue', bd=4)
    pomoshh.place(x=75, y=450, anchor='c')

    reboot_button = Button(text='Clear Field', command=reboot, activebackground='skyblue', bd=4)
    reboot_button.place(x=75, y=490, anchor='c')

    shagX2 = Button(text='Grid Step X2', command=shag_setki_UP, activebackground='skyblue', bd=4)
    shagX2.place(x=230, y=600, anchor='c')

    shagX1 = Button(text='Grid Step X1', command=shag_setki_DOWN, activebackground='skyblue', bd=4)
    shagX1.place(x=330, y=600, anchor='c')

    stope = Button(text='STOP', command=stop, bg='tomato', activebackground='skyblue', bd=4)
    stope.place(x=530, y=600, anchor='c')


def menu(event):
    can.unbind('<Button-1>')
    can.delete('all')            
    x=event.x;y=event.y
    global KNdem
    global KNpom
    global KNzast
    global KNusl
    global KNexit
    can.unbind('<Button-1>')
    can.bind('<Button-1>',taskmanage)
    can.bind('<Motion>',ris)
    can.create_text(330, 80, text="M E N U", font='Calibri 25')

    KNdem = can.create_rectangle(koord['x'] - 21, koord['y1'], koord['x'] + 121, koord['y1'] + 40,
                                 outline='deepskyblue', fill='deepskyblue', width=5)
    can.create_text(koord['x'] + 50, koord['y1'] + 20, text='Demonstration', anchor='c', font='Calibri 13')

    KNpom = can.create_rectangle(koord['x'] - 21, koord['y2'], koord['x'] + 121, koord['y2'] + 40, outline='orange',
                                 fill='orange', width=5)
    can.create_text(koord['x'] + 50, koord['y2'] + 20, text='Help', anchor='c', font='Calibri 13')

    KNzast = can.create_rectangle(koord['x'] - 21, koord['y3'], koord['x'] + 121, koord['y3'] + 40, outline='yellow',
                                  fill='yellow', width=5)
    can.create_text(koord['x'] + 50, koord['y3'] + 20, text='Splash Screen', anchor='c', font='Calibri 13')

    KNusl = can.create_rectangle(koord['x'] - 21, koord['y4'], koord['x'] + 121, koord['y4'] + 40, outline='lime',
                                 fill='lime', width=5)
    can.create_text(koord['x'] + 50, koord['y4'] + 20, text='Condition', anchor='c', font='Calibri 13')

    KNexit = can.create_rectangle(koord['x'] - 21, koord['y5'], koord['x'] + 121, koord['y5'] + 40, outline='tomato',
                                  fill='tomato', width=5)
    can.create_text(koord['x'] + 50, koord['y5'] + 20, text='Exit', anchor='c', font='Calibri 13')

    can.create_line(320, 360, 320, 560, width=5)
    can.create_line(320, 560, 620, 560, width=5)
    can.create_line(400, 80, 700, 80, width=5)
    can.create_line(700, 80, 700, 280, width=5)

    if (x <= koord['x'] + 121 and x >= koord['x'] - 21 and y <= koord['y1'] + 40 and y >= koord['y1']):
        can.itemconfig(KNdem, outline='black')
    if (x <= koord['x'] + 121 and x >= koord['x'] - 21 and y <= koord['y2'] + 40 and y >= koord['y2']):
        can.itemconfig(KNpom, outline='black')
    if (x <= koord['x'] + 121 and x >= koord['x'] - 21 and y <= koord['y3'] + 40 and y >= koord['y3']):
        can.itemconfig(KNzast, outline='black')
    if (x <= koord['x'] + 121 and x >= koord['x'] - 21 and y <= koord['y4'] + 40 and y >= koord['y4']):
        can.itemconfig(KNusl, outline='black')
    if (x <= koord['x'] + 121 and x >= koord['x'] - 21 and y <= koord['y5'] + 40 and y >= koord['y5']):
        can.itemconfig(KNexit, outline='black')

    can.create_text(510, 600, text='Navigate the menu items by clicking the left mouse button on the corresponding windows',anchor='c', justify='center', font='Calibri 15')


def zast():
    can.unbind ('<Button-1>')
    can.unbind ('<Motion>')
    can.delete('ALL')
    can.bind('<Button-1>',menu)
    can.create_text(510, 210, text='Simulation \n Construction of magnetic induction lines of the field, \n created by a toroidal coil\n 2018-2019',font='Calibri 25', anchor='c', justify='center')  # Just the main title
    can.create_text(510, 400, text='Performed by: Kirill Teslenko 10G', font='Calibri 15', anchor='c', justify='center')
    can.create_text(510, 580, text='To continue, click the left mouse button on the screen', anchor='c',justify='center', font='Calibri 15')
    can.create_line(70,100,70,600,width=5,fill='blue')
    can.create_line(70,600,950,600,width=5,fill='blue')
    can.create_line(950,600,950,100,width=5,fill='blue')
    can.create_line(950,100,70,100,width=5,fill='blue')
    root.update()
zast()
root.mainloop ()
