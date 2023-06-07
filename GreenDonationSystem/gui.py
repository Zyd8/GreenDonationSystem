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
        
def get_widgets(root, type):
    widgets = []
    for child in root.winfo_children():
        if isinstance(child, type):
            widgets.append(child)
    return widgets

Accounts.init_db()
Donations.init_db()
Trees.init_db()

current_user = None

def window_sign_in():
    gui = GUI_manager()
    
    label = tk.Label(gui.root)
    def confirm_btn_click():
        label.pack_forget()
        signal, id = Accounts.verify_account(ent_email.get(), ent_pass.get())
        if signal == "0":
            label.configure(text="Welcome!!")
            label.pack(padx=20, pady=20)
            return id
        elif signal == "1":
            label.configure(text="Wrong password")
            label.pack(padx=20, pady=20)
            ent_pass.delete(0, tk.END) 
            return None
        else:
            label.configure(text="Account not found")
            label.pack(padx=20, pady=20)
            ent_email.delete(0, tk.END)  
            ent_pass.delete(0, tk.END)  
            return None

    def handle_confirm_btn():
        global current_user
        current_user = confirm_btn_click()
        if current_user is not None:
            Accounts.read_row(current_user)
            gui.destroy()
            window_donor_base()
            return 0
        
    def handle_window_sign_up():
        gui.destroy()
        window_sign_up()

    title = tk.Label(gui.root, text="Sign in", font=("Monospace", 18))
    title.pack(padx=20, pady=20)

    ent_email = tk.Entry(gui.root)
    ent_email.pack(padx=10, pady=10)

    ent_pass = tk.Entry(gui.root)
    ent_pass.pack(padx=10, pady=10)

    confirm_btn = tk.Button(gui.root, text="Confirm", font=("Monospace", 12), command=handle_confirm_btn)
    confirm_btn.pack(padx=20, pady=20)
    
    sign_up_btn = tk.Button(gui.root, text="Sign up?", font=("Monospace", 12), command=handle_window_sign_up)
    sign_up_btn.pack(padx=100, pady=20)
    
    gui.start()
    

def window_sign_up():
    gui = GUI_manager()
    
    def create_account_btn():
        label_error.config(text="")
        
        entry_widgets = get_widgets(gui.root, tk.Entry)
        for entry in entry_widgets:
            if entry.get() == "":
                label_error.configure(text="Must satisfy all fields")
                return

        if Accounts.pass_align(ent_pass, ent_conf_pass):
            label_error.configure(text="Password did not match")
            return
        
        object = Accounts(Accounts.rand_num_gen(), ent_email.get(), ent_pass.get())
        object.create_row()
        label_error.configure(text="Successfully created the account")
        return True
            
    def handle_create_account_btn():
        if create_account_btn():
            gui.destroy()
            window_donor_base()
    
    def handle_back_btn():
        gui.destroy()
        window_sign_in()
    
    title = tk.Label(gui.root, text="Sign up", font=("Monospace", 18))
    title.pack(padx=20, pady=20)
    
    ent_email = tk.Entry(gui.root)
    ent_email.pack(padx=10, pady=10)

    ent_pass = tk.Entry(gui.root)
    ent_pass.pack(padx=10, pady=10)
    
    ent_conf_pass = tk.Entry(gui.root)
    ent_conf_pass.pack(padx=10, pady=10)
    
    create_btn = tk.Button(gui.root, text="Confirm", font=("Monospace", 12), command=handle_create_account_btn)
    create_btn.pack(padx=20, pady=20)
    
    back_btn = tk.Button(gui.root, text="Back", font=("Monospace", 12), command=handle_back_btn)
    back_btn.pack(padx=20, pady=20)
    
    label_error = tk.Label(gui.root, fg="red")
    label_error.pack(padx=20, pady=20)

    gui.start()
    
    
def window_donor_base():
    gui = GUI_manager()
    
    def handle_general_btn():
        gui.destroy
        window_general_base()
    
    def handle_trees_btn():
        pass
    
    def handle_ocean_btn():
        pass
    
    btn_frame = tk.Frame(gui.root)
    btn_frame.pack(padx=20, pady=20)
    
    # always make the tkinter component always be the abrreviated prefix. example btn_trees

    general_btn = tk.Button(btn_frame, text="General", font=("Monospace", 12), command=handle_general_btn)
    trees_btn = tk.Button(btn_frame, text="Trees", font=("Monospace", 12), command=handle_trees_btn)
    ocean_btn = tk.Button(btn_frame, text="Ocean", font=("Monospace", 12), command=handle_ocean_btn)

    general_btn.grid(row=0, column=0, padx=10, pady=10)
    trees_btn.grid(row=0, column=1, padx=10, pady=10)
    ocean_btn.grid(row=0, column=2, padx=10, pady=10)

    btn_frame.columnconfigure(0, weight=1) 
    gui.start()
    
    
def window_general_base():
    Donations.extend_row(current_user) 
    
    gui = GUI_manager()   
    
    def confirm_btn_click():
        object = Donations()
        Donations.alter_row(object, current_user, DonColumn.MONEY, int(ent_money.get()))
    
    def handle_confirm_btn():
        confirm_btn_click()
    
    ent_frame = tk.Frame(gui.root)
    ent_frame.pack(padx=20, pady=20)
    
    ent_money = tk.Entry(gui.root)
    ent_money.pack(padx=10, pady=10)
    
    confirm_btn = tk.Button(gui.root, text="Confirm", font=("Monospace", 12), command=handle_confirm_btn)
    confirm_btn.pack(padx=20, pady=20)
    
    gui.start()
    


def window_trees_base():
    pass

def window_ocean_base():
    pass

    
window_sign_in()

