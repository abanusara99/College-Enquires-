import tkinter as tk
from PIL import ImageTk, Image
import os

root = tk.Tk()
root.geometry("500x600")
root.title("ABAS")
root.config(bg="light cyan")

# Load the logo image
logo_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "ab.png")
logo_image = ImageTk.PhotoImage(Image.open(logo_path))

# Create a label with the logo image
logo_label = tk.Label(root, image=logo_image)
logo_label.pack()

def run_main():
    os.system("python main.py")
    root.destroy()

# Create the next button
next_button = tk.Button(root, text="Next", font=("Arial", 20), command=run_main)
next_button.pack(side="bottom")



root.mainloop()
