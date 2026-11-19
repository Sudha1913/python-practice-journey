import tkinter as tk

def click(btn_text):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(btn_text))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Python GUI Calculator")
root.geometry("320x450")
root.config(bg="#f0f0f0")
root.resizable(False, False)

# Display Screen
entry = tk.Entry(root, font=("Arial", 22), justify="right", bg="#ffffff", fg="#000000", bd=5)
entry.pack(padx=15, pady=20, ipady=10, fill=tk.X)

# Button Frame
btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack()

buttons = [
    ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
    ('C', 3, 0), ('0', 3, 1), ('=', 3, 2), ('+', 3, 3)
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(btn_frame, text=text, font=("Arial", 16, "bold"), bg="#4CAF50", fg="white", width=5, height=2, command=calculate)
    elif text == 'C':
        btn = tk.Button(btn_frame, text=text, font=("Arial", 16, "bold"), bg="#f44336", fg="white", width=5, height=2, command=clear)
    else:
        btn = tk.Button(btn_frame, text=text, font=("Arial", 16), bg="#e0e0e0", width=5, height=2, command=lambda t=text: click(t))
    btn.grid(row=row, column=col, padx=6, pady=6)

root.mainloop()