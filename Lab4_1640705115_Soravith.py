from tkinter import *

def mainwindow():
    root = Tk()
    root.geometry("1000x800")
    root.title('LAB4: My Sweety cake shop by Soravith Puvekit')
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=10)
    root.rowconfigure(2, weight=2)
    root.columnconfigure((0,1), weight=1)
    return root

def createframe(root):
    topframe = Frame(root, bg='#FFC4E1')
    topframe.grid(row=0, column=0, columnspan=2, sticky='news')
    
    leftframe = LabelFrame(root, text='Cake Menu', bg='#FFEDDB', font=("Product Sans", 13, "bold"))
    leftframe.grid(row=1, column=0, sticky='news')
    
    rightframe = LabelFrame(root, text='Checkout', bg='#FFEDDB', font=("Product Sans", 13, "bold"))
    rightframe .grid(row=1, column=1, sticky='news')

    bottomframe  = Frame(root, bg='#FFC4E1')
    bottomframe .grid(row=2, column=0, columnspan=2, sticky='news')
    
    return (root, topframe, leftframe, rightframe, bottomframe)

def widgettop(topframe):
    topframe.columnconfigure(0,weight=1)
    topframe.rowconfigure(0,weight=1)
    title = Label(topframe, text="My cake shop", fg='#FFF9F9', bg='#FFC4E1', font=("Product Sans", 25, "bold"))
    title.grid(row=0, column=0, sticky='NEWS')

def widgetleft(leftframe):
    leftframe.columnconfigure((0,1), weight=1)
    leftframe.rowconfigure((0,1,2,3,4,5), weight=1)
    lb_img_cake1 = Label(leftframe, image=img_cake1, bg='#FFEDDB')
    lb_img_cake1.grid(row=0, column=0, rowspan=2, pady=5)
    lb_cake1 = Label(leftframe, text='Carrot cake Cheesecake\nPrice 180 bahts', bg='#FFEDDB', font=("Product Sans", 12, "bold"))
    lb_cake1.grid(row=0, column=1)
    spin_cake1 = Spinbox(leftframe, from_=0, to=10, width=10, justify=CENTER, fg='#BF9270', bd=0, font=("Product Sans", 12, "bold"))
    spin_cake1.grid(row=1, column=1, ipady=5)
    

    lb_img_cake2 = Label(leftframe, image=img_cake2, bg='#FFEDDB')
    lb_img_cake2.grid(row=2, column=0, rowspan=2, pady=5)
    lb_cake2 = Label(leftframe, text='Chocolate rose Cake\nPrice 250 bahts', bg='#FFEDDB', font=("Product Sans", 12, "bold"))
    lb_cake2.grid(row=2, column=1)
    spin_cake2 = Spinbox(leftframe, from_=0, to=10, width=10, justify=CENTER, fg='#BF9270', bd=0, font=("Product Sans", 12, "bold"))
    spin_cake2.grid(row=3, column=1, ipady=5)


    lb_img_cake3 = Label(leftframe, image=img_cake3, bg='#FFEDDB')
    lb_img_cake3.grid(row=4, column=0, rowspan=2, pady=5)
    lb_cake3 = Label(leftframe, text='Raspberry chocolate Cake\nPrice 380 bahts', bg='#FFEDDB', font=("Product Sans", 12, "bold"))
    lb_cake3.grid(row=4, column=1)

    spin_cake3 = Spinbox(leftframe, from_=0, to=10, width=10, justify=CENTER, fg='#BF9270', bd=0, font=("Product Sans", 12, "bold"))
    spin_cake3.grid(row=5, column=1, ipady=5)

    btn_checkout = Button(leftframe, text='Checkout', 
                                    image=img_cart, 
                                    compound=LEFT, 
                                    bd=0, 
                                    bg='#FFFFFF', 
                                    pady=5, 
                                    padx=10, 
                                    fg='#BF9270',
                                    activebackground='#FFC4E1', 
                                    font=("Product Sans", 15, "bold"),
                                    command=checkout)
    btn_checkout.grid(row=6,columnspan=2,sticky='NEWS')

    return spin_cake1 , spin_cake2 , spin_cake3

