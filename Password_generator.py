import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip
# Creating GUI
root = tk.Tk()
root.title("Random Password Generator Using GUI")
lable = tk.Label(root,text="Password Length:")
lable.pack()
entry = tk.Entry(root)
entry.pack()  

# password complexcity options for user

complexity_label = tk.Label(root,text="Password/Security Code:")
complexity_label.pack()

LowerCase_var = tk.IntVar()
lowerCase_checkbox = tk.Checkbutton(root,text="Lowercase",variable=LowerCase_var)
lowerCase_checkbox.pack()

UpperCase_var = tk.IntVar()
upperCase_checkbox = tk.Checkbutton(root,text="Uppercase",variable=UpperCase_var)
upperCase_checkbox.pack()

Digit_var = tk.IntVar()
digitCase_checkbox = tk.Checkbutton(root,text="Digits",variable=Digit_var)
digitCase_checkbox.pack()

SpecialCase_var = tk.IntVar()
specialCase_checkbox = tk.Checkbutton(root,text="Special characters",variable=SpecialCase_var)
specialCase_checkbox.pack()

# creating function
def password_creator(Password_len,complexity_options):
    password = " "
    for _ in range(Password_len):
        char_type = random.choice(complexity_options)
        if char_type == "lower":
            password += random.choice(string.ascii_lowercase)
        elif char_type == "upper":
            password += random.choice(string.ascii_uppercase)
        elif char_type == "digit":
            password += random.choice(string.digits)
        else:
            password += random.choice(string.punctuation)
    return password

# functions for week or strong password
def password_strength(password):
    strength = "Weak"
    if len(password) >= 10:
        strength = "Strong"
    elif len(password) >= 6:
        strength  = "Medium"
    return strength

# function for clipboard
def copy_generated_password(password):
    pyperclip.copy(password)
    messagebox.showinfo("Copied")
# functions for complexcity options

def generate_password():
    complexity_options = []
    try:
        password_len = int(entry.get())
        if password_len <= 0:
            raise ValueError("Password length must be positive:")
        if LowerCase_var.get():
           complexity_options.append("lower")
        if UpperCase_var.get():
           complexity_options.append("upper")
        if Digit_var.get():
           complexity_options.append("digit")
        if SpecialCase_var.get():
           complexity_options.append("special")
        password = password_creator(password_len, complexity_options)
        password_strength_indicator.config(text=f"Password strength:{password_strength(password)}")
        print(password)
        password_entry.delete(0,tk.END)
        password_entry.insert(0,password)
        button_copy.config(command=lambda:copy_generated_password(password))
    except ValueError as e:
        messagebox.showerror("Error",str(e))



generate_button = tk.Button(root,text="Generate Password", command=generate_password)
generate_button.pack()

password_strength_indicator = tk.Label(root,text=" ")
password_strength_indicator.pack()

password_label = tk.Label(root,text="Generated Password")
password_label.pack()
password_entry = tk.Entry(root)
password_entry.pack()

button_copy = tk.Button(root, text="Copy to the clipboard", command=lambda: copy_generated_password(password_entry.get()))
button_copy.pack()

root.mainloop()

