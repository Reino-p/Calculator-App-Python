import tkinter as tk
from tkinter import messagebox


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x600")

        self.expression = ""
        self.text_input = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Display
        text_display = tk.Entry(self.root, font=('arial', 20, 'bold'), textvariable=self.text_input, bd=30, insertwidth=4,
                                width=14, justify='right').grid(row=0, column=0, columnspan=4)

        # Buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            self.create_button(button, row_val, col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def create_button(self, value, row, column):
        button = tk.Button(self.root, text=value, padx=20, pady=20, font=('arial', 18, 'bold'),
                            command=lambda: self.button_click(value))
        button.grid(row=row, column=column)

    def button_click(self, value):
        if value == '=':
            try:
                result = str(eval(self.expression))
                self.text_input.set(result)
                self.expression = result
            except:
                messagebox.showerror("Error", "Invalid input")
                self.text_input.set("")
                self.expression = ""
        elif value == 'C':
            self.text_input.set("")
            self.expression = ""
        else:
            self.expression += str(value)
            self.text_input.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
