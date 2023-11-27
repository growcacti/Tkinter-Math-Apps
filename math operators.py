import tkinter as tk
from tkinter import messagebox

class MathOperationsGUI(tk.Tk):
    def __init__(self, math_operations):
        super().__init__()
        self.math_operations = math_operations
        self.title("Math Operations GUI")
        self.create_widgets()

    def create_widgets(self):
        # Widgets for digit_nth_power
        tk.Label(self, text="Enter N for Nth Power:").grid(row=0, column=0)
        self.nth_power_entry = tk.Entry(self)
        self.nth_power_entry.grid(row=0, column=1)
        tk.Button(self, text="Calculate Digit Nth Power", command=self.calculate_digit_nth_power).grid(row=0, column=2)

        # Widgets for distinct_powers
        tk.Label(self, text="Enter A for Distinct Powers:").grid(row=1, column=0)
        self.a_entry = tk.Entry(self)
        self.a_entry.grid(row=1, column=1)
        tk.Label(self, text="Enter B for Distinct Powers:").grid(row=2, column=0)
        self.b_entry = tk.Entry(self)
        self.b_entry.grid(row=2, column=1)
        tk.Button(self, text="Calculate Distinct Powers", command=self.calculate_distinct_powers).grid(row=1, column=2, rowspan=2)

        # Result Label
        self.result_label = tk.Label(self, text="Result will be shown here")
        self.result_label.grid(row=3, column=0, columnspan=3)

    def calculate_digit_nth_power(self):
        try:
            nth = int(self.nth_power_entry.get())
            result = self.math_operations.digit_nth_power(nth)
            self.result_label.config(text=f"Sum of Nth Power: {result}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input for Nth Power")

    def calculate_distinct_powers(self):
        try:
            a = int(self.a_entry.get())
            b = int(self.b_entry.get())
            result = self.math_operations.distinct_powers(a, b)
            self.result_label.config(text=f"Distinct Powers: {result}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input for Distinct Powers")

if __name__ == "__main__":
    math_operations = MathOperations()
    app = MathOperationsGUI(math_operations)
    app.mainloop()
