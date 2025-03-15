import tkinter as tk
from tkinter import ttk, messagebox
from decimal import Decimal  # For precise calculations

# Resistance per 1000 ft for Copper wire
awg_resistance = {
    0000: 0.050,  # 4/0 AWG
    000: 0.063,   # 3/0 AWG
    00: 0.079,    # 2/0 AWG
    0: 0.100,     # 1/0 AWG
    1: 0.126,
    2: 0.159,
    4: 0.253,
    6: 0.403,
    8: 0.641,
    10: 1.018,
    12: 1.619,
    14: 2.525,
    16: 4.016,
    18: 6.385,
    20: 10.15,
    22: 16.14,
    24: 25.67,
    26: 40.81,
    28: 64.94,
    30: 103.2
}

class WireCalcApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Wire AWG Calculator")
        self.create_widgets()

    def create_widgets(self):
        inputs = ["Voltage (V)", "Current (A)", "Length (ft)", "Type (AC/DC)"]
        self.entries = {}

        for idx, label in enumerate(inputs):
            ttk.Label(self, text=label).grid(row=idx, column=0, sticky="W", pady=5, padx=5)
            if label == "Type (AC/DC)":
                self.type_var = tk.StringVar(value="DC")
                ttk.OptionMenu(self, self.type_var, "DC", "DC", "AC").grid(row=idx, column=1, pady=5, padx=5, sticky="ew")
            else:
                entry = ttk.Entry(self)
                entry.grid(row=idx, column=1, pady=5, padx=5, sticky="ew")
                self.entries[label] = entry

        ttk.Button(self, text="Calculate AWG", command=self.calculate_awg).grid(row=5, column=0, columnspan=2, pady=10)
        self.result_label = ttk.Label(self, text="Recommended AWG: ")
        self.result_label.grid(row=6, column=0, columnspan=2, pady=5)

        ttk.Button(self, text="Reset", command=self.reset_fields).grid(row=7, column=0, pady=5)
        ttk.Button(self, text="Exit", command=self.quit).grid(row=7, column=1, pady=5)

    def calculate_awg(self):
        try:
            voltage = float(self.entries["Voltage (V)"].get())
            current = float(self.entries["Current (A)"].get())
            length = float(self.entries["Length (ft)"].get())

            # Allow a higher voltage drop for low-voltage systems
            if voltage < 50:
                max_v_drop = voltage * 0.05  # 5% drop for low voltage
            else:
                max_v_drop = voltage * 0.03  # 3% drop for high voltage

            recommended_awg = None
            for awg, resist in sorted(awg_resistance.items(), key=lambda x: x[1]):  # Sort by resistance
                v_drop = Decimal(2) * Decimal(length) * Decimal(current) * Decimal(resist) / Decimal(1000)
                if v_drop <= max_v_drop:
                    recommended_awg = awg
                    break

            if recommended_awg:
                self.result_label.config(text=f"Recommended AWG: {recommended_awg}")
            else:
                self.result_label.config(text="AWG 30 is sufficient for very low currents.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numeric values.")

    def reset_fields(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.result_label.config(text="Recommended AWG: ")
        self.type_var.set("DC")

if __name__ == "__main__":
    app = WireCalcApp()
    app.mainloop()
