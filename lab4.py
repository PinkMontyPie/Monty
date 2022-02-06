from tkinter import *

def mainwindow():
    root = Tk()
    root.geometry("1000x800")
    root.title('LAB4: My Sweety cake shop by Varissara Tepsute')
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=10)
    root.rowconfigure(2, weight=2)
    root.columnconfigure((0,1), weight=1)
    return root

def createframe(root):
    top = Frame(root, bg='#F5F2E7')
    top.grid(row=0, column=0, columnspan=2, sticky='news')
    left = LabelFrame(root, text='Cake Menu', bg='#D885A3')
    left.grid(row=1, column=0, sticky='news')
    right = LabelFrame(root, text='Checkout', bg='#D885A3')
    right .grid(row=1, column=1, sticky='news')
    bottom = Frame(root, bg='#F5F2E7')
    bottom .grid(row=2, column=0, columnspan=2, sticky='news')
    return top, left, right, bottom

def widgettop(top):
    top.columnconfigure(0,weight=1)
    top.rowconfigure(0,weight=1)
    title = Label(top, text="My cake shop", bg='#F5F2E7', fg='#2C3333')
    title.grid(row=0, column=0, sticky='NEWS')

def widgetLeft(left):
    left.columnconfigure((0,1), weight=1)
    left.rowconfigure((0,1,2,3,4,5), weight=1)
    lb_img_cake1 = Label(left, image=img_cake1, bg='#D885A3')
    lb_img_cake1.grid(row=0, column=0, rowspan=2, pady=5)
    lb_cake1 = Label(left, text='Carrot cake Cheesecake\nPrice 180 bahts', bg='#D885A3')
    lb_cake1.grid(row=0, column=1)
    spin_cake1 = Spinbox(left, from_=0, to=10, width=10, fg='#BF9270', bd=0, justify=CENTER)
    spin_cake1.grid(row=1, column=1, ipady=5)
    

    lb_img_cake2 = Label(left, image=img_cake2, bg='#D885A3')
    lb_img_cake2.grid(row=2, column=0, rowspan=2, pady=5)
    lb_cake2 = Label(left, text='Chocolate rose Cake\nPrice 250 bahts', bg='#D885A3')
    lb_cake2.grid(row=2, column=1)
    spin_cake2 = Spinbox(left, from_=0, to=10, width=10, fg='#BF9270', bd=0, justify=CENTER)
    spin_cake2.grid(row=3, column=1, ipady=5)


    lb_img_cake3 = Label(left, image=img_cake3, bg='#D885A3')
    lb_img_cake3.grid(row=4, column=0, rowspan=2, pady=5)
    lb_cake3 = Label(left, text='Raspberry chocolate Cake\nPrice 380 bahts', bg='#D885A3')
    lb_cake3.grid(row=4, column=1)
    spin_cake3 = Spinbox(left, from_=0, to=10, width=10, fg='#BF9270', bd=0, justify=CENTER)
    spin_cake3.grid(row=5, column=1, ipady=5)

    btn_checkout = Button(left, text='Checkout', image=img_cart, compound=LEFT, bg='#FFFFFF', pady=5, padx=10, fg='#BF9270', bd=0, activebackground='#FFC4E1', command=checkout)
    btn_checkout.grid(row=6,columnspan=2,sticky='NEWS')

    return spin_cake1 , spin_cake2 , spin_cake3

def checkout():
    quan1 = int(spin_cake1.get())
    total_cake1 = (180 * quan1)
    
    quan2 = int(spin_cake2.get())
    total_cake2 = (250 * quan2) 

    quan3 = int(spin_cake3.get())
    total_cake3 = (380 * quan3)      

    total_price = (total_cake1 + total_cake2  + total_cake3)
    
    str_cake1 = StringVar()
    str_cake1.set("%0.2f"%total_cake1)
    ent_cake1['text'] = str_cake1

    str_cake2 = StringVar()
    str_cake2.set("%0.2f"%total_cake2)
    ent_cake2['text'] = str_cake2

    str_cake3 = StringVar()
    str_cake3.set("%0.2f"%total_cake3)
    ent_cake3['text'] = str_cake3
    
    str_total = StringVar()
    str_total.set("%0.2f"%total_price)
    ent_total['text'] = str_total

def widgetright(right):
    right.columnconfigure((0,1), weight=1)
    lb_chk_cake1 = Label(right, text="Carrot cake Cheesecake\nPrice 180 bahts", bg='#D885A3')
    lb_chk_cake1.grid(row=0, column=0,sticky='E')
    ent_cake1 = Entry(right, width=10, justify=CENTER, fg='#D885A3', bd=0)
    ent_cake1.grid(row=0, column=1, padx=30, pady=50, ipady=5)

    lb_chk_cake2 = Label(right, text="Chocolate rose Cake\nPrice 250 bahts", bg='#D885A3')
    lb_chk_cake2.grid(row=1, column=0,sticky='E')
    ent_cake2 = Entry(right, width=10, justify=CENTER, fg='#D885A3', bd=0)
    ent_cake2.grid(row=1, column=1, padx=30, pady=50, ipady=5)
    
    lb_chk_cake3 = Label(right, text="Raspberry chocolate Cake\nPrice 380 bahts", bg='#D885A3')
    lb_chk_cake3.grid(row=2, column=0,sticky='E')
    ent_cake3 = Entry(right, width=10, justify=CENTER, fg='#D885A3', bd=0)
    ent_cake3.grid(row=2, column=1, padx=30, pady=50, ipady=5)

    lb_chk_total = Label(right, text="Total Price :", bg='#D885A3', fg='#FFFFFF')
    lb_chk_total.grid(row=4, column=0,sticky='E')
    ent_total = Entry(right, width=10, justify=CENTER, bg='#FFFFFF', fg='#D885A3', bd=0)
    ent_total.grid(row=4, column=1, padx=30, pady=50, ipady=5,)

    return ent_cake1 , ent_cake2 , ent_cake3 , ent_total

def widgetbottom(bottom):
    bottom.columnconfigure(0,weight=1)
    bottom.rowconfigure(0,weight=1)
    button_exit = Button(bottom, text="Exit Program", image=img_exit, fg='#2C3333', bg='#ffffff', height=80, width=180, bd=0 ,padx=10, compound='left', command=exit)
    button_exit.grid(row=0,column=1,padx=30)

root = mainwindow()

img_icon = PhotoImage(file="images/heart.png")
root.iconphoto(FALSE,img_icon)

img_cake1 = PhotoImage(file="images\cake1.png")
img_cake2 = PhotoImage(file="images\cake2.png")
img_cake3 = PhotoImage(file="images\cake3.png")
img_cart = PhotoImage(file="images\cart.png")
img_exit = PhotoImage(file="images\exit.png")

top, left, right, bottom = createframe(root)
widgettop(top)
spin_cake1 , spin_cake2 , spin_cake3 = widgetLeft(left)
ent_cake1 , ent_cake2 , ent_cake3 , ent_total = widgetright(right)
widgetbottom(bottom)

root.mainloop()

