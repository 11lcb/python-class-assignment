import random
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
def surprise():
    popup_1 = tk.Toplevel(root)
    
    class ImageViewer:
      
            popup_1.title("彩蛋")
            image = Image.open("a.jpg") 
            photo = ImageTk.PhotoImage(image)
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            b = 400 
            c = 150
            x= random.randint(0,screen_width - b)
            y= random.randint(0,screen_height - c)
            popup_1.geometry(f'{b}x{c}+{x}+{y}')
            label_3 = tk.Label(popup_1, image=photo)
            label_3.pack(padx=10, pady=10)
    app = ImageViewer(root)
surprise()