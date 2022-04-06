import sqlite3
from tkinter import messagebox
from tkinter import *
from tkVideoPlayer import TkinterVideo
from password_strength import PasswordStats

def createconnection() :
    global conn,cursor
    conn = sqlite3.connect('BD\BD_Holiday.db')
    cursor = conn.cursor()

def mainwindow() :
    root = Tk()
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.resizable(False,False)
    root.config(bg='#ffffff')
    root.title("Holiday")
    root.option_add('*font',("Product Sans", 20))
    videoplayer = TkinterVideo(master=root, scaled=True ,pre_load=False)
    videoplayer.load(r"video\logo.mp4")
    videoplayer.pack(expand=True, fill="both")
    videoplayer.play()
    return root

def mainlayout():
    global mainframe
    mainframe = Frame(root, bg='#ffffff')
    mainframe.place(x=0, y=0, width=w, height=h)
    mainframe.rowconfigure(0, weight=10)  
    Label(mainframe, image=main_img1,bg="#ffffff").place(x=185,y=206)
    Button(mainframe, image=main_img2, foreground='#ffffff',bg='#ffffff',bd=0,command=loginlayout).place(x=689,y=321)
    Button(mainframe, image=main_img3, foreground='#ffffff',bg='#ffffff',bd=0,command=signuplayout).place(x=689,y=425)

def usertext(event):
    userentry.delete(0,END)
    userentry.config(fg='black')

def passtext(event):
    passentry.delete(0, END)
    passentry.config(show='•')
    passentry.config(fg='black')

def loginlayout():
    global userentry,passentry,loginframe
    mainframe.destroy
    root.title("Login")
    loginframe = Frame(root, bg='#ffffff')
    loginframe.place(x=0, y=0, width=w, height=h)
    loginframe.rowconfigure(0, weight=10)  
    Label(loginframe, image=login_img1,bg="#ffffff").place(x=185,y=206)

    Label(loginframe, image=login_img3,bg="#ffffff",).place(x=725,y=257)
    userentry = Entry(loginframe, bg='#ffffff',bd=0, fg='#398AB9',textvariable=userinfo,width=18)
    userentry.insert(0,' Email')
    userentry.bind("<Button>",usertext)
    userentry.place(x=800,y=260)
    Frame(width=300,height=3,bg="#D8D2CB").place(x=800,y=300)

    Label(loginframe, image=login_img2,bg="#ffffff").place(x=725,y=346)
    passentry = Entry(loginframe, bg='#ffffff',bd=0, fg='#398AB9',textvariable=passinfo,width=18)
    passentry.insert(0,' Password')
    passentry.bind("<Button>",passtext)
    passentry.place(x=800,y=350)
    Frame(width=300,height=3,bg="#D8D2CB").place(x=800,y=390)

    Button(loginframe, image=login_img5, foreground='#ffffff',bg='#ffffff',bd=0,command=backsignup).place(x=813,y=432)
    Button(loginframe, image=login_img4, foreground='#ffffff',bg='#ffffff',bd=0,command=loginclick).place(x=787,y=516)

def backsignup():
    loginframe.destroy
    userentry.delete(0,END)
    passentry.delete(0, END)
    signuplayout()

def loginclick():
    global result
    if userentry.get() == "" or passentry.get() == "":
        messagebox.showwarning("Admin: ", "Enter email or password first")
        userentry.focus_force()
    else:
        sql = "select * from Login where email=? and password=?"
        cursor.execute(sql, [userinfo.get(), passinfo.get()])
        result = cursor.fetchall()
        print(result)
        if result:
            messagebox.showinfo("Admin : ", "Login Successfuly")
        else:
            messagebox.showwarning("Admin : ", "Email not exists")
            userentry.select_range(0, END)
            userentry.focus_force()

def newfirstnametext(event):
    newfirstname.delete(0,END)
    newfirstname.config(fg='black')

def newlastnametext(event):
    newlastname.delete(0,END)
    newlastname.config(fg='black')

def newemailtext(event):
    newemail.delete(0,END)
    newemail.config(fg='black')

def newpasstext(event):
    newpass.delete(0,END)
    newpass.config(show='•')
    newpass.config(fg='black')

def newconfirpasstext(event):
    newconfirpass.delete(0,END)
    newconfirpass.config(show='•')
    newconfirpass.config(fg='black')

