from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        # Background Image
        self.bg = ImageTk.PhotoImage(file=r"college_images/student2.jpeg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Frame
        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        # Login Image
        img1 = Image.open(r"college_images/login.png")
        img1 = img1.resize((100, 100), Image.Resampling.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=730, y=175, width=100, height=100)

        # Title
        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=100)

        # Username label and entry
        username = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=70, y=155)
        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        # Password label and entry
        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=70, y=225)
        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"), show='*')
        self.txtpass.place(x=40, y=250, width=270)

        # Login button
        loginbtn = Button(frame, text="Login", command=self.login, font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=300, width=120, height=35)

        # Register button
        registerbtn = Button(frame, text="New User Register", command=self.register_window, font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=10, y=350, width=160)

        # Forget password button
        forgetbtn = Button(frame, text="Forget Password", command=self.forgot_password_window, font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        forgetbtn.place(x=10, y=370, width=160)

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.txtuser.get() == "ABC" and self.txtpass.get() == "ABC":
            messagebox.showinfo("Success", "Welcome to the attendance system")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Arati@123", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM register WHERE email=%s AND password=%s", (self.txtuser.get(), self.txtpass.get()))
                row = my_cursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid username or password")
                else:
                    open_main = messagebox.askyesno("Access", "Access only admin?")
                    if open_main:
                        self.new_window = Toplevel(self.root)
                        self.app = Face_Recognition_System(self.new_window)
                conn.close()
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {str(err)}")
        self.clear()

    def clear(self):
        self.txtuser.delete(0, END)
        self.txtpass.delete(0, END)

    def forgot_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please enter the email address to reset password")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Arati@123", database="face_recognizer")
                my_cursor = conn.cursor()
                query = "SELECT * FROM register WHERE email=%s"
                value = (self.txtuser.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                if row is None:
                    messagebox.showerror("Error", "Invalid email address")
                else:
                    conn.close()
                    self.reset_password_window()
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {str(err)}")

    def reset_password_window(self):
        self.root2 = Toplevel()
        self.root2.title("Reset Password")
        self.root2.geometry("340x450+610+170")

        l = Label(self.root2, text="Reset Password", font=("times new roman", 12, "bold"), fg="red", bg="white")
        l.place(x=0, y=10, relwidth=1)

        security_Q = Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white")
        security_Q.place(x=50, y=80)
        self.combo_security_Q = ttk.Combobox(self.root2, font=("times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your birth place", "Your pet name", "Your school name")
        self.combo_security_Q.place(x=50, y=110, width=250)
        self.combo_security_Q.current(0)

        security_A = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
        security_A.place(x=50, y=150)
        self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
        self.txt_security.place(x=50, y=180, width=250)

        new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white")
        new_password.place(x=50, y=220)
        self.txt_newpass = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
        self.txt_newpass.place(x=50, y=250, width=250)

        btn = Button(self.root2, text="Reset", font=("times new roman", 15, "bold"), fg="white", bg="green", command=self.reset_password)
        btn.place(x=100, y=290)

    def reset_password(self):
        if self.combo_security_Q.get() == "Select":
            messagebox.showerror("Error", "Select security question")
        elif self.txt_security.get() == "":
            messagebox.showerror("Error", "Please enter the answer")
        elif self.txt_newpass.get() == "":
            messagebox.showerror("Error", "Please enter the new password")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Arati@123", database="face_recognizer")
                my_cursor = conn.cursor()
                query = "SELECT * FROM register WHERE email=%s AND securityQ=%s AND securityA=%s"
                value = (self.txtuser.get(), self.combo_security_Q.get(), self.txt_security.get())
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                
                if row is None:
                    messagebox.showerror("Error", "Invalid answer")
                else:
                    update_query = "UPDATE register SET password=%s WHERE email=%s"
                    my_cursor.execute(update_query, (self.txt_newpass.get(), self.txtuser.get()))
                    conn.commit()
                    messagebox.showinfo("Success", "Password reset successfully")
                    self.root2.destroy()
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {str(err)}")
            finally:
                conn.close()

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")

        # Background Image
        self.bg = ImageTk.PhotoImage(file=r"college_images/student2.jpeg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Frame
        frame = Frame(self.root, bg="white")
        frame.place(x=610, y=170, width=340, height=450)

        # Register Image
        img1 = Image.open(r"college_images/register.png")
        img1 = img1.resize((100, 100), Image.Resampling.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="white", borderwidth=0)
        lblimg1.place(x=730, y=175, width=100, height=100)

        # Title
        title = Label(frame, text="Register", font=("times new roman", 20, "bold"), fg="black", bg="white")
        title.place(x=90, y=100)

        # Username label and entry
        username = Label(frame, text="Username", font=("times new roman", 15, "bold"), bg="white")
        username.place(x=70, y=155)
        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        # Email label and entry
        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white")
        email.place(x=70, y=225)
        self.txtemail = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtemail.place(x=40, y=250, width=270)

        # Security question label and entry
        security_Q = Label(frame, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white")
        security_Q.place(x=70, y=295)
        self.combo_security_Q = ttk.Combobox(frame, font=("times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your birth place", "Your pet name", "Your school name")
        self.combo_security_Q.place(x=40, y=320, width=270)
        self.combo_security_Q.current(0)

        # Security answer label and entry
        security_A = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
        security_A.place(x=70, y=355)
        self.txt_security = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txt_security.place(x=40, y=380, width=270)

        # Password label and entry
        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white")
        password.place(x=70, y=405)
        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"), show='*')
        self.txtpass.place(x=40, y=430, width=270)

        # Register button
        registerbtn = Button(frame, text="Register", command=self.register, font=("times new roman", 15, "bold"), bg="blue", fg="white", activeforeground="white", activebackground="blue")
        registerbtn.place(x=100, y=470, width=120, height=35)

    def register(self):
        if self.txtuser.get() == "" or self.txtemail.get() == "" or self.combo_security_Q.get() == "Select" or self.txt_security.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Arati@123", database="face_recognizer")
                my_cursor = conn.cursor()
                query = "SELECT * FROM register WHERE email=%s"
                value = (self.txtemail.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                if row is not None:
                    messagebox.showerror("Error", "User already exists with this email")
                else:
                    insert_query = "INSERT INTO register (username, email, securityQ, securityA, password) VALUES (%s, %s, %s, %s, %s)"
                    insert_value = (self.txtuser.get(), self.txtemail.get(), self.combo_security_Q.get(), self.txt_security.get(), self.txtpass.get())
                    my_cursor.execute(insert_query, insert_value)
                    conn.commit()
                    messagebox.showinfo("Success", "Registration successful")
                    self.root.destroy()
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {str(err)}")
            finally:
                conn.close()

# To run the application
if __name__ == "__main__":
    root = Tk()
    app = Login_Window(root)
    root.mainloop()
