import tkinter as tk

def confirm_button_clicked():
    email = entry_email.get() 
    password = entry_pass.get()  
    print("Email:", email)
    print("Password:", password)

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
