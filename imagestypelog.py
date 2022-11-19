from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk
import balance
import hashlib


def imagestypelog(login_hash):
    def hashfunction(path):
        global img_hash
        with open(path, "rb") as f:
            img_hash = hashlib.md5()
            while chunk := f.read(8192):
                img_hash.update(chunk)
        img_hash = img_hash.hexdigest()

        if login_hash == img_hash:
            root.destroy()
            balance.balance(login_hash)

        else:
            messagebox.showerror("Error", "Wrong Choice!", parent=root)
            root.destroy()

    def first():
        hashfunction("photos/animals/3.jpg")

    def second():
        hashfunction("photos/animals/4.jpg")

    def third():
        hashfunction("photos/animals/6.jpg")

    root = Tk()
    root.title("Login type")
    img_label = Label(root, text="Choose one of the three pictures:", bg="black", fg="white", width=40,
                      font=("bold", 20))
    img_label.place(x=90, y=53)
    img_label.pack()

    width, height = 850, 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))
    root.geometry("{}x{}+{}+{}".format(width, height, x, y))

    img1 = Image.open("photos/animals/3.jpg")
    img2 = Image.open("photos/animals/4.jpg")
    img3 = Image.open("photos/animals/6.jpg")

    resize_image1 = img1.resize((200, 200))
    resize_image2 = img2.resize((200, 200))
    resize_image3 = img3.resize((200, 200))

    img1 = ImageTk.PhotoImage(resize_image1)
    img2 = ImageTk.PhotoImage(resize_image2)
    img3 = ImageTk.PhotoImage(resize_image3)

    Button(root, image=img1, command=first).place(x=100, y=100)
    Button(root, image=img2, command=second).place(x=320, y=100)
    Button(root, image=img3, command=third).place(x=540, y=100)

    root.configure(bg='black')

    root.mainloop()


if __name__ == "__main__":
    imagestypelog()
