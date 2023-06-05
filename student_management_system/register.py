from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3
import os
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #======Bg Image====
        self.bg=ImageTk.PhotoImage(file="b2.jpg")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)
        #=====left image=====
        self.left=ImageTk.PhotoImage(file="side.png")
        left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)
        #=========Register Frame========
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)

        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)
    #=============row1=========================
        #self.var_frame=StringVar()
        f_name = Label(frame1, text="First Name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=100)
        #txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray",textvariable=self.var_frame).place(x=50,y=130,width=250)
        self.txt_fname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_fname.place(x=50, y=130,width=250)

        l_name = Label(frame1, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_lname.place(x=370,y=130,width=250)
        #--------------------------row2
        contact = Label(frame1, text="Contact number", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_contact.place(x=50,y=200,width=250)

        Email = Label(frame1, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=170)
        self.txt_Email=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_Email.place(x=370,y=200,width=250)
        #-----------row3
        question = Label(frame1, text="Security Question", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=240)

        self.cmd_quest=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify=CENTER)
        self.cmd_quest['values'] = ("Select", "Your First pet Name", "Your Birth Place", "Your Best Friends")
        self.cmd_quest.place(x=50, y=270, width=250)
        self.cmd_quest.current(0)

        answer = Label(frame1, text="Answer", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=240)
        self.txt_answer=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_answer.place(x=370,y=270,width=250)

        #-------------ro4
        password = Label(frame1, text="password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=310)
        self.txt_password=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_password.place(x=50,y=340,width=250)

        cpassword = Label(frame1, text="Confirm password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=310)
        self.txt_cpassword=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_cpassword.place(x=370,y=340,width=250)

        #------terms----'
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Term & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=50,y=380)
        self.btn_img=ImageTk.PhotoImage(file="register.png")
        btn_register=Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.register_data).place(x=50,y=420)

        btn_login = Button(self.root, text="Sign In",command=self.login_window,font=("times new roman",20),bd=0,cursor="hand2").place(x=200, y=460,width=180)


    def login_window(self):
        self.root.destroy()
        os.system("python login.py")
    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_Email.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_cpassword.delete(0, END)
        self.cmd_quest.current(0)
        self.txt_answer.delete(0, END)





    def register_data(self):
        #print(self.var_frame.get(),self.txt_lname.get())

        if self.txt_fname.get()=="" or self.txt_Email.get()=="" or self.cmd_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="" or self.txt_contact.get()=="":
            messagebox.showerror("Error","All fields are Requierd",parent=self.root)
        elif self.txt_password.get()!= self.txt_cpassword.get():
            messagebox.showerror("Error","Password & confirm password should be same")
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","pls Agree all the term and condition",parent=self.root)
        else:
                try:
                    con =con=sqlite3.connect(database="rms.db")
                    cur = con.cursor()
                    cur.execute("select * from employee where email=?",(self.txt_Email.get(),))
                    row=cur.fetchone()
                    if row!=None:
                        messagebox.showerror("Error", "user already exist pls try with another email", parent=self.root)
                    else:
                        query = "INSERT INTO employee (f_name, l_name, contact, Email, question, answer, password) VALUES (?, ?, ?, ?, ?, ?, ?)"
                        values = (
                            self.txt_fname.get(),
                            self.txt_lname.get(),
                            self.txt_contact.get(),
                            self.txt_Email.get(),
                            self.cmd_quest.get(),
                            self.txt_answer.get(),
                            self.txt_password.get()
                        )
                        cur.execute(query, values)
                        con.commit()
                        con.close()
                        messagebox.showinfo("Success", "Registration successful", parent=self.root)
                        self.clear()
                        self.login_window()
                except Exception as ex:
                       messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
root=Tk()
obj=Register(root)
root.mainloop()




'''

con=pymysql.connect(host="localhost",user=root,password="",database="employee2")
                cur=con.cursor()
                cur.execute("insert into employee (f_name,l_name,contact,Email,question,answer,password) values(? ? ? ? ? ? ?) ",
                            (
                                self.txt_fname.get(),
                                self.txt_lname.get(),
                                self.txt_contact.get(),
                                self.txt_Email.get(),
                                self.cmd_quest.get(),
                                self.txt_answer.get(),
                                self.txt_password.get()
                            ))
                con.commit()
                con.close()
                messagebox.showinfo("Success","Register successful",parent=self.root)
                


'''