from tkinter import *

num = ""

def mainwindow():
    root = Tk()
    root.geometry("500x800")
    root.title('Calculator')
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=2)
    root.columnconfigure((0,1,2,3,4,5), weight=1)
    return root

def createframe(root):
    topframe = Frame(root, bg='#17181A')
    topframe.grid(row=0, column=0, columnspan=6, sticky='news')

    bottomframe  = Frame(root, bg='#17181A')
    bottomframe .grid(row=1, column=0, columnspan=6, sticky='news')

    return topframe, bottomframe

def widgettop(topframe):
    topframe.rowconfigure(0,weight=1)
    topframe.columnconfigure(0,weight=1)
    lb_total = Label(topframe, text='0.0', bg='#17181A',fg='#ffffff',font=("Product Sans", 50, "bold"), textvariable=txt_total)
    lb_total.grid(row=0,column=0, sticky='news')


def widgetbottom(bottomframe):
    bottomframe.rowconfigure((0,1,2,3,4,5),weight=1)
    bottomframe.columnconfigure((0,1,2,3,4,5),weight=1)  
    #row1
    button_ac = Button(bottomframe, image=img_ac, activebackground='#17181A', bg='#17181A', bd=0, command=clear())
    button_ac.grid(row=0,column=1,padx=5)
    button_c = Button(bottomframe, image=img_c, activebackground='#17181A', bg='#17181A', bd=0, command=clear())
    button_c.grid(row=0,column=2,padx=5)
    button_presence = Button(bottomframe, image=img_presence, activebackground='#17181A', bg='#17181A', bd=0,command=lambda: press("%"))
    button_presence.grid(row=0,column=3,padx=5)
    button_p = Button(bottomframe, image=img_p, activebackground='#17181A', bg='#17181A', bd=0,command=lambda: press("/"))
    button_p.grid(row=0,column=4,padx=5)

    #row2
    button_7 = Button(bottomframe, image=img_7, activebackground='#17181A', bg='#17181A', bd=0,command=lambda: press(7))
    button_7.grid(row=1,column=1,padx=5)
    button_8 = Button(bottomframe, image=img_8, activebackground='#17181A', bg='#17181A', bd=0,command=lambda: press(8))
    button_8.grid(row=1,column=2,padx=5)
    button_9 = Button(bottomframe, image=img_9, activebackground='#17181A', bg='#17181A', bd=0,command=lambda: press(9))
    button_9.grid(row=1,column=3,padx=5)
    button_x = Button(bottomframe, image=img_x, activebackground='#17181A', bg='#17181A', bd=0,command=lambda: press("*"))
    button_x.grid(row=1,column=4,padx=5)

    #row3
    button_4 = Button(bottomframe, image=img_4, activebackground='#17181A', bg='#17181A', bd=0,command=lambda: press(4))
    button_4.grid(row=2,column=1,padx=5)
    button_5 = Button(bottomframe, image=img_5, activebackground='#17181A', bg='#17181A', bd=0,command=lambda: press(5))
    button_5.grid(row=2,column=2,padx=5)
    button_6 = Button(bottomframe, image=img_6, activebackground='#17181A', bg='#17181A', bd=0,command=lambda: press(6))
    button_6.grid(row=2,column=3,padx=5)
    button_minus = Button(bottomframe, image=img_minus, activebackground='#17181A', bg='#17181A', bd=0,command=lambda: press("-"))
    button_minus.grid(row=2,column=4,padx=5)

    #row4
    button_1 = Button(bottomframe, image=img_1, activebackground='#17181A', bg='#17181A', bd=0,command=lambda: press(1))
    button_1.grid(row=3,column=1,padx=5)
    button_2 = Button(bottomframe, image=img_2, activebackground='#17181A', bg='#17181A', bd=0,command=lambda: press(2))
    button_2.grid(row=3,column=2,padx=5)
    button_3 = Button(bottomframe, image=img_3, activebackground='#17181A', bg='#17181A', bd=0,command=lambda: press(3))
    button_3.grid(row=3,column=3,padx=5)
    button_plus = Button(bottomframe, image=img_plus, activebackground='#17181A', bg='#17181A', bd=0,command=lambda: press("+"))
    button_plus.grid(row=3,column=4,padx=5)

    #row5
    button_0 = Button(bottomframe, image=img_0, activebackground='#17181A', bg='#17181A', bd=0,command=lambda: press(0))
    button_0.grid(row=4,column=1,columnspan=2,padx=5)
    button_dot = Button(bottomframe, image=img_dot, activebackground='#17181A', bg='#17181A', bd=0,command=lambda: press("."))
    button_dot.grid(row=4,column=3,padx=5)
    button_total = Button(bottomframe, image=img_total, activebackground='#17181A', bg='#17181A', bd=0,command=equalpress)
    button_total.grid(row=4,column=4,padx=5)

def press(num):
    


root = mainwindow()

txt_total = StringVar()
txt_total.set('0.0')

img_icon = PhotoImage(file="images/Logo.png")
root.iconphoto(FALSE,img_icon)
img_0 = PhotoImage(file="images/0.png")
img_1 = PhotoImage(file="images/1.png")
img_2 = PhotoImage(file="images/2.png")
img_3 = PhotoImage(file="images/3.png")
img_4 = PhotoImage(file="images/4.png")
img_5 = PhotoImage(file="images/5.png")
img_6 = PhotoImage(file="images/6.png")
img_7 = PhotoImage(file="images/7.png")
img_8 = PhotoImage(file="images/8.png")
img_9 = PhotoImage(file="images/9.png")
img_ac = PhotoImage(file="images/ac.png")
img_c = PhotoImage(file="images/c.png")
img_presence = PhotoImage(file="images/presence.png")
img_p = PhotoImage(file="images/p.png")
img_x = PhotoImage(file="images/x.png")
img_minus = PhotoImage(file="images/minus.png")
img_plus = PhotoImage(file="images/plus.png")
img_dot = PhotoImage(file="images/dot.png")
img_total = PhotoImage(file="images/total.png")


topframe, bottomframe = createframe(root)
widgettop(topframe)
widgetbottom(bottomframe)

root.mainloop()
