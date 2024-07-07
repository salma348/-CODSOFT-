import random
import string
import tkinter as tk
from tkinter import messagebox
def generate_password(length):  
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def on_generate():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Length must be a positive integer.")
        password = generate_password(length)
        result_label.config(text=f"Generated password: {password}")
    except ValueError as e:
        messagebox.showerror("Invalid input", f"Error: {e}")
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.config(bg="#2E3B4E") 
label_font = ("Helvetica", 12, "bold")
entry_font = ("Helvetica", 12)
button_font = ("Helvetica", 12, "bold")
result_font = ("Helvetica", 12, "italic")
label_fg = "#EAECEE"
entry_bg = "#ABB2B9"
entry_fg = "#000000"
button_bg = "#5DADE2"
button_fg = "#FFFFFF"
result_fg = "#D4AC0D"
tk.Label(root, text="Enter the desired length of the password:", font=label_font, fg=label_fg, bg="#2E3B4E").pack(pady=10)
length_entry = tk.Entry(root, font=entry_font, bg=entry_bg, fg=entry_fg)
length_entry.pack(pady=5)
generate_button = tk.Button(root, text="Generate Password", font=button_font, bg=button_bg, fg=button_fg, command=on_generate)
generate_button.pack(pady=10)
result_label = tk.Label(root, text="", font=result_font, fg=result_fg, bg="#2E3B4E")
result_label.pack(pady=10)
root.mainloop()
