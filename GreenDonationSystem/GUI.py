import tkinter as tk
from accounts import Accounts 
from donations import Donations
from trees import Trees
from enums import *

Accounts.init_db()
Donations.init_db()
Trees.init_db()

current_user = None
root = tk.Tk()

def window_sign_in():
    
    def confirm_button_click():
        label.pack_forget()
        signal, id = Accounts.verify_account(entry_email.get(), entry_pass.get())
        if signal == "0":
            label.configure(text="Welcome!!")
            label.pack(padx=20, pady=20)
            return id
        elif signal == "1":
            label.configure(text="Wrong password")
            label.pack(padx=20, pady=20)
            entry_pass.delete(0, tk.END) 
            return None
        else:
            label.configure(text="Account not found")
            label.pack(padx=20, pady=20)
            entry_email.delete(0, tk.END)  
            entry_pass.delete(0, tk.END)  
            return None

    def handle_confirm_button_click():
        global current_user
        current_user = confirm_button_click()
        if current_user is not None:
            Accounts.read_row(current_user)
            root.destroy()

    global root
    root.geometry("500x300")
    root.title("Green Donation System")

    title = tk.Label(root, text="Sign in", font=("Monospace", 18))
    title.pack(padx=20, pady=20)

    entry_email = tk.Entry(root)
    entry_email.pack(padx=10, pady=10)

    entry_pass = tk.Entry(root)
    entry_pass.pack(padx=10, pady=10)

    confirm_button = tk.Button(root, text="Confirm", font=("Monospace", 12), command=handle_confirm_button_click)
    confirm_button.pack(padx=20, pady=20)
    
    sign_up_button = tk.Button(root, text="Sign up?", font=("Monospace", 12), command=window_sign_up)
    sign_up_button.pack(padx=100, pady=20)
    
    label = tk.Label(root)

    root.mainloop()
    
def window_sign_up():
    global root
    root.destroy()
    root = tk.Tk()
    root.geometry("500x300")
    root.title("Green Donation System")

    title = tk.Label(root, text="Sign up", font=("Monospace", 18))
    title.pack(padx=20, pady=20)

window_sign_in()