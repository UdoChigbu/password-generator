import tkinter as tk

def update_text():
    label.config(text="Text changed!", fg="red")

root = tk.Tk()
root.geometry("200x100")

label = tk.Label(root, text="Original", font=("Helvetica", 14))
label.pack()

button = tk.Button(root, text="Click Me", command=update_text)
button.pack()

root.mainloop()