def widgetright(rightframe):
    rightframe.columnconfigure((0,1), weight=1)
    lb_chk_cake1 = Label(rightframe, text="Carrot cake Cheesecake\nPrice 180 bahts", bg='#FFEDDB', font=("Product Sans", 12, "bold"))
    lb_chk_cake1.grid(row=0, column=0)
    ent_cake1 = Entry(rightframe, width=10, justify=CENTER, fg='#54BAB9', bd=0, font=("Product Sans", 12, "bold"))
    ent_cake1.grid(row=0, column=1, padx=30, pady=50, ipady=5)

    lb_chk_cake2 = Label(rightframe, text="Chocolate rose Cake\nPrice 250 bahts", bg='#FFEDDB', font=("Product Sans", 12, "bold"))
    lb_chk_cake2.grid(row=1, column=0)
    ent_cake2 = Entry(rightframe, width=10, justify=CENTER, fg='#54BAB9', bd=0, font=("Product Sans", 12, "bold"))
    ent_cake2.grid(row=1, column=1, padx=30, pady=50, ipady=5)
    
    lb_chk_cake3 = Label(rightframe, text="Raspberry chocolate Cake\nPrice 380 bahts", bg='#FFEDDB', font=("Product Sans", 12, "bold"))
    lb_chk_cake3.grid(row=2, column=0)
    ent_cake3 = Entry(rightframe, width=10, justify=CENTER, fg='#54BAB9', bd=0, font=("Product Sans", 12, "bold"))
    ent_cake3.grid(row=2, column=1, padx=30, pady=50, ipady=5)

    lb_chk_total = Label(rightframe, text="Total Price :", bg='#FFEDDB', fg='#54BAB9', font=("Product Sans", 20, "bold"))
    lb_chk_total.grid(row=4, column=0)
    ent_total = Entry(rightframe, width=10, justify=CENTER, bg='#54BAB9', fg='#FFFFFF', bd=0, font=("Product Sans", 12, "bold"))
    ent_total.grid(row=4, column=1, padx=30, pady=50, ipady=5,)

    return ent_cake1 , ent_cake2 , ent_cake3 , ent_total

def widgetbottom(bottomframe):
    bottomframe.columnconfigure(0,weight=1)
    bottomframe.rowconfigure(0,weight=1)
    button_exit = Button(bottomframe, text="Exit Program", 
                                    image=img_exit, 
                                    activebackground='#FFC4E1',
                                    fg='#FF6464',
                                    bg='#FDEBF7',
                                    compound='left', 
                                    height=80, 
                                    width=180, 
                                    bd=0, 
                                    font=("Product Sans", 12, "bold"),
                                    padx=5,
                                    command=exit)
    button_exit.grid(row=0,column=1,padx=30)

def checkout():
    print('Checkout click')
    
    quantity1 = int(spin_cake1.get())
    quantity2 = int(spin_cake2.get())
    quantity3 = int(spin_cake3.get())

    total_cake1 = (180 * quantity1)
    total_cake2 = (250 * quantity2)  
    total_cake3 = (380 * quantity3)      

    total_all = (total_cake1 + total_cake2  + total_cake3)
    
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
    str_total.set("%0.2f"%total_all)
    ent_total['text'] = str_total
    
    print(total_cake1)
    print(total_cake2)
    print(total_cake3)
    print(total_all)

root = mainwindow()

img_icon = PhotoImage(file="images/heart.png")
root.iconphoto(FALSE,img_icon)

img_exit = PhotoImage(file="images\exit.png")
img_cake1 = PhotoImage(file="images\cake1.png")
img_cake2 = PhotoImage(file="images\cake2.png")
img_cake3 = PhotoImage(file="images\cake3.png")
img_cart = PhotoImage(file="images\cart.png")

root, topframe, leftframe, rightframe, bottomframe = createframe(root)
widgettop(topframe)
spin_cake1 , spin_cake2 , spin_cake3 = widgetleft(leftframe)
ent_cake1 , ent_cake2 , ent_cake3 , ent_total = widgetright(rightframe)
widgetbottom(bottomframe)

root.mainloop()
