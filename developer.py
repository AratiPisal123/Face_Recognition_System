from tkinter import *
from tkinter import ttk, filedialog, messagebox
import cv2
from PIL import Image, ImageTk
import mysql.connector
import os

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Title label
        title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Top image
        img_top = Image.open(r"C:\Users\madhu\OneDrive\Desktop\Projects\Face Recognition Attendance System\college_images\developer.jpeg")
        img_top = img_top.resize((1530, 720), Image.Resampling.LANCZOS)  # Updated Resampling method
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=720)

        # Main frame (adjusted size for better fit)
        main_frame = Frame(f_lbl, bd=2, bg="white")
        main_frame.place(x=1050, y=100, width=450, height=500)

        # Developer image
        img_top1 = Image.open(r"C:\Users\madhu\OneDrive\Desktop\Projects\Face Recognition Attendance System\college_images\developer1.jpg")
        img_top1 = img_top1.resize((150, 150), Image.Resampling.LANCZOS)  # Smaller size
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)
        f_lbl = Label(main_frame, image=self.photoimg_top1)
        f_lbl.place(x=150, y=0, width=150, height=150)

        # Developer info
        dev_label = Label(main_frame, text="Hello, my name is Arati", font=("times new roman", 20, "bold"), fg="blue")
        dev_label.place(x=60, y=160)
        dev_label2 = Label(main_frame, text="I am a full stack developer", font=("times new roman", 20, "bold"), fg="blue")
        dev_label2.place(x=30, y=200)

        # Second developer image
        img2 = Image.open(r"C:\Users\madhu\OneDrive\Desktop\Projects\Face Recognition Attendance System\college_images\developer2.jpg")
        img2 = img2.resize((400, 300), Image.Resampling.LANCZOS)  # Adjusted size to fit main frame
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(main_frame, image=self.photoimg2)
        f_lbl.place(x=25, y=250, width=400, height=300)

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
