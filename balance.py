from tkinter import *

import login
import pyqrcode

key = ""


def balance(login_hash):
    def prevpage():
        root.destroy()
        login.log()

    def show():
        qr = pyqrcode.create(login_hash)
        qr.show()

    root = Tk()
    root.title("Balance")
    b_label = Label(root, text="Your Bitcoin Balance", bg="black", fg="white", font=("Helvetica", 16))
    b_label.place(x=90, y=53)
    b_label.pack()

    width, height = 500, 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))
    root.geometry("{}x{}+{}+{}".format(width, height, x, y))

    Label(root, text="Bitcoin balance:", bg="black", fg="white").place(x=80, y=80)

    Button(root, text='Show QR code', bd='5', bg="purple", command=show).place(x=80, y=150)

    Button(root, text="End Session", width=30, height=5, bg="purple", fg="white", command=prevpage).place(x=150, y=400)

    root.configure(bg='black')

    root.mainloop()


if __name__ == "__main__":
    balance()
