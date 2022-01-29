from tkinter import *
from tkinter import messagebox

def mainwindow():
    root = Tk()
    root.title("Sales Dashboard")
    root.geometry("900x650")
    root.config(bg='#ffffff')
    root.rowconfigure(0,weight=1)
    root.rowconfigure(1,weight=5)
    root.rowconfigure(2,weight=2)
    root.columnconfigure((0,1,2), weight=1)
    return(root)

def createframe(root):
    frame1 = Frame(root,bg='#ff00e1')
    frame1.columnconfigure(0,weight=1)
    frame1.rowconfigure(0,weight=1)
    frame2 = Frame(root,bg='#ffffff')
    frame2.columnconfigure((0,1),weight=1)
    frame2.rowconfigure(0,weight=1)
    frame2.rowconfigure(1,weight=1)
    frame2.rowconfigure(2,weight=3)
    frame3 = Frame(root,bg='#ffffff')
    frame3.columnconfigure((0,1),weight=1)
    frame3.rowconfigure(0,weight=1)
    frame3.rowconfigure(1,weight=1)
    frame3.rowconfigure(2,weight=3)
    frame4 = Frame(root,bg='#004cff')
    frame4.columnconfigure(0,weight=1)
    frame4.rowconfigure(0,weight=1)
    frame5 = Frame(root,bg='#17e848')
    frame5.columnconfigure((0,1,2,3),weight=1)
    frame5.rowconfigure(0,weight=1)
    
    frame1.grid(row=0,columnspan=3,sticky="NEWS")
    frame2.grid(row=1,column=0,sticky="NEWS")
    frame3.grid(row=1,column=1,sticky="NEWS")
    frame4.grid(row=1,column=2,sticky="NEWS")
    frame5.grid(row=2,columnspan=3,sticky="NEWS")

    return(root,frame1,frame2,frame3,frame4,frame5)

def infoclick1():
    messagebox.showinfo("Varissara said:","Click Me 1 clicked")
def infoclick2():
    messagebox.showinfo("Varissara said:","Click Me 2 clicked")
def infoclick3():
    messagebox.showinfo("Varissara said:","Click Me 3 clicked")

def widgetop(frame1):
    title = Label(frame1, text="Sales Dashboard by Varissara", fg='white', bg='#396EB0',font='sarabun')
    title.grid(row=0, columnspan=2, sticky='NEWS')

def widgetleft(frame2):
    bg1 = Label(frame2, text="Revenue\n\n917,000", bg='#28A745', width=1, height=1, bd=0, fg='white',font='sarabun')
    bg2 = Label(frame2, text="Revenue\n\n898", bg='#FFC107', width=1, height=1, bd=0, fg='white',font='sarabun')
    text = Label(frame2, text="Top Channels", bg='#ffffff',font='sarabun')
    img1 = Label(frame2, image=image_chanels, bg='#ffffff', width=300, height=190)
    
    bg1.grid(row=0, column=0, padx=2, pady=5, sticky='news')
    bg2.grid(row=0, column=1, padx=2, pady=5, sticky='news')
    img1.place(x=4, y=160)
    text.place(x=5, y=120)

def widgetcenter(frame3):
    bg1 = Label(frame3, text="Avg. Order Value\n\n1,021", bg='#17A2B8', width=1, height=1, bd=0, fg='white',font='sarabun')
    bg2 = Label(frame3, text="Customers\n\n819", bg='#DC3545', width=1, height=1, bd=0, fg='white',font='sarabun')
    text1 = Label(frame3, text="Bestsellers", bg='#ffffff',font='sarabun')
    detail = Text(frame3, fg='black',bg='#ffffff', width=30, height=20, bd=0,font='sarabun')
    detail.insert(INSERT,"""\n1. Le Chiquito Bag\n\n2. Fendi FF Mask\n\n3. Raito Racer Sneakers\n\n4. Carty Mini Bag\n\n5. Eva Shoulder Bag - Ivory Croc """)
    bg1.grid(row=0, column=0, padx=2, pady=5, sticky='news')
    bg2.grid(row=0, column=1, padx=2, pady=5, sticky='news')
    text1.place(x=5, y=120)
    detail.place(x=10, y=160)

def widgetright(frame4):
    framelabel = LabelFrame(frame4, text="Device", bg='#ffffff' ,font='sarabun')
    img = Label(framelabel, image=image_device, bd=0 ,font='sarabun')
    framelabel.grid(row=0, sticky='NEWS')
    img.place(x=0, y=0)

def widgebottom(frame5): 
    Button1 = Button(frame5, text="Click Me1", bg='#FC997C', activebackground='#FC997C', bd=0, image=image_button, compound='center',font='sarabun', command=infoclick1)
    Button2 = Button(frame5, text="Click Me2", bg='#FC997C', activebackground='#FC997C', bd=0, image=image_button, compound='center',font='sarabun', command=infoclick2)
    Button3 = Button(frame5, text="Click Me3", bg='#FC997C', activebackground='#FC997C', bd=0, image=image_button, compound='center',font='sarabun', command=infoclick3)
    Button4 = Button(frame5, text="Exit Program", bg='#FC997C', activebackground='#FC997C', bd=0, image=image_button, compound='center',font='sarabun', command=exit)
    
    Button1.grid(row=0, column=0)
    Button2.grid(row=0, column=1)
    Button3.grid(row=0, column=2)
    Button4.grid(row=0, column=3)

root = mainwindow()

image_chanels = PhotoImage(file="img\chanels.png")
image_button = PhotoImage(file="img\Button.png")
image_device = PhotoImage(file="img\device.png")
image_icon = PhotoImage(file="img\git.png")
root.iconphoto(FALSE,image_icon)

root,frame1,frame2,frame3,frame4,frame5 = createframe(root)
widgetop(frame1)
widgetleft(frame2)
widgetcenter(frame3)
widgetright(frame4)
widgebottom(frame5)
root.mainloop()