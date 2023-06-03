import tkinter as tk
from accounts import Accounts 
from enums import *

Accounts.init_db()

current_user = None

def confirm_button_clicked(): 
    signal, id = Accounts.verify_account(entry_email.get(), entry_pass.get())
    global current_user
    if signal == "0":
        label = tk.Label(root, text="Welcome!!", font=("Monospace", 12))
        label.pack(padx=20, pady=20)
        current_user = id
        return
    elif signal == "1":
        label = tk.Label(root, text="Wrong password", font=("Monospace", 12))
        label.pack(padx=20, pady=20)
        return
    else:
        label = tk.Label(root, text="Account not found", font=("Monospace", 12))
        label.pack(padx=20, pady=20)
        return

root = tk.Tk()

root.geometry("800x500")
root.title("Green Donation System")

label = tk.Label(root, text="Sign in", font=("Monospace", 18))
label.pack(padx=20, pady=20)

entry_email = tk.Entry(root)
entry_email.pack(padx=10, pady=10)

entry_pass = tk.Entry(root)
entry_pass.pack(padx=10, pady=10)

button = tk.Button(root, text="Confirm", font=("Monospace", 12), command=confirm_button_clicked)
button.pack(padx=20, pady=20)

root.mainloop()
