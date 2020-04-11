# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 17:15:48 2019

@author: Ajayi Raymond T
"""

from tkinter import *
from PIL import Image,ImageTk
from tkinter.filedialog import askopenfilename,asksaveasfilename
from tkinter.messagebox import askquestion,showinfo
import math

lastx = lasty = drawLine = bulbimg = bulbid = line_id = item_id = imageitem= None
filename= ''
start = None
center = [100, 100]
        
root = Tk()

root.title(' Shugar-eSim')
#loadrub = Image.open('Rubix.png')
#renderrub = ImageTk.PhotoImage(loadrub)
#root.wm_iconbitmap(renderrub)

motionbar = Frame(root,bd = 2, relief = 'raised')
motionbar.grid_propagate(0)
motionbar.pack(side='top',anchor='w') 

toolbar = Frame(root,bd = 2, relief = 'raised')
toolbar.grid_propagate(0)
toolbar.pack(side='top',anchor='w')

body= Frame(root,bg='white')
body.pack(side='top')
canva = Canvas(body,height = 560, width = 1100, bg='lightgray')
canva.grid(row =0,column=0)
scrolly = Scrollbar (body, orient = 'vertical', command = canva.yview)
scrollx = Scrollbar (body, orient = 'horizontal', command = canva.xview)
scrolly.grid(row =0, column = 1, sticky = 'ns')
scrollx.grid(row = 1, column = 0, sticky ='ew')
canva.configure(yscrollcommand = scrolly.set)
canva.configure(xscrollcommand = scrollx.set)
canva.postscript ( rotate = True )

def newpage():
    global filename
    root.title('Untitled Shugar-eSim')
    filename = None
    canvas.delete(1.0,'end')
def openf():
    filename = askopenfilename(defaultextension = '.png',filetypes = [('All Files','*.*'),('Text files','.png')])
    if filename == '':
        filename = None
    else:
        loadn = Image.open(filename)
        rendern = ImageTk.PhotoImage(loadn, master = root)
        canvas.create_image(50,50, image= rendern,)
        filename.close()
def save():
    global filename
    filename= asksaveasfilename(filetypes = [('All Files',('.png'))])
    if filename=='':
             if filename=='':
                filename= None
             else:
                s = open(filename,'w')
                s.write(canva.get(1.0,'end'))
                filename.close()
    else:
            s = open(filename,'w')
            s.write(canva.get(1.0,'end'))
            filename.close()
def saveas():
    global filename
    filename= asksaveasfilename(filetypes = [('All Files',('.png'))])
    if filename == '':
        filename = None
    else:
        s = open(filename,'w')
        s.write(canva.get(1.0,'end'))
        filename.close()
def pgst():
    pass
def delete():
    canva.delete(ALL)
def prnt():
    pass
def Quit():
    answer = askquestion(title='Quit?', message='Are you sure?')
    if answer=='yes':
        root.destroy()
def menu():
    pass

def createImage(value):
    global imageitem, bulbimg, bulbid
    imageitem = canva.create_image(30, 30, image = value, tag=value)
    if(value == bulbimg):
       bulbid = imageitem
    '''def showImage():
         #dim = dimval.get().split(',')
         canva.create_arc(30, 30, 30, 30, start=0, extent=150, fill='red')
         inputval.destroy()
    if str(event.type) == 'Buttonpress':
        pass
    else:
    inputval = Toplevel()
    inputval.grid_propagate(0)
    dimval = StringVar()
    Label(inputval, text="Enter capacity").pack(side=LEFT, expand=YES, fill=BOTH)
    findw = Entry(inputval, width=50, textvariable=dimval)
    findw.focus_set()
    findw.pack(side=LEFT, expand=YES, fill=BOTH, padx=3)
    Button(inputval, text='Enter', width=10, command=showImage).pack(side=LEFT, expand=YES, fill=BOTH, padx=3)
'''
def mouseDown(event):
    global lastx, lasty, imageitem, item_id
    item_id = canva.find_withtag(CURRENT)
    lastx = event.x
    lasty = event.y
def mouseMove(event):
    global lastx, lasty
    canva.move(CURRENT, event.x - lastx, event.y - lasty)
    lastx = event.x
    lasty = event.y

def resizeLine():
    global item_id
    if item_id:
        cordx, cordy, ofsetx, ofsety = canva.coords(item_id)
        lnscale = float(linesize.get())
        canva.scale(item_id, 0, 0, ofsetx  +lnscale, ofsety +lnscale)

def createLine():
    global line_id
    canva.configure(cursor = "plus")
    coords = {"x":0,"y":0,"x2":0,"y2":0}
    # keep a reference to all lines by keeping them in a list 
    lines = []
    def click(event):
        global line_id
        # define start point for line
        coords["x"] = event.x
        coords["y"] = event.y 
        # create a line on this point and store it in the list
        line_id = lines.append(canva.create_line(coords["x"],coords["y"],coords["x"],coords["y"], tag="linetag", activefill='blue'))
       
    def drag(event):
        # update the coordinates from the event
        coords["x2"] = event.x
        coords["y2"] = event.y
        # Change the coordinates of the last created line to the new coordinates
        canva.coords(lines[-1], coords["x"],coords["y"],coords["x2"],coords["y2"])
    
    canva.bind("<ButtonPress-1>", click)
    canva.bind("<B1-Motion>", drag)
    
def changeCursor():
    global drawLine
    Widget.unbind(canva, "<B1-Motion>", drawLine)
    canva.configure(cursor = "arrow")
    Widget.bind(canva, "<B1-Motion>", mouseMove)
    Widget.bind(canva, "<1>", mouseDown)
    
 
def cursorChange(envent):
    canva.itemconfig(CURRENT, cursor="tcross")
def drawStraightLine():
    canva.create_line(300, 35, 300, 200, dash = (5, 2), activefill='blue')

def rotate_clockwise():
    global item_id
    cordx, cordy, ofsetx, ofsety = canva.coords(item_id)
    canva.coords(item_id, cordx+5, cordy+5, ofsetx+5, ofsety+5)

def rotate_anticlockwise():
    global item_id
    cordx, cordy, ofsetx, ofsety = canva.coords(item_id)
    canva.coords(item_id, cordx-5, cordy-5, ofsetx-5, ofsety-5)
    
newbulb = Image.open('sim/Globe Bulb.png')
newbulb = ImageTk.PhotoImage(newbulb, master = root)
def play_motion():
    global bulbid
    canva.itemconfig(bulbid, image= newbulb)
    canva.itemconfigure("linetag", fill='red')
    
def stop_motion():
     canva.itemconfig(bulbid, image= bulbimg)
     canva.itemconfigure("linetag", fill='black')

def deleteimg():
    global item_id
    canva.delete(item_id)

loadnw = Image.open('sim/newfile.png')
rendernw = ImageTk.PhotoImage(loadnw, master = root)
btnnw = Button(motionbar, image= rendernw, command = newpage)
btnnw.pack(side= 'left',anchor= 'w')

loadop = Image.open('sim/openw.png')
renderop = ImageTk.PhotoImage(loadop, master = root)
btnop = Button(motionbar,image= renderop,command = openf)
btnop.pack(side= 'left',anchor= 'w')

loadsv = Image.open('sim/wsave.png')
rendersv = ImageTk.PhotoImage(loadsv, master = root)
btnsv = Button(motionbar,image= rendersv,command =save)
btnsv.pack(side= 'left',anchor= 'w')

loadpr = Image.open('sim/print.png')
renderpr = ImageTk.PhotoImage(loadpr, master = root)
btnpr = Button(motionbar,image= renderpr)
btnpr.pack(side= 'left',anchor= 'w')

loadcle = Image.open('sim/cancel.png')
rendercle = ImageTk.PhotoImage(loadcle, master = root)
btncle = Button(motionbar,image= rendercle, command=deleteimg)
btncle.pack(side= 'left',anchor= 'w')

loadpl = Image.open('sim/bplay.png')
renderpl = ImageTk.PhotoImage(loadpl, master = root)
btnpl = Button(motionbar,image= renderpl, command =play_motion)
btnpl.pack(side= 'left',anchor= 'w')

loadstp = Image.open('sim/stop.png')
renderstp = ImageTk.PhotoImage(loadstp, master = root)
btnstp = Button(motionbar,image= renderstp, command = stop_motion)
btnstp.pack(side= 'left',anchor= 'w')

loadwd = Image.open('sim/brewind.png')
renderwd = ImageTk.PhotoImage(loadwd, master = root)
btnwd = Button(motionbar,image= renderwd)
btnwd.pack(side= 'left',anchor= 'w')

loadfw = Image.open('sim/bff.png')
renderfw = ImageTk.PhotoImage(loadfw, master = root)
btnfw = Button(motionbar,image= renderfw)
btnfw.pack(side= 'left',anchor= 'w')

loadud = Image.open('sim/bundo.png')
renderud = ImageTk.PhotoImage(loadud, master = root)
btnud = Button(motionbar,image= renderud, command = rotate_anticlockwise)
btnud.pack(side= 'left',anchor= 'w')

loadrd = Image.open('sim/bredo.png')
renderrd = ImageTk.PhotoImage(loadrd, master = root)
btnrd = Button(motionbar,image= renderrd, command = rotate_clockwise)
btnrd.pack(side= 'left',anchor= 'w')

loadmn = Image.open('sim/menu.png')
rendermn = ImageTk.PhotoImage(loadmn, master = root)
btnmn = Button(motionbar,image= rendermn)
btnmn.pack(side= 'left',anchor= 'w')

resistorimg = Image.open('sim/Resistor.png')
resistorimg = ImageTk.PhotoImage(resistorimg, master = root)
btnresistor = Button(toolbar,image= resistorimg, command= lambda: createImage(resistorimg))
btnresistor.pack(side= 'left',anchor= 'w') 

batteryimg = Image.open('sim/Low Battery.png')
batteryimg = ImageTk.PhotoImage(batteryimg, master = root)
btnbattery = Button(toolbar,image= batteryimg, command= lambda: createImage(batteryimg))
btnbattery.pack(side= 'left',anchor= 'w') 

bulbimg = Image.open('sim/Light Off.png')
bulbimg = ImageTk.PhotoImage(bulbimg, master = root)
btnbulb = Button(toolbar,image= bulbimg, command= lambda: createImage(bulbimg))
btnbulb.pack(side= 'left',anchor= 'w') 

lineimg = Image.open('sim/cedit.png')
lineimg = ImageTk.PhotoImage(lineimg, master = root)
btnline = Button(toolbar,image= lineimg, command= createLine)
btnline.pack(side= 'left',anchor= 'w') 

line2img = Image.open('sim/Edit.png')
line2img = ImageTk.PhotoImage(line2img, master = root)
btnline2 = Button(toolbar,image= line2img, command= drawStraightLine)
btnline2.pack(side= 'left',anchor= 'w') 

cursorimg = Image.open('sim/Cursor.png')
cursorimg = ImageTk.PhotoImage(cursorimg, master = root)
btncursor = Button(toolbar,image= cursorimg, command= changeCursor)
btncursor.pack(side= 'left',anchor= 'w') 

Label(toolbar, text="Line length:").pack(side="left", anchor="w")
linesize = Spinbox(toolbar, from_= 0, to = 10, width = 5, increment=0.1, command=resizeLine)
linesize.pack(side= 'left',anchor= 'w')

menubar = Menu(root)
fileMenu = Menu(menubar, tearoff=0,bg='white')
fileMenu.add_command(label = 'New',command=newpage, accelerator = 'Ctrl+N',image=rendernw, compound='left')
fileMenu.add_command(label = 'Open...',command=openf , accelerator = 'Ctrl+O',image=renderop, compound='left')
fileMenu.add_command(label = 'Save',command=save , accelerator = 'Ctrl+S',image=rendersv, compound='left')
loadsvas = Image.open('sim/saveas.png')
rendersvas = ImageTk.PhotoImage(loadsvas, master = root)
fileMenu.add_command(label = 'Save As...',command=saveas,image=rendersvas, compound='left')
fileMenu.add_separator()
loaddel = Image.open('sim/cancel.png')
renderdel = ImageTk.PhotoImage(loaddel, master = root)
fileMenu.add_command(label = 'Delete',command=delete , accelerator = '     Del', image= renderdel,compound= 'left')
fileMenu.add_command(label = 'Print',command=prnt,image= renderpr,compound= 'left',  accelerator = 'Ctrl+P')
fileMenu.add_separator()
loadex = Image.open('sim/bexit.png')
renderex = ImageTk.PhotoImage(loadex, master = root)
fileMenu.add_command(label = 'Exit',command=Quit,image= renderex,compound= 'left')
menubar.add_cascade(label = 'File',menu = fileMenu,underline = 0)
root.config(menu = menubar)

editMenu = Menu(menubar, tearoff=0,bg='white')
loadcp = Image.open('sim/bcopy.png')
rendercp = ImageTk.PhotoImage(loadcp, master = root)
editMenu.add_command(label = 'Copy',command=newpage, accelerator = 'Ctrl+C',image= rendercp,compound= 'left')
loadps = Image.open('sim/bpaste.png')
renderps = ImageTk.PhotoImage(loadps, master = root)
editMenu.add_command(label = 'Paste',command=openf , accelerator = 'Ctrl+V',image= renderps,compound= 'left')
editMenu.add_separator()
editMenu.add_command(label = 'Undo',command=save , accelerator = 'Ctrl+Z',image= renderud,compound= 'left')
editMenu.add_command(label = 'Redo',command=saveas, accelerator = 'Ctrl+Shift+Z',image=renderrd, compound='left')
menubar.add_cascade(label = 'Edit',menu = editMenu,underline = 0)
root.config(menu = menubar)

Widget.bind(canva, "<1>", mouseDown)
Widget.bind(canva, "<B1-Motion>", mouseMove)

root.mainloop()