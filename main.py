import tkinter
from tkinter import messagebox
from tkinter import font

def register():
    login_user = login.get()
    password = password1.get()
    if len(login_user) > 2 and password == password2.get():
        with open("user.txt", 'a') as file:
            file.write(f"{login_user} : {password}\n")
        messagebox.showinfo("OK")
    else:
        messagebox.showerror("Error")

window = tkinter.Tk()
# print(len(font.families()))
# print(font.families())
window.geometry("400x300")
window.resizable(False, False)
window.title("Login and Password")

desc = tkinter.Label(window, text="SignUp", font=("Arial", 18, "italic"), pady=15)
desc.pack()

login_label = tkinter.Label(window, text="Input Login", font=("Arial", 12, "italic"))
login_label.pack()
login = tkinter.Entry(window, font=("Arial", 18, "italic"), width=15)
login.pack()

pass_label = tkinter.Label(window, text="Input Password", font=("Arial", 12, "italic"))
pass_label.pack()
password1 = tkinter.Entry(window, font=("Arial", 16, "italic"), width=16, show="*")
password1.pack()

pass_label2 = tkinter.Label(window, text="Confirm password",  font=("Arial", 12, "italic"))
pass_label2.pack()
password2 = tkinter.Entry(window, font=("Arial", 16, "italic"), width=16,  show="*" )
password2.pack()

btn = tkinter.Button(window, text="Enter", width=15, command=register)
btn.pack(pady=10)

tkinter.mainloop()