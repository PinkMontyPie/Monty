from tkinter import *

def createwindow() :
    root = Tk()
    root.title("BasicGUI#1: by type your Soravih Puvekit 1640705115")
    root.geometry('500x500')
    root.configure(bg='#3895D3')
    return root

def createwidget(root):
    title = Label(root,text="Calculating Program",fg='blue',bg="#3895D3")
    tag1 = Label(root,text="Tag Name1 : ",fg="blue",bg="lightblue")
    tag2 = Label(root,text="Tag Name2 : ",fg="blue",bg="lightpink")
    title.grid(row=0,column=0,pady=10,padx=40)
    tag1.grid(row=1,column=0,)
    tag2.grid(row=2,column=0,pady=10)
    box1 = Entry(width=10,bg='lightgrey')
    box2 = Entry(width=10,bg='lightgrey')
    box1.grid(row=1,column=1,)
    box2.grid(row=2,column=1,)
    btn1 = Button(root,text="Button1",width=10,bg='Pink')
    btn2 = Button(root,text="Button2",width=10,bg='Blue')
    btn1.grid(row=3,column=0,pady=10,ipady=10,ipadx=10)
    btn2.grid(row=3,column=1,pady=10,ipady=10,ipadx=10)
    
def createReplaceWidget(root):
    root.title("Replace")
    lb_findwhat = Label(root, text="Find what:", font="product 14 bold")
    lb_findwhat.grid(row=0 , column=0)
    
    ent_find = Entry(root, width=20, bg="lightblue")
    ent_find.grid(row=0, column=1 )

    btn_find = Button(root, text="Find Next", bg="pink" ,width=12)
    btn_find.grid(row=0, column=2)

    lb_replace = Label(root, text="Replace With:")
    lb_replace.grid(row=1, column=0, padx=20 , pady=5 , sticky="w")

    ent_replace = Entry(root, width=20, bg="lightblue")
    ent_replace.grid(row=1, column=1, padx=15)

    btn_replace = Button(root, text="Replace", bg="pink" ,width=12)
    btn_replace.grid(row=1, column=2)

    lbDirection = Label(root, text="Direction:")
    lbDirection.grid(row=2, column=0 ,padx=20, pady=5, sticky="w")
    
    radUp = Radiobutton(root, text="Up", value="up")
    radUp.grid(row=2 ,column=1, padx=15, sticky="w")

    radDown = Radiobutton(root, text="Down", value="down")
    radDown.grid(row=3, column=1, padx=15, sticky="w")

    btnReplace = Button(root, text="Replace All", bg="red" ,width=12)
    btnReplace.grid(row=2, column=2)

    btnCancel = Button(root, text="Cancel", fg="white", bg="grey", width=12)
    btnCancel.grid(row=3, column=2)

root = createwindow()
#createwidget(root)
createReplaceWidget(root)
root.mainloop()