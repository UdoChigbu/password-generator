import tkinter as tk
from tkinter import messagebox
import string
import random
import pyperclip

def generate_password():
    length = length_var.get()
    if length <= 0:
        messagebox.showwarning("Warning", "Password length must be greater than 0")
        return

    characters = ""
    if use_uppercase.get():
        characters += string.ascii_uppercase
    if use_lowercase.get():
        characters += string.ascii_lowercase
    if use_digits.get():
        characters += string.digits
    if use_symbols.get():
        characters += string.punctuation

    if not characters:
        messagebox.showwarning("Warning", "Select at least one character type")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

def copy_to_clipboard():
    pyperclip.copy(password_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# Variables
length_var = tk.IntVar(value=12)
password_var = tk.StringVar()
use_uppercase = tk.BooleanVar(value=True)
use_lowercase = tk.BooleanVar(value=True)
use_digits = tk.BooleanVar(value=True)
use_symbols = tk.BooleanVar(value=False)

# Widgets
tk.Label(root, text="Password Length:").pack(pady=5)
tk.Entry(root, textvariable=length_var, width=5).pack()

tk.Checkbutton(root, text="Include Uppercase Letters", variable=use_uppercase).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Include Lowercase Letters", variable=use_lowercase).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Include Numbers", variable=use_digits).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Include Symbols", variable=use_symbols).pack(anchor="w", padx=20)

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)
tk.Entry(root, textvariable=password_var, width=40).pack(pady=5)
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=5)

root.mainloop()
