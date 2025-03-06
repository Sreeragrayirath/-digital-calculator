import tkinter as tk
from tkinter import messagebox

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Digital Calculator")
        self.geometry("300x400")
        self.configure(bg="lightgray")
        self.expression = ""
        self.create_widgets()

    def create_widgets(self):
        self.display = tk.Entry(self, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4)
        self.display.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        row_val = 1
        col_val = 0
        for button_text in buttons:
            button = tk.Button(self, text=button_text, padx=20, pady=20, font=("Arial", 15),
                               command=lambda txt=button_text: self.on_button_click(txt))
            button.grid(row=row_val, column=col_val, sticky="nsew")
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception as e:
                messagebox.showerror("Error", "Invalid Expression")
                self.expression = ""
        else:
            self.expression += str(char)
        self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

if __name__ == '__main__':
    calculator = Calculator()
    calculator.mainloop()
