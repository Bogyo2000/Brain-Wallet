from tkinter import *
from hashlib import sha256
from tkinter import messagebox

import balance

key = ""
counter = 0


def wordstypelogin(login_hash):
    def retrieve_input():
        global counter
        counter = counter + 1
        if counter < 3:
            firstw = first.get()
            secondw = second.get()
            thirdw = third.get()
            fourthw = fourth.get()
            fifthw = fifth.get()
            sixthw = sixth.get()

            if (firstw == "" or
                    secondw == "" or
                    thirdw == "" or
                    fourthw == "" or
                    fifthw == "" or
                    sixthw == ""):
                messagebox.showerror("Error", "All fields are required", parent=root)

            else:

                ret_string = firstw + " " + secondw + " " + thirdw + " " + fourthw + " " + fifthw + " " + sixthw

                global key
                key = sha256(ret_string.encode("utf-8")).hexdigest()

                if login_hash == key:
                    root.destroy()
                    balance.balance(login_hash)
                    counter = 0
        else:
            messagebox.showerror("Error", "Too many login attempts", parent=root)
            root.destroy()
            counter = 0

        # counter = 0
        # while (counter<=3):
        #     if login_hash == key:
        #         root.destroy()
        #         balance.balance()
        #     else:
        #         counter = counter + 1
        # messagebox.showerror("Error", "Too many login attempts", parent=root)
        # root.destroy()

    root = Tk()
    root.title("Enter to your account")
    login_label = Label(root, text="Add your six word code", bg="black", fg="white", width=20, font=("bold", 20))
    login_label.place(x=90, y=53)
    login_label.pack()

    width, height = 500, 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))
    root.geometry("{}x{}+{}+{}".format(width, height, x, y))

    Label(root, text="First word:", bg="black", fg="white").place(x=80, y=80)

    first = Entry(root, show='*')
    first.place(x=240, y=80)

    Label(root, text="Second word:", bg="black", fg="white").place(x=80, y=130)

    second = Entry(root, show='*')
    second.place(x=240, y=130)

    Label(root, text="Third word:", bg="black", fg="white").place(x=80, y=180)

    third = Entry(root, show='*')
    third.place(x=240, y=180)

    Label(root, text="Fourth word:", bg="black", fg="white").place(x=80, y=230)

    fourth = Entry(root, show='*')
    fourth.place(x=240, y=230)

    Label(root, text="Fifth word:", bg="black", fg="white").place(x=80, y=280)

    fifth = Entry(root, show='*')
    fifth.place(x=240, y=280)

    Label(root, text="Sixth word:", bg="black", fg="white").place(x=80, y=330)

    sixth = Entry(root, show='*')
    sixth.place(x=240, y=330)

    Button(root, text="Submit", width=20, bg="purple", fg="white", font="Helvetica",
           command=retrieve_input).place(x=170, y=400)

    root.configure(bg='black')

    root.mainloop()

    if __name__ == "__main__":
        wordstypelogin()
