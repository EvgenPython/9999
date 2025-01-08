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
def login_enter():
    window.destroy()
    window_signin()
    with open('user.txt', 'r') as file:
        data = file.readlines()
    res = []
    for elem in data:
        res.append(elem.replace("\n", ""))
    user_dict = {}
    for elem in res:
        log = elem[:elem.find(":")-1]
        pswd = elem[elem.find(":")+2:]
        user_dict[log] = pswd



def window_signin():
    window = tkinter.Tk()
    window.geometry("400x350")
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
    btn = tkinter.Button(window, text="SignIn", width=15, command=register)
    btn.pack(pady=50)
    tkinter.mainloop()

window = tkinter.Tk()
# print(len(font.families()))
# print(font.families())
window.geometry("400x350")
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
btn_login = tkinter.Button(window, text="Login", width=15, command=login_enter)
btn_login.pack(pady=2)
tkinter.mainloop()