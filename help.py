from tkinter import *
from tkinter import ttk, filedialog, messagebox
import cv2
from PIL import Image, ImageTk
import mysql.connector
import os

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Title label
        title_lbl = Label(self.root, text="HELP DESK", font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Top image
        img_top = Image.open(r"C:\Users\madhu\OneDrive\Desktop\Projects\Face Recognition Attendance System\college_images\helpdesk.jpeg")
        img_top = img_top.resize((1530, 720), Image.Resampling.LANCZOS)  # Updated Resampling method
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        top_lbl = Label(self.root, image=self.photoimg_top)
        top_lbl.place(x=0, y=55, width=1530, height=720)

        # Developer info
        dev_label = Label(self.root, text="Email: codewithme@gmail.com", font=("times new roman", 20, "bold"), fg="blue")
        dev_label.place(x=550, y=220)

        # Second developer image
        img2 = Image.open(r"C:\Users\madhu\OneDrive\Desktop\Projects\Face Recognition Attendance System\college_images\developer2.jpg")
        img2 = img2.resize((400, 300), Image.Resampling.LANCZOS)  # Adjusted size to fit the window
        self.photoimg2 = ImageTk.PhotoImage(img2)
        second_img_lbl = Label(self.root, image=self.photoimg2)
        second_img_lbl.place(x=650, y=300, width=400, height=300)

if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
