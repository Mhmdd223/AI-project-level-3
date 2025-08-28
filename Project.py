import tkinter as tk

window = tk.Tk()
window.title("Calculator")


    # Entry
entry_var = tk.StringVar()
entry = tk.Entry(window, textvariable=entry_var, font=("Arial", 20), justify='right', bd=10, relief=tk.RIDGE)
entry.grid(row=0, column=0, columnspan=4)

    # Buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

    # Print the number on button
for (txt, row, col) in buttons:
    btn = tk.Button(window, text=txt, font=("Arial", 20), width=5, height=2, command=lambda t=txt: on_click(t))
    btn.grid(row=row, column=col)


    # The C and = operations
def on_click(button_text):
    if button_text == "C":
        entry_var.set("")
    elif button_text == "=":
        try:
            result = eval(entry_var.get())
            entry_var.set(result)
        except:
            entry_var.set("Error")
    else:
        entry_var.set(entry_var.get() + button_text)

window.mainloop()
