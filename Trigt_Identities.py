import tkinter as tk
from tkinter import ttk, messagebox
import math
import matplotlib.pyplot as plt
import numpy as np

class TrigCalculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Trig Identity Calculator")
        self.geometry("500x500")
        self.configure(padx=10, pady=10)

        # Angle Entry
        ttk.Label(self, text="Enter Angle:").grid(row=0, column=0, padx=5, pady=5)
        self.angle_entry = ttk.Entry(self, width=10)
        self.angle_entry.grid(row=0, column=1, padx=5, pady=5)

        # Unit Selection
        self.angle_type = tk.StringVar(value="degrees")
        ttk.Radiobutton(self, text="Degrees", variable=self.angle_type, value="degrees").grid(row=0, column=2)
        ttk.Radiobutton(self, text="Radians", variable=self.angle_type, value="radians").grid(row=0, column=3)

        # Identity Selection
        ttk.Label(self, text="Select Identity:").grid(row=1, column=0, columnspan=2, pady=5)

        self.identity_var = tk.StringVar(value="sin")
        identities = ["sin", "cos", "tan", "sin(A+B)", "cos(A+B)", "tan(A+B)", "sin(-A)", "cos(-A)", "tan(-A)",
                      "sin(2A)", "cos(2A)", "tan(2A)", "Pythagorean"]

        self.identity_menu = ttk.Combobox(self, values=identities, textvariable=self.identity_var, state="readonly")
        self.identity_menu.grid(row=1, column=2, columnspan=2)
        self.identity_menu.current(0)

        # Compute Button
        ttk.Button(self, text="Calculate", command=self.calculate_identity).grid(row=2, column=0, columnspan=2, pady=5)

        # Convert Button
        ttk.Button(self, text="Convert Deg ↔ Rad", command=self.convert_angle).grid(row=2, column=2, columnspan=2, pady=5)

        # Result Display
        self.result_label = ttk.Label(self, text="Result: ", font=("Arial", 12))
        self.result_label.grid(row=3, column=0, columnspan=4, pady=10)

        # Plot Button
        ttk.Button(self, text="Plot Graphs", command=self.plot_graphs).grid(row=4, column=0, columnspan=4, pady=10)

    def get_angle(self):
        """Retrieve and convert the angle input based on user selection"""
        try:
            angle = float(self.angle_entry.get())
            if self.angle_type.get() == "degrees":
                angle = math.radians(angle)  # Convert to radians
            return angle
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number.")
            return None

    def calculate_identity(self):
        """Perform trigonometric identity calculations"""
        angle = self.get_angle()
        if angle is None:
            return

        identity = self.identity_var.get()
        result = None

        if identity == "sin":
            result = math.sin(angle)
        elif identity == "cos":
            result = math.cos(angle)
        elif identity == "tan":
            result = math.tan(angle)
        elif identity == "sin(A+B)":
            result = math.sin(angle) + math.sin(angle)  # Example with same angle
        elif identity == "cos(A+B)":
            result = math.cos(angle) * math.cos(angle) - math.sin(angle) * math.sin(angle)
        elif identity == "tan(A+B)":
            result = (math.tan(angle) + math.tan(angle)) / (1 - math.tan(angle) * math.tan(angle))
        elif identity == "sin(-A)":
            result = -math.sin(angle)
        elif identity == "cos(-A)":
            result = math.cos(angle)
        elif identity == "tan(-A)":
            result = -math.tan(angle)
        elif identity == "sin(2A)":
            result = 2 * math.sin(angle) * math.cos(angle)
        elif identity == "cos(2A)":
            result = math.cos(angle) ** 2 - math.sin(angle) ** 2
        elif identity == "tan(2A)":
            result = (2 * math.tan(angle)) / (1 - math.tan(angle) ** 2)
        elif identity == "Pythagorean":
            sin_val = math.sin(angle)
            cos_val = math.cos(angle)
            result = f"sin² + cos² = {sin_val**2 + cos_val**2:.4f} (should be 1)"

        if result is not None:
            self.result_label.config(text=f"Result: {result:.4f}")

    def convert_angle(self):
        """Convert between degrees and radians"""
        try:
            angle = float(self.angle_entry.get())
            if self.angle_type.get() == "degrees":
                converted = math.radians(angle)
                self.result_label.config(text=f"{angle}° = {converted:.4f} rad")
            else:
                converted = math.degrees(angle)
                self.result_label.config(text=f"{angle} rad = {converted:.4f}°")
        except ValueError:
            messagebox.showerror("Conversion Error", "Enter a valid number.")

    def plot_graphs(self):
        """Plot sin(x), cos(x), tan(x) graphs"""
        x = np.linspace(-2 * np.pi, 2 * np.pi, 400)
        y_sin = np.sin(x)
        y_cos = np.cos(x)
        y_tan = np.tan(x)

        plt.figure(figsize=(8, 6))
        plt.plot(x, y_sin, label="sin(x)")
        plt.plot(x, y_cos, label="cos(x)")
        plt.plot(x, y_tan, label="tan(x)", linestyle="dashed")

        plt.ylim(-2, 2)
        plt.axhline(0, color="black", linewidth=0.5)
        plt.axvline(0, color="black", linewidth=0.5)
        plt.title("Trig Functions")
        plt.legend()
        plt.grid()
        plt.show()

if __name__ == "__main__":
    app = TrigCalculator()
    app.mainloop()
