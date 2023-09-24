import tkinter as tk

def on_button_click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.delete(0, tk.END)
            screen.insert(tk.END, result)
        except Exception as e:
            screen.delete(0, tk.END)
            screen.insert(tk.END, "Error")
    elif text == "C":
        screen.delete(0, tk.END)
    else:
        screen.insert(tk.END, text)

root = tk.Tk()
root.geometry("500x600")
root.title("Calculator")

screen = tk.Entry(root, font=("Helvetica", 20), bd=10, insertwidth=4, width=14, justify="right")
screen.pack(fill="both", expand=True)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C"
]

row, col = 1, 0

for button_text in buttons:
    button = tk.Button(button_frame, text=button_text, font=("Helvetica", 20), width=5, height=2)
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Button-1>", on_button_click)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
