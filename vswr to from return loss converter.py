import tkinter as tk
from math import log10, pow

def vswr_to_return_loss(vswr):
    return -20 * log10((vswr - 1) / (vswr + 1))

def return_loss_to_vswr(return_loss):
    return (1 + pow(10, return_loss / 20)) / (1 - pow(10, return_loss / 20))

def calculate():
    try:
        if vswr_var.get():
            vswr = float(vswr_entry.get())
            if vswr <= 1:
                raise ValueError("VSWR must be greater than 1.")
            result = vswr_to_return_loss(vswr)
            result_label.config(text=f"Return Loss: {result:.2f} dB")
        else:
            return_loss = float(return_loss_entry.get())
            result = return_loss_to_vswr(return_loss)
            result_label.config(text=f"VSWR: {result:.2f}")
    except ValueError as e:
        result_label.config(text=f"Error: {e}")
def clear():
    vswr_entry.delete(0, tk.END)
    return_loss_entry.delete(0, tk.END)
    
# Create the main window
root = tk.Tk()
root.title("RF Conversion Tool")

# Define variables
vswr_var = tk.BooleanVar()

# Create widgets
vswr_entry = tk.Entry(root)
return_loss_entry = tk.Entry(root)
calculate_btn = tk.Button(root, text="Calculate", command=calculate)
clear_btn = tk.Button(root, text="Clear", command=clear)
result_label = tk.Label(root, text="Result")
vswr_radio = tk.Radiobutton(root, text="VSWR to Return Loss (use top entry example 1.5)", variable=vswr_var, value=True)
return_loss_radio = tk.Radiobutton(root, text="Return Loss to VSWR (Use bottom entry example -14", variable=vswr_var, value=False)

# Arrange widgets using grid
vswr_radio.grid(row=0, column=0, sticky="w")
return_loss_radio.grid(row=1, column=0, sticky="w")
vswr_entry.grid(row=0, column=1, padx=5, pady=5)
return_loss_entry.grid(row=1, column=1, padx=5, pady=5)
calculate_btn.grid(row=4, column=0, columnspan=2, pady=5)
clear_btn.grid(row=4, column=1, pady=5)
result_label.grid(row=5, column=0, columnspan=2)

# Set the column configuration for alignment
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Start the GUI event loop
root.mainloop()
