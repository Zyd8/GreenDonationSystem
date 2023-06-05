import tkinter as tk
from accounts import Accounts 
from donations import Donations
from trees import Trees
from enums import *

class GUI_manager:
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x800")
        self.root.title("Green Donation System")

    def start(self):
        self.root.mainloop()

    def destroy(self):
        self.root.destroy()

Accounts.init_db()
Donations.init_db()
Trees.init_db()

current_user = None

def window_sign_in():
    gui = GUI_manager()
    
    label = tk.Label(gui.root)
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
            gui.destroy()
            return 0
        
    def handle_window_sign_up():
        gui.destroy()
        window_sign_up()

    title = tk.Label(gui.root, text="Sign in", font=("Monospace", 18))
    title.pack(padx=20, pady=20)

    entry_email = tk.Entry(gui.root)
    entry_email.pack(padx=10, pady=10)

    entry_pass = tk.Entry(gui.root)
    entry_pass.pack(padx=10, pady=10)

    confirm_button = tk.Button(gui.root, text="Confirm", font=("Monospace", 12), command=handle_confirm_button_click)
    confirm_button.pack(padx=20, pady=20)
    
    sign_up_button = tk.Button(gui.root, text="Sign up?", font=("Monospace", 12), command=handle_window_sign_up)
    sign_up_button.pack(padx=100, pady=20)
    
    gui.start()

def window_sign_up():
    gui = GUI_manager()
    
    def get_entry_widgets(root):
        entry_widgets = []
        for child in root.winfo_children():
            if isinstance(child, tk.Entry):
                entry_widgets.append(child)
        return entry_widgets
    
    # transfer all validation to Accounts class as static methods
    def create_account_button():
        label_error.config(text="")
        
        entry_widgets = get_entry_widgets(gui.root)
        for entry in entry_widgets:
            if entry.get() == "":
                label_error.configure(text="Must satisfy all fields")
                return

        if entry_pass.get() != entry_conf_pass.get():
            label_error.configure(text="Passwords do not match")
            return 
        
        object = Accounts(Accounts.rand_num_gen(), entry_email.get(), entry_pass.get())
        object.create_row()
        label_error.configure(text="Successfully created the account")
            
            
    def handle_create_account_button():
        create_account_button()
    
    def handle_back_button():
        gui.destroy()
        window_sign_in()
    
    title = tk.Label(gui.root, text="Sign up", font=("Monospace", 18))
    title.pack(padx=20, pady=20)
    
    entry_email = tk.Entry(gui.root)
    entry_email.pack(padx=10, pady=10)

    entry_pass = tk.Entry(gui.root)
    entry_pass.pack(padx=10, pady=10)
    
    entry_conf_pass = tk.Entry(gui.root)
    entry_conf_pass.pack(padx=10, pady=10)
    
    create_button = tk.Button(gui.root, text="Confirm", font=("Monospace", 12), command=handle_create_account_button)
    create_button.pack(padx=20, pady=20)
    
    back_button = tk.Button(gui.root, text="Back", font=("Monospace", 12), command=handle_back_button)
    back_button.pack(padx=20, pady=20)
    
    label_error = tk.Label(gui.root, fg="red")
    label_error.pack(padx=20, pady=20)

    gui.start()
    
window_sign_in()

