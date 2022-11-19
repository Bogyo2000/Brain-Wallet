from tkinter import *
from tkinter import messagebox
import os
import openpyxl
import main
import wordstypelog
import imagestypelog



def log():
    def prevpage():
        root.destroy()
        main.main()

    def username_focus():
        user_name.focus_set()

    def email_focus():
        email.focus_set()

    def login_type():
        currentdir = os.getcwd()
        file = os.path.join(currentdir, "excel.xlsx")
        wb = openpyxl.load_workbook(file)
        sheet = wb.active

        for row in sheet.iter_rows():
            if (row[0].value == user_name.get()):
                if (row[1].value == email.get()):
                    if (row[2].value == 1):
                        root.destroy()
                        wordstypelog.wordstypelogin(row[3].value)
                        return
                    else:
                        root.destroy()
                        imagestypelog.imagestypelog(row[4].value)
                        return

                else:
                    messagebox.showerror("Error", "Name and email pair doesnt exists", parent=root)
                    return

        messagebox.showerror("Error", "Name does not exists", parent=root)
        return

    root = Tk()
    root.title("Login")
    log_label = Label(root, text="Welcome back!", bg="black", fg="white", width=20, font=("bold", 20))
    log_label.place(x=90, y=53)
    log_label.pack()

    width, height = 500, 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))
    root.geometry("{}x{}+{}+{}".format(width, height, x, y))

    user_name = Entry(root, font=("bold", 10))
    email = Entry(root, font=("bold", 10))

    usr_label = Label(root, text="Username:", bg="black", fg="white", width=20, font=("bold", 10))
    usr_label.place(x=68, y=130)

    user_name.place(x=240, y=130)
    user_name.bind("<Return>", username_focus)

    email_label = Label(root, text="Email:", bg="black", fg="white", width=20, font=("bold", 10))
    email_label.place(x=68, y=180)

    email.place(x=240, y=180)
    email.bind("<Return>", email_focus)

    Button(root, width=15, text="Login", bg="purple", fg="white", font="Helvetica", relief=SOLID,
           command=login_type).place(x=170, y=230)
    Button(root, width=15, text="Go back", bg="purple", fg="white", font="Helvetica", relief=SOLID,
           command=prevpage).place(x=170, y=280)

    root.configure(bg='black')

    root.mainloop()


if __name__ == "__main__":
    log()
