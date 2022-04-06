from tkinter import *
from password_strength import PasswordStats

def mainwindow() :
    root = Tk()
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.resizable(False,False)
    root.config(bg='#ffffff')
    root.title("Holiday")
    root.option_add('*font',("Product Sans", 20))
    return root

def signuplayout():
    global newpass,fcolor,signupframe,passtag
    root.title("Sign up")
    signupframe = Frame(root, bg='#ffffff')
    signupframe.place(x=0, y=0, width=w, height=h)
    signupframe.rowconfigure(0, weight=10) 
    passtag = Label(signupframe, text=" ",bg="#ffffff",fg="#ffffff")
    passtag.place(x=1015,y=390)
    newpass = Entry(signupframe,bg='#ffffff',bd=0, fg='#398AB9',width=12)
    newpass.insert(0,' Password')
    newpass.bind("<Button>",newpasstext)
    newpass.bind("<Key>",check)
    newpass.place(x=800,y=393)
    fcolor = Frame(width=300,height=3,bg="#D8D2CB")
    fcolor.place(x=800,y=433)


def check(event):
    if len(newpass.get()) >= 2:
        result=PasswordStats(newpass.get())
        final=result.strength()
        print(final)
        if final >= 0.40:
            fcolor.config(bg="#27cf54")
            passtag.config(text="Strong",fg="#27cf54")
        elif final > 0.05 and final < 0.10:
            fcolor.config(bg="#f0f007")
            passtag.config(text="Good",fg="#f0f007")
        elif final <= 0.05:
            fcolor.config(bg="#de3c3c")
            passtag.config(text="Weak",fg="#de3c3c")

clickcont = []
def newpasstext(event):
    if len(clickcont) == 0:
        clickcont.append(1)
        newpass.delete(0,END)
        newpass.config(show='•')
        newpass.config(fg='black')
    else:
        pass

w = 1300
h = 800

root = mainwindow()

signuplayout()

#loginlayout info
userinfo = StringVar()
passinfo = StringVar()

#signuplayout info
newemailinfo = StringVar()
newfnameinfo = StringVar()
newlnameinfo = StringVar()
newpwdinfo = StringVar()
newconfirpwdinfo = StringVar()


root.mainloop()