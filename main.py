from tkinter import *
import registration
import login


def main():
    def log():
        root.destroy()
        login.log()

    def reg():
        root.destroy()
        registration.reg()

    root = Tk()
    root.title("Brain Wallets")
    label = Label(root, text="Welcome to the Brain Wallets!", bg="black", fg="white", font=("Helvetica", 20))
    label.pack()
    width, height = 500, 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))
    root.geometry("{}x{}+{}+{}".format(width, height, x, y))

    Button(root, text="Login", width=30, height=5, bg="purple", fg="white", font="Helvetica", command=log).place(x=120, y=100)
    Button(root, text="Registration", width=30, height=5, bg="purple", fg="white", font="Helvetica", command=reg).place(x=120, y=250)

    root.configure(bg='black')

    root.mainloop()


if __name__ == "__main__":
    main()
