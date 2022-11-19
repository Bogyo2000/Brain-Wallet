from tkinter import *
from PIL import ImageTk, Image
# import random
import hashlib
import registration

img_hash = ""


def images():
    def prevpage():
        root.destroy()
        registration.reg()

    def clicked(path):
        global img_hash
        with open(path, "rb") as f:
            img_hash = hashlib.md5()
            while chunk := f.read(8192):
                img_hash.update(chunk)
        img_hash = img_hash.hexdigest()
        root.destroy()

    def first():
        clicked("photos/animals/3.jpg")

    def second():
        clicked("photos/animals/4.jpg")

    def third():
        clicked("photos/animals/6.jpg")

    root = Tk()
    root.title("Login type")
    img_label = Label(root, text="Choose one of the three pictures:", bg="black", fg="white", font=("bold", 20))
    img_label.place(x=90, y=53)
    img_label.pack()

    width, height = 800, 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))
    root.geometry("{}x{}+{}+{}".format(width, height, x, y))

    # def generate_number():
    #     list = ["animals", "buildings", "cars", "flowers", "fruits and vegetables", "icons", "objects", "vehicles"]
    #     number = ["1", "2", "3", "4", "5", "6"]
    #     maps = []
    #     num = []
    #     for i in range(2):
    #         d = random.choice(list)
    #         maps.append(d)
    #         list.remove(d)
    #         n = random.choice(number)
    #         num.append(n)
    #         number.remove(n)
    #     return maps, num

    # d,n = generate_number()
    # img1 = Image.open(f"photos/{d[0]}/{n[0]}.jpg")
    # img2 = Image.open(f"photos/{d[1]}/{n[1]}.jpg")

    img1 = Image.open("photos/animals/3.jpg")
    img2 = Image.open("photos/animals/4.jpg")
    img3 = Image.open("photos/animals/6.jpg")

    resize_image1 = img1.resize((200, 200))
    resize_image2 = img2.resize((200, 200))
    resize_image3 = img3.resize((200, 200))

    img1 = ImageTk.PhotoImage(resize_image1)
    img2 = ImageTk.PhotoImage(resize_image2)
    img3 = ImageTk.PhotoImage(resize_image3)

    Button(root, image=img1, command=first).place(x=80, y=150)
    Button(root, image=img2, command=second).place(x=300, y=150)
    Button(root, image=img3, command=third).place(x=520, y=150)

    # Button(root, width = 15, text = "Skip", bg = "purple", fg = "white", relief = SOLID).place(x = 250, y = 400)
    Button(root, width=15, text="Go back", bg="purple", fg="white", font="Helvetica", relief=SOLID,
           command=prevpage).place(x=330, y=400)

    root.configure(bg='black')

    root.mainloop()


if __name__ == "__main__":
    images()