def signuplayout():
    global newfirstname,newlastname,newemail,newpass,newconfirpass,signupframe,f2color,passtag
    mainframe.destroy
    root.title("Sign up")
    signupframe = Frame(root, bg='#ffffff')
    signupframe.place(x=0, y=0, width=w, height=h)
    signupframe.rowconfigure(0, weight=10)  
    Label(signupframe, image=singup_img1,bg="#ffffff").place(x=185,y=206)

    newemail = Entry(signupframe, bg='#ffffff',bd=0, fg='#398AB9',width=18,textvariable=newemailinfo)
    newemail.insert(0,' Email')
    newemail.bind("<Button>",newemailtext)
    newemail.place(x=800,y=123)
    Frame(width=300,height=3,bg="#D8D2CB").place(x=800,y=163)

    newfirstname = Entry(signupframe, bg='#ffffff',bd=0, fg='#398AB9',width=18,textvariable=newfnameinfo)
    newfirstname.insert(0,' Firstname')
    newfirstname.bind("<Button>",newfirstnametext)
    newfirstname.place(x=800,y=213)
    Frame(width=300,height=3,bg="#D8D2CB").place(x=800,y=253)
    
    newlastname = Entry(signupframe, bg='#ffffff',bd=0, fg='#398AB9',width=18,textvariable=newlnameinfo)
    newlastname.insert(0,' Lastname')
    newlastname.bind("<Button>",newlastnametext)
    newlastname.place(x=800,y=303)
    Frame(width=300,height=3,bg="#D8D2CB").place(x=800,y=343)
    
    passtag = Label(signupframe, text=" ",bg="#ffffff",fg="#ffffff")
    passtag.place(x=1015,y=390)
    newpass = Entry(signupframe, bg='#ffffff',bd=0, fg='#398AB9',width=12,textvariable=newpwdinfo)
    newpass.insert(0,' Password')
    newpass.bind("<Button>",newpasstext)
    newpass.bind("<Key>",check)
    newpass.place(x=800,y=393)
    f2color = Frame(width=300,height=3,bg="#D8D2CB")
    f2color.place(x=800,y=433)
    
    newconfirpass = Entry(signupframe, bg='#ffffff',bd=0, fg='#398AB9',width=18,textvariable=newconfirpwdinfo)
    newconfirpass.insert(0,' Confirm password')
    newconfirpass.bind("<Button>",newconfirpasstext)
    newconfirpass.place(x=800,y=487)
    Frame(width=300,height=3,bg="#D8D2CB").place(x=800,y=527)

    Button(signupframe, image=singup_img2, foreground='#ffffff',bg='#ffffff',bd=0,command=backlogin).place(x=789,y=582)
    Button(signupframe, image=singup_img3, foreground='#ffffff',bg='#ffffff',bd=0,command=registration).place(x=825,y=647)

def check(event):
    if len(newpass.get()) >= 2:
        result=PasswordStats(newpass.get())
        final=result.strength()
        print(final)
        if final >= 0.40:
            f2color.config(bg="#27cf54")
            passtag.config(text="Strong",fg="#27cf54")
        elif final > 0.10 and final < 0.20:
            f2color.config(bg="#F0A500")
            passtag.config(text="Good",fg="#F0A500")
        elif final <= 0.10:
            f2color.config(bg="#D0312D")
            passtag.config(text="Weak",fg="#D0312D")
 
def backlogin():
    signupframe.destroy
    newfirstname.delete(0,END)
    newlastname.delete(0,END)
    newemail.delete(0,END)
    newpass.delete(0,END)
    newconfirpass.delete(0,END)
    loginlayout()

def registration() :
    sql_chk = "SELECT * FROM Login WHERE email= ?"
    cursor.execute(sql_chk,[newemailinfo.get()])
    chk_result = cursor.fetchall()
    print(chk_result)
    if chk_result:
        messagebox.showwarning("Admin", 'This Email already use')
        newemail.focus_force()
        newemail.select_range(0,END)
    else:
        if newemailinfo.get() == "":
            messagebox.showwarning("Admin", 'Please enter your Email')
            newemail.focus_force()
        elif newfnameinfo.get() == "":
            messagebox.showwarning("Admin", 'Please enter your Firstname')
            newfirstname.focus_force()
        elif newlnameinfo.get() == "":
            messagebox.showwarning("Admin", 'Please enter your Lastname')
            newlastname.focus_force()
        elif newpwdinfo.get() == "":
            messagebox.showwarning("Admin", 'Please enter your password')
            newpass.focus_force()
        elif newconfirpwdinfo.get() == "":
            messagebox.showwarning("Admin","Please enter your Confirm Password")
            newconfirpass.focus_force()
        else:
            if newpwdinfo.get() == newconfirpwdinfo.get():
                sql_ins = 'INSERT INTO Login VALUES (?,?,?,?)'
                cursor.execute(sql_ins, [newfnameinfo.get(),newlnameinfo.get(),newemailinfo.get(),newpwdinfo.get()])
                conn.commit()
                retrivedata()
                messagebox.showinfo("Admin","Registration Successfully")
                loginlayout()
            else:
                 messagebox.showwarning("admin",'Confirm password is not matched')

def retrivedata() :
    sql = "select * from Login"
    cursor.execute(sql)
    result = cursor.fetchall()
    print("Total row = ",len(result))
    for i,data in enumerate(result) :
        print("Row#",i+1,data)

w = 1300
h = 800

createconnection()
root = mainwindow()

#loginlayout info
userinfo = StringVar()
passinfo = StringVar()

#signuplayout info
newemailinfo = StringVar()
newfnameinfo = StringVar()
newlnameinfo = StringVar()
newpwdinfo = StringVar()
newconfirpwdinfo = StringVar()

#icon
img_icon = PhotoImage(file="images\paper-plane.png")
root.iconphoto(FALSE,img_icon)

#mainlayout_img
main_img1 = PhotoImage(file=r'images\main_img.png')
main_img2 = PhotoImage(file=r'images\login_button.png')
main_img3 = PhotoImage(file=r'images\signup_button.png')

#loginlayout_img
login_img1 = PhotoImage(file=r'images\login_img.png')
login_img2 = PhotoImage(file=r'images\Vpn key.png')
login_img3 = PhotoImage(file=r'images\Account circle.png')
login_img4 = PhotoImage(file=r'images\login_small_button.png')
login_img5 = PhotoImage(file=r'images\back to sign up.png')

#signuplayout_img
singup_img1 = PhotoImage(file=r'images\singup_img.png')
singup_img2 = PhotoImage(file=r'images\Already have an account.png')
singup_img3 = PhotoImage(file=r'images\signup_small_button.png')


root.after(3500,mainlayout)

root.mainloop()