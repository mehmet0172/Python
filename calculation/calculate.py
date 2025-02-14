import tkinter as tk
from tkinter import font

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Profesyonel Hesap Makinesi")
        self.root.geometry("400x600")
        self.root.configure(bg="#2E3440")

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Giriş alanı
        input_frame = tk.Frame(self.root, width=400, height=50, bd=0, highlightbackground="#4C566A", highlightcolor="#4C566A", highlightthickness=2, bg="#3B4252")
        input_frame.pack(side=tk.TOP)

        input_field = tk.Entry(input_frame, font=('Helvetica', 24), textvariable=self.input_text, width=50, bg="#3B4252", fg="#ECEFF4", bd=0, justify=tk.RIGHT)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)

        # Butonlar
        buttons_frame = tk.Frame(self.root, width=400, height=450, bg="#2E3440")
        buttons_frame.pack()

        # Butonların yerleşimi
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row_val = 0
        col_val = 0

        for button in buttons:
            if button == '=':
                btn = tk.Button(buttons_frame, text=button, fg="#ECEFF4", width=20, height=3, bd=0, bg="#4C566A", cursor="hand2", command=lambda: self.evaluate())
                btn.grid(row=row_val, column=col_val, columnspan=2, padx=1, pady=1)
                col_val += 1
            elif button == 'C':
                btn = tk.Button(buttons_frame, text=button, fg="#ECEFF4", width=10, height=3, bd=0, bg="#BF616A", cursor="hand2", command=lambda: self.clear())
                btn.grid(row=row_val, column=col_val, padx=1, pady=1)
            else:
                btn = tk.Button(buttons_frame, text=button, fg="#ECEFF4", width=10, height=3, bd=0, bg="#4C566A", cursor="hand2", command=lambda b=button: self.append(b))
                btn.grid(row=row_val, column=col_val, padx=1, pady=1)

            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def append(self, value):
        self.expression += str(value)
        self.input_text.set(self.expression)

    def clear(self):
        self.expression = ""
        self.input_text.set("")

    def evaluate(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except Exception as e:
            self.input_text.set("Hata")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()