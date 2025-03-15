import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import csv

class NumberCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Enhanced Number List Calculator")

        # Max number of entries
        self.max_entries = 100
        self.entry_vars = []
        self.numbers_list = []

        # Frame for input controls
        control_frame = ttk.Frame(root)
        control_frame.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        # Label and dropdown to select the number of entries
        ttk.Label(control_frame, text="Number of Entries:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_count_var = tk.IntVar(value=10)  # Default to 10
        self.entry_count_menu = ttk.Combobox(control_frame, textvariable=self.entry_count_var, 
                                             values=[i for i in range(1, self.max_entries + 1)], 
                                             width=5, state="readonly")
        self.entry_count_menu.grid(row=0, column=1, padx=5, pady=5)
        self.entry_count_menu.bind("<<ComboboxSelected>>", self.create_entries)

        # Buttons for additional features
        self.load_button = ttk.Button(control_frame, text="Load CSV", command=self.load_csv)
        self.load_button.grid(row=0, column=2, padx=5, pady=5)

        self.reset_button = ttk.Button(control_frame, text="Reset", command=self.reset_entries)
        self.reset_button.grid(row=0, column=3, padx=5, pady=5)

        self.save_button = ttk.Button(control_frame, text="Save Results", command=self.save_results)
        self.save_button.grid(row=0, column=4, padx=5, pady=5)

        # Frame to hold manual entry fields
        self.entry_frame = ttk.Frame(root)
        self.entry_frame.grid(row=1, column=0, padx=10, pady=5)

        # Frame for Listbox (for large datasets from CSV)
        self.listbox_frame = ttk.Frame(root)
        self.listbox_frame.grid(row=1, column=1, padx=10, pady=5, sticky="ns")

        ttk.Label(self.listbox_frame, text="CSV Data:").pack()
        self.listbox = tk.Listbox(self.listbox_frame, width=20, height=15)
        self.listbox.pack()

        # Labels for results
        self.sum_label = ttk.Label(root, text="Sum: 0", font=("Arial", 12, "bold"))
        self.sum_label.grid(row=2, column=0, pady=5)

        self.avg_label = ttk.Label(root, text="Average: 0", font=("Arial", 12, "bold"))
        self.avg_label.grid(row=3, column=0, pady=5)

        self.delta_label = ttk.Label(root, text="Smallest Δ: 0, Largest Δ: 0", font=("Arial", 12, "bold"))
        self.delta_label.grid(row=4, column=0, pady=5)

        # Create initial entries
        self.create_entries()

    def create_entries(self, event=None):
        """Creates or updates entry fields based on user selection."""
        # Clear previous widgets
        for widget in self.entry_frame.winfo_children():
            widget.destroy()

        # Get number of entries from dropdown
        num_entries = self.entry_count_var.get()
        self.entry_vars.clear()

        # Generate entry fields
        for i in range(num_entries):
            var = tk.StringVar()
            var.trace_add("write", lambda *args: self.calculate())  # Auto-update on change
            entry = ttk.Entry(self.entry_frame, textvariable=var, width=10)
            entry.grid(row=i, column=0, padx=5, pady=2)
            self.entry_vars.append(var)

        self.calculate()  # Update calculation when entries are changed

    def calculate(self):
        """Calculates sum, average, and delta values."""
        numbers = []
        for var in self.entry_vars:
            value = var.get().strip()
            if value:
                try:
                    num = float(value)
                    numbers.append(num)
                except ValueError:
                    continue  # Ignore invalid input

        # Include numbers from Listbox (CSV data)
        numbers.extend(self.numbers_list)

        if numbers:
            total = sum(numbers)
            avg = total / len(numbers)
            self.sum_label.config(text=f"Sum: {total}")
            self.avg_label.config(text=f"Average: {avg:.2f}")

            # Calculate deltas (differences between consecutive values)
            deltas = [abs(numbers[i] - numbers[i - 1]) for i in range(1, len(numbers))]
            if deltas:
                smallest_delta = min(deltas)
                largest_delta = max(deltas)
                self.delta_label.config(text=f"Smallest Δ: {smallest_delta:.2f}, Largest Δ: {largest_delta:.2f}")
            else:
                self.delta_label.config(text="Smallest Δ: 0, Largest Δ: 0")

        else:
            self.sum_label.config(text="Sum: 0")
            self.avg_label.config(text="Average: 0")
            self.delta_label.config(text="Smallest Δ: 0, Largest Δ: 0")

    def reset_entries(self):
        """Clears all manual entry fields and listbox data."""
        for var in self.entry_vars:
            var.set("")
        self.listbox.delete(0, tk.END)
        self.numbers_list.clear()
        self.calculate()

    def save_results(self):
        """Saves sum, average, and delta values to a text file."""
        sum_value = self.sum_label.cget("text").split(": ")[1]
        avg_value = self.avg_label.cget("text").split(": ")[1]
        delta_value = self.delta_label.cget("text").split(": ")[1]

        file_path = filedialog.asksaveasfilename(defaultextension=".txt", 
                                                 filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(f"Sum: {sum_value}\n")
                file.write(f"Average: {avg_value}\n")
                file.write(f"{delta_value}\n")
            messagebox.showinfo("Success", "Results saved successfully!")

    def load_csv(self):
        """Loads numbers from a CSV file into the Listbox."""
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")])
        if not file_path:
            return

        try:
            with open(file_path, "r") as file:
                reader = csv.reader(file)
                data = []
                for row in reader:
                    for value in row:
                        try:
                            data.append(float(value.strip()))  # Convert to float
                        except ValueError:
                            continue  # Skip non-numeric values

                if not data:
                    messagebox.showerror("Error", "No valid numbers found in the CSV file.")
                    return

                # Update Listbox
                self.listbox.delete(0, tk.END)
                self.numbers_list = data[:self.max_entries]  # Limit to 100 entries
                for num in self.numbers_list:
                    self.listbox.insert(tk.END, num)

                self.calculate()  # Update calculations
                messagebox.showinfo("Success", "CSV file loaded successfully!")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load CSV file:\n{e}")

# Run the application
root = tk.Tk()
app = NumberCalculator(root)
root.mainloop()
