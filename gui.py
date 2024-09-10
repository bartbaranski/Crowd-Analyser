import tkinter as tk
from tkinter import filedialog
from main import analyze_video

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        analyze_video(file_path)

root = tk.Tk()
root.title("Crowd Analysis")

open_button = tk.Button(root, text="Open Video", command=open_file)
open_button.pack()

root.mainloop()

