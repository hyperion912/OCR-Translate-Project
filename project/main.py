from tkinter import *
from tkinter import filedialog


win = Tk()
win.geometry("900x600")
win.title("Project")
win.config(padx=150, pady=150, bg="#222222")

img_label = Label(text="Select Image",  font=("Calibri", 50, "bold"), bg="#222222", fg="#D8D9CF", padx=30, pady=30).pack()

def open():
    win.filename = filedialog.askopenfilename(initialdir="C:/", title="Select a file", filetypes = (("png file", "*.png"), ("jpeg file", "*.jpeg"), ("jpg file", "*.jpg")))
    if win.filename == "":
        pass
    else:
        top = Toplevel(win)
        top.geometry("1920x1080")
        top.config(pady=25, padx=25)
        top.title("new window")

img = PhotoImage(file="addimage.png")
button = Button(text="Browse", command=open, image=img, highlightthickness=0).pack()


win.mainloop()