from tkinter import *
from hashlib import sha256
from tkinter import messagebox
import registration

key = ""


def words():
    def prevpage():
        root.destroy()
        registration.reg()

    def retrive_input():
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

        elif (firstw == secondw or
              firstw == thirdw or
              firstw == fourthw or
              firstw == fifthw or
              firstw == sixthw or
              secondw == thirdw or
              secondw == fourthw or
              secondw == fifthw or
              secondw == sixthw or
              thirdw == fourthw or
              thirdw == fifthw or
              thirdw == sixthw or
              fourthw == fifthw or
              fourthw == sixthw or
              fifthw == sixthw):
            messagebox.showerror("Error", "Each field must be unique", parent=root)

        else:

            ret_string = firstw + " " + secondw + " " + thirdw + " " + fourthw + " " + fifthw + " " + sixthw

            global key
            key = sha256(ret_string.encode("utf-8")).hexdigest()
            root.destroy()

    root = Tk()
    root.title("Login type")
    words_label = Label(root, text="Enter 6 random words", bg="black", fg="white", width=20, font=("bold", 20))
    words_label.place(x=90, y=53)
    words_label.pack()

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

    Button(root, text="Save", width=20, bg="purple", fg="white", font="Helvetica", command=retrive_input).place(x=150, y=380)
    Button(root, text="Go back", width=20, bg="purple", fg="white", font="Helvetica", command=prevpage).place(x=150,
                                                                                                              y=430)

    root.configure(bg='black')

    root.mainloop()


if __name__ == "__main__":
    words()
