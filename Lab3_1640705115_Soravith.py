from tkinter import *
from tkinter import messagebox

def mainwindow():
    root = Tk()
    root.geometry("900x650")
    root.config(bg='#ffffff')
    root.title("Sales Dashboard")
    root.columnconfigure((0,1,2), weight=1)
    root.rowconfigure(0,weight=1)
    root.rowconfigure(1,weight=8)
    root.rowconfigure(2,weight=2)
    return(root)

def createframe(root):
    f1 = Frame(root,bg='#008ce3')
    f1.columnconfigure(0,weight=1)
    f1.rowconfigure(0,weight=1)
    f1.grid(row=0,columnspan=3,sticky="NEWS")

    f2 = Frame(root,bg='#ffffff')
    f2.columnconfigure((0,1),weight=1)
    f2.rowconfigure(0,weight=1)
    f2.rowconfigure(1,weight=1)
    f2.rowconfigure(2,weight=3)
    f2.grid(row=1,column=0,sticky="NEWS")

    f3 = Frame(root,bg='#ffffff')
    f3.columnconfigure((0,1),weight=1)
    f3.rowconfigure(0,weight=1)
    f3.rowconfigure(1,weight=1)
    f3.rowconfigure(2,weight=3)
    f3.grid(row=1,column=1,sticky="NEWS")

    f4 = Frame(root,bg='#ffe554')
    f4.columnconfigure(0,weight=1)
    f4.rowconfigure(0,weight=1)
    f4.grid(row=1,column=2,sticky="NEWS")

    f5 = Frame(root,bg='#FC997C')
    f5.columnconfigure((0,1,2,3),weight=1)
    f5.rowconfigure(0,weight=1)
    f5.grid(row=2,columnspan=3,sticky="NEWS")

    return(root,f1,f2,f3,f4,f5)

def widgetop(f1):
    title = Label(f1, text="Sales Dashboard by Soravith", fg='white', bg='#396EB0')
    title.configure(font=("Product Sans", 20, "bold"))
    title.grid(row=0, columnspan=2, sticky='NEWS')

def widgetleft(f2):
    tag1 = Label(f2, text="Revenue\n\n917,000", bg='#28A745', width=1, height=1, bd=0, fg='white')
    tag1.configure(font=("Product Sans", 12, "bold"))
    tag1.grid(row=0, column=0, padx=2, pady=5, sticky='news')
    
    tag2 = Label(f2, text="Revenue\n\n898", bg='#FFC107', width=1, height=1, bd=0, fg='white')
    tag2.configure(font=("Product Sans", 12, "bold"))
    tag2.grid(row=0, column=1, padx=2, pady=5, sticky='news')

    text = Label(f2, text="Top Channels", bg='#ffffff')
    text.configure(font=("Product Sans", 20, "bold"))
    text.place(x=5, y=120)

    img1 = Label(f2, image=img_chanels, width=300, height=190, bg='#ffffff')
    img1.place(x=4, y=160)

def widgetcenter(f3):
    tag1 = Label(f3, text="Avg. Order Value\n\n1,021", bg='#17A2B8', width=1, height=1, bd=0, fg='white')
    tag1.configure(font=("Product Sans", 12, "bold"))
    tag1.grid(row=0, column=0, padx=2, pady=5, sticky='news')
    
    tag2 = Label(f3, text="Customers\n\n819", bg='#DC3545', width=1, height=1, bd=0, fg='white')
    tag2.configure(font=("Product Sans", 12, "bold"))
    tag2.grid(row=0, column=1, padx=2, pady=5, sticky='news')
    
    text1 = Label(f3, text="Bestsellers", bg='#ffffff')
    text1.configure(font=("Product Sans", 20, "bold"))
    text1.place(x=5, y=120)

    detail = Text(f3, fg='black',bg='#ffffff', width=30, height=20, bd=0)
    detail.insert(INSERT,"""\n1. Le Chiquito Bag\n\n2. Fendi FF Mask\n\n3. Raito Racer Sneakers\n\n4. Carty Mini Bag\n\n5. Eva Shoulder Bag - Ivory Croc """)
    detail.configure(font=("Product Sans", 10, "bold"))
    detail.place(x=10, y=160)

def widgetright(f4):
    frame = LabelFrame(f4, text="Device", bg='#ffffff')
    frame.grid(row=0, sticky='NEWS')
    img = Label(frame, image=img_device, bd=0)
    img.place(x=0, y=0)

def widgebottom(f5):
    b1 = Button(f5, text="Click Me1", compound='center', bg='#FC997C', bd=0, image=img_button, activebackground='#FC997C', command=fnclick1)
    b1.configure(font=("Product Sans", 12, "bold"))
    b1.grid(row=0, column=0)

    b2 = Button(f5, text="Click Me2", compound='center', bg='#FC997C', bd=0, image=img_button, activebackground='#FC997C', command=fnclick2)
    b2.configure(font=("Product Sans", 12, "bold"))
    b2.grid(row=0, column=1)
    
    b3 = Button(f5, text="Click Me3", compound='center', bg='#FC997C', bd=0, image=img_button, activebackground='#FC997C', command=fnclick3)
    b3.configure(font=("Product Sans", 12, "bold"))
    b3.grid(row=0, column=2)

    b4 = Button(f5, text="Exit Program", compound='center', bg='#FC997C', bd=0, image=img_button, activebackground='#FC997C', command=exit)
    b4.configure(font=("Product Sans", 12, "bold"))
    b4.grid(row=0, column=3)

def fnclick1():
    messagebox.showinfo("Soravith said:","Click Me 1 clicked")

def fnclick2():
    messagebox.showinfo("Soravith said:","Click Me 2 clicked")

def fnclick3():
    messagebox.showinfo("Soravith said:","Click Me 3 clicked")

root = mainwindow()

img_button = PhotoImage(file="img\Button.png")
img_device = PhotoImage(file="img\device.png")
img_chanels = PhotoImage(file="img\chanels.png")

img_icon = PhotoImage(file="img\git.png")
root.iconphoto(FALSE,img_icon)

root,f1,f2,f3,f4,f5 = createframe(root)

widgetop(f1)
widgetleft(f2)
widgetcenter(f3)
widgetright(f4)
widgebottom(f5)

root.mainloop()