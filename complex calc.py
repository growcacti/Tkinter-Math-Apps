import tkinter as tk
from tkinter import messagebox
import math
class ComplexCalculatorGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Complex Number Calculator")
        self.create_widgets()

    def create_widgets(self):
        # Input fields for the first complex number
        tk.Label(self, text="First Complex Number (a+bi):").grid(row=0, column=0, columnspan=2)
        tk.Label(self, text="Real:").grid(row=1, column=0)
        self.real1_entry = tk.Entry(self)
        self.real1_entry.grid(row=1, column=1)
        tk.Label(self, text="Imaginary:").grid(row=2, column=0)
        self.imag1_entry = tk.Entry(self)
        self.imag1_entry.grid(row=2, column=1)

        # Input fields for the second complex number
        tk.Label(self, text="Second Complex Number (a+bi):").grid(row=3, column=0, columnspan=2)
        tk.Label(self, text="Real:").grid(row=4, column=0)
        self.real2_entry = tk.Entry(self)
        self.real2_entry.grid(row=4, column=1)
        tk.Label(self, text="Imaginary:").grid(row=5, column=0)
        self.imag2_entry = tk.Entry(self)
        self.imag2_entry.grid(row=5, column=1)

        # Operation buttons
        tk.Button(self, text="+", command=lambda: self.operate('+')).grid(row=6, column=0)
        tk.Button(self, text="-", command=lambda: self.operate('-')).grid(row=6, column=1)
        tk.Button(self, text="*", command=lambda: self.operate('*')).grid(row=7, column=0)
        tk.Button(self, text="/", command=lambda: self.operate('/')).grid(row=7, column=1)
        tk.Button(self, text="Mod", command=self.modulus).grid(row=8, column=0, columnspan=2)

        # Label to display the result
        self.result_label = tk.Label(self, text="Result will be shown here")
        self.result_label.grid(row=9, column=0, columnspan=2)

    def operate(self, operation):
        try:
            c1 = Complex(float(self.real1_entry.get()), float(self.imag1_entry.get()))
            c2 = Complex(float(self.real2_entry.get()), float(self.imag2_entry.get()))
            if operation == '+':
                result = c1 + c2
            elif operation == '-':
                result = c1 - c2
            elif operation == '*':
                result = c1 * c2
            elif operation == '/':
                result = c1 / c2
            self.result_label.config(text=f"Result: {result}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

    def modulus(self):
        try:
            c1 = Complex(float(self.real1_entry.get()), float(self.imag1_entry.get()))
            result = c1.mod()
            self.result_label.config(text=f"Modulus: {result.real:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    app = ComplexCalculatorGUI()
    app.mainloop()
