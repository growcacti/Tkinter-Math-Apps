import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext
import math
import csv
from time import strftime

class ElectricalCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Electrical & Solar Calculation Tool")
        self.root.geometry("700x500")

        # Labels & Inputs
        ttk.Label(root, text="Voltage (V):").grid(row=0, column=0, padx=5, pady=5)
        self.voltage_var = tk.StringVar()
        ttk.Entry(root, textvariable=self.voltage_var).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(root, text="Current (A):").grid(row=1, column=0, padx=5, pady=5)
        self.current_var = tk.StringVar()
        ttk.Entry(root, textvariable=self.current_var).grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(root, text="Power (W):").grid(row=2, column=0, padx=5, pady=5)
        self.power_var = tk.StringVar()
        ttk.Entry(root, textvariable=self.power_var).grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(root, text="Energy (kWh):").grid(row=3, column=0, padx=5, pady=5)
        self.energy_var = tk.StringVar()
        ttk.Entry(root, textvariable=self.energy_var).grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(root, text="Time (Hours):").grid(row=4, column=0, padx=5, pady=5)
        self.time_var = tk.StringVar()
        ttk.Entry(root, textvariable=self.time_var).grid(row=4, column=1, padx=5, pady=5)

        # Dropdown for Calculation Type
        ttk.Label(root, text="Calculation Type:").grid(row=5, column=0, padx=5, pady=5)
        self.calc_type = tk.StringVar()
        self.calc_options = [
            "Ohm's Law", "Power", "Energy", "Solar Panel Output", "Inverter Efficiency",
            "Charger Current", "Breaker Sizing", "Battery Runtime", "Series Resistance", "Parallel Resistance"
        ]
        self.calc_dropdown = ttk.Combobox(root, textvariable=self.calc_type, values=self.calc_options, state="readonly")
        self.calc_dropdown.grid(row=5, column=1, padx=5, pady=5)
        self.calc_dropdown.set(self.calc_options[0])  # Default selection

        # Calculate Button
        self.calc_button = ttk.Button(root, text="Calculate", command=self.calculate)
        self.calc_button.grid(row=6, column=0, columnspan=2, pady=10)

        # Result Display
        self.result_var = tk.StringVar()
        ttk.Label(root, text="Result:").grid(row=7, column=0, padx=5, pady=5)
        self.result_label = ttk.Label(root, textvariable=self.result_var, font=("Arial", 12, "bold"), foreground="blue")
        self.result_label.grid(row=7, column=1, padx=5, pady=5)

        # Log Section
        self.log_text = scrolledtext.ScrolledText(root, width=70, height=10)
        self.log_text.grid(row=8, column=0, columnspan=2, padx=5, pady=5)
        self.log_text.insert(tk.END, "Calculation Log:\n")

        # Save Log & Export Buttons
        ttk.Button(root, text="Save Log", command=self.save_log).grid(row=9, column=0, pady=5)
        ttk.Button(root, text="Export to CSV", command=self.export_csv).grid(row=9, column=1, pady=5)

        # List to store calculation logs
        self.calculation_logs = []

    def calculate(self):
        try:
            voltage = float(self.voltage_var.get()) if self.voltage_var.get() else None
            current = float(self.current_var.get()) if self.current_var.get() else None
            power = float(self.power_var.get()) if self.power_var.get() else None
            energy = float(self.energy_var.get()) if self.energy_var.get() else None
            time = float(self.time_var.get()) if self.time_var.get() else None

            calc_type = self.calc_type.get()
            result = ""

            if calc_type == "Ohm's Law":
                if voltage and current:
                    result = f"Resistance: {voltage / current:.2f} Ω"
                else:
                    result = "Enter Voltage & Current"

            elif calc_type == "Power":
                if voltage and current:
                    result = f"Power: {voltage * current:.2f} W"
                else:
                    result = "Enter Voltage & Current"

            elif calc_type == "Energy":
                if power and time:
                    result = f"Energy: {power * time:.2f} kWh"
                else:
                    result = "Enter Power & Time"

            elif calc_type == "Solar Panel Output":
                if voltage and current:
                    result = f"Solar Output: {voltage * current:.2f} W"
                else:
                    result = "Enter Voltage & Current"

            elif calc_type == "Inverter Efficiency":
                if power and energy:
                    result = f"Efficiency: {(power / energy) * 100:.2f} %"
                else:
                    result = "Enter Power & Energy"

            elif calc_type == "Charger Current":
                if power and voltage:
                    result = f"Required Charging Current: {power / voltage:.2f} A"
                else:
                    result = "Enter Power & Voltage"

            elif calc_type == "Breaker Sizing":
                safety_factor = 1.25  # 25% margin
                if power and voltage:
                    result = f"Breaker Size: {(power / voltage) * safety_factor:.2f} A"
                else:
                    result = "Enter Power & Voltage"

            elif calc_type == "Battery Runtime":
                if energy and power:
                    result = f"Battery Runtime: {energy / power:.2f} Hours"
                else:
                    result = "Enter Energy & Power"

            elif calc_type == "Series Resistance":
                resistances = list(map(float, self.voltage_var.get().split(",")))
                result = f"Total Resistance: {sum(resistances):.2f} Ω"

            elif calc_type == "Parallel Resistance":
                resistances = list(map(float, self.voltage_var.get().split(",")))
                result = f"Total Resistance: {1 / sum(1/r for r in resistances):.2f} Ω"

            else:
                result = "Select a calculation type"

            self.result_var.set(result)
            timestamp = strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"{timestamp} - {calc_type}: {result}\n"
            self.log_text.insert(tk.END, log_entry)
            self.calculation_logs.append([timestamp, calc_type, result])

        except ValueError:
            self.result_var.set("Invalid Input!")

    def save_log(self):
        with open("calculation_log.txt", "w") as file:
            file.writelines(self.log_text.get("1.0", tk.END))

    def export_csv(self):
        with open("calculations.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Calculation Type", "Result"])
            writer.writerows(self.calculation_logs)

# Run Application
if __name__ == "__main__":
    root = tk.Tk()
    app = ElectricalCalculator(root)
    root.mainloop()
