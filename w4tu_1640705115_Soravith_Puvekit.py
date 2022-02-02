# onsite
from tkinter import *

def mainwindow():
    root = Tk()
    root.geometry("800x600")
    root.title('Chicken Kuk Kuk')
    root.option_add('*font', 'Calibri 14')
    #Icon image
    root.rowconfigure((0,1), weight=1)
    root.columnconfigure((0,1), weight=1)
    return root

def createFrame(root):
    left = LabelFrame(root, text='Menu', bg='skyblue')
    left.grid(row=0, column=0, sticky='news')
    right = LabelFrame(root, text='Checkout', bg='Lightgreen')
    right.grid(row=0, column=1, sticky='news')
    bottom = Frame(root, bg='Lightgrey')
    bottom.grid(row=1, column=0, columnspan=2, sticky='news')
    return left, right, bottom

def widgetLeft(left):
    left.columnconfigure((0,1), weight= 1)
    lb_imgPart = Label(left,image=img_part, bg='skyblue')
    lb_imgPart.grid(row=0, column=0,rowspan=2,pady=5)
    lb_part = Label(left,text='Select Part', bg='skyblue')
    lb_part.grid(row=0,column=1)
    part_list =['Drumsticks','wings','Combo']
    spin_part = Spinbox(left, values=part_list, width=15, justify=CENTER)
    spin_part.grid(row=1,column=1)

    lb_imgSize = Label(left, image=img_size,bg='skyblue')
    lb_imgSize.grid(row=2,column=0,rowspan=2,pady=5)
    lb_size = Label(left, text="Select Size\n S=150฿, M=250฿ , L=340฿",bg="skyblue")
    lb_size.grid(row=2,column=1)
    size_list = ['Small','Medium','Large']
    spin_size = Spinbox(left,values=size_list,width=15,justify=CENTER)
    spin_size.grid(row=3,column=1)

    lb_imgquan  =  Label(left, image=img_quan,bg='skyblue')
    lb_imgquan.grid(row=4, column=0,rowspan=2,pady=5)
    lb_quan = Label(left,text='Quantity',bg='skyblue')
    lb_quan.grid(row=4,column=1)
    spin_quan =Spinbox(left,from_=0,to=10,width=10,justify=CENTER)
    spin_quan.grid(row=5,column=1)

    lb_add = Label(left,text='Additional sides',bg='skyblue')
    lb_add.grid(row=6,column=0)
    chk_kimchi = Checkbutton(left, text='Kimchi(50฿/serve',variable=kimchiVal,onvalue='Yes',offvalue='No',bg='skyblue')
    chk_kimchi.grid(row=6,column=1,padx=10)
    kimchiVal.set('No')

    btn_checkout = Button(left, text='Checkout', image=img_cart, compound=LEFT, command=checkout)
    btn_checkout.grid(row=7,column=1,pady=10)

    return spin_part, spin_size, spin_quan, chk_kimchi
   
def checkout():
    print('Checkout click')
    total = 0
    kimchi_price = 0
    if spin_size.get() == 'Small':
        size_price = 150
    elif spin_size.get() ==  'Medium':
        size_price = 250
    elif spin_size.get() == 'Large':
        size_price = 340

    quantity = int(spin_quan.get())
    
    if kimchiVal.get() == 'Yes':
        kimchi_price = 50
    else:
        kimchi_price = 0

    total = (size_price * quantity) + kimchi_price

    str_total = StringVar()
    str_total.set("%0.2f"%total)
    ent_total['text'] = str_total
    
    ent_part.delete(0, END)
    ent_part.insert(0, spin_part.get())
    
    ent_size.delete(0, END)
    ent_size.insert(0, spin_size.get())

    ent_quan.delete(0, END)
    ent_quan.insert(0, spin_quan.get())

    ent_kimchi.delete(0, END)
    ent_kimchi.insert(0, kimchiVal.get())

    ent_total['bg'] = 'skyblue'
    ent_total['fg'] = 'white'


def widgetRight(right):
    right.columnconfigure((0,1), weight=1)

    lb_chk_part = Label(right, text="Part:", bg='lightgreen')
    lb_chk_part.grid(row=0, column=0, sticky='e')
    ent_part = Entry(right, width=15, justify=CENTER)
    ent_part.grid(row=0, column=1, padx=30,pady=10)

    lb_chk_size = Label(right, text="Size:", bg='lightgreen')
    lb_chk_size.grid(row=1, column=0, sticky='e')
    ent_size = Entry(right, width=15, justify=CENTER)
    ent_size.grid(row=1, column=1, padx=30,pady=10)
    
    lb_chk_quan = Label(right, text="Quantity:", bg='lightgreen')
    lb_chk_quan.grid(row=2, column=0, sticky='e')
    ent_quan = Entry(right, width=15, justify=CENTER)
    ent_quan.grid(row=2, column=1, padx=30,pady=10)

    lb_chk_kimchi = Label(right, text="Kimchi:", bg='lightgreen')
    lb_chk_kimchi.grid(row=3, column=0, sticky='e')
    ent_kimchi = Entry(right, width=15, justify=CENTER)
    ent_kimchi.grid(row=3, column=1, padx=30,pady=10)

    lb_chk_total = Label(right, text="Total price:", bg='lightgreen', font='Calibir 14 bold')
    lb_chk_total.grid(row=4, column=0, sticky='e')
    ent_total = Entry(right, width=15, justify=CENTER)
    ent_total.grid(row=4, column=1, padx=30,pady=10)

    return ent_part, ent_size, ent_quan, ent_kimchi, ent_total

def widgetbottom(bottom):
    bottom.columnconfigure((0,1), weight=1)
    bu_exit = Button(bottom,text='Exit Program',image=img_exit,command=exit,width=50,compound=RIGHT)
    bu_exit.grid(row=0,columnspan=2,sticky='e',pady=30,padx=10)
    

root = mainwindow()
left, right, bottom = createFrame(root)

kimchiVal = StringVar()

img_icon = PhotoImage(file="img/heart.png")
root.iconphoto(FALSE,img_icon)

img_part = PhotoImage(file='img/part.png')
img_size = PhotoImage(file='img/size.png')
img_quan = PhotoImage(file='img/kimchi.png')
img_cart = PhotoImage(file='img/cart.png')
img_exit = PhotoImage(file='img/exit.png')
# Frame left widget
widgetbottom(bottom)
spin_part, spin_size, spin_quan,  chk_kimchi = widgetLeft(left)
ent_part, ent_size, ent_quan, ent_kimchi, ent_total = widgetRight(right) # Frame right widget 
root.mainloop()