import tkinter as tk
from tkinter import ttk, filedialog
import math
import itertools
import numbers
import pandas as pd

def load_csv():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        df = pd.read_csv(file_path)
        data_listbox.delete(0, tk.END)
        for col in df.columns:
            data_listbox.insert(tk.END, col)
        global csv_data
        csv_data = df

def calculate_factorial():
    try:
        x = int(entry_factorial.get())
        result = math.factorial(x)
        label_factorial_result.config(text=f"Factorial: {result}")
    except ValueError:
        label_factorial_result.config(text="Invalid input")

def calculate_inverse_factorial():
    try:
        number = int(entry_inverse_factorial.get())
        result = 1
        current = 1
        for i in itertools.count(2):
            current *= i
            if current == number:
                result = i
                break
            elif current > number:
                result = i - 1
                break
        label_inverse_factorial_result.config(text=f"Inverse Factorial: {result}")
    except ValueError:
        label_inverse_factorial_result.config(text="Invalid input")

def calculate_median():
    try:
        numbers_list = list(map(float, entry_median.get().split(',')))
        numbers_list.sort()
        n = len(numbers_list)
        if n % 2 == 0:
            median = (numbers_list[n//2 - 1] + numbers_list[n//2]) / 2
        else:
            median = numbers_list[n//2]
        label_median_result.config(text=f"Median: {median}")
    except ValueError:
        label_median_result.config(text="Invalid input")

def calculate_mean():
    try:
        numbers_list = list(map(float, entry_mean.get().split(',')))
        mean = sum(numbers_list) / len(numbers_list)
        label_mean_result.config(text=f"Mean: {mean}")
    except ValueError:
        label_mean_result.config(text="Invalid input")

def calculate_csv_statistics():
    selected_col = data_listbox.get(tk.ACTIVE)
    if selected_col and selected_col in csv_data.columns:
        col_data = csv_data[selected_col].dropna()
        mean = col_data.mean()
        median = col_data.median()
        label_csv_mean.config(text=f"Mean: {mean}")
        label_csv_median.config(text=f"Median: {median}")

root = tk.Tk()
root.title("Math Function GUI")
notebook = ttk.Notebook(root)
notebook.grid(row=0, column=0, sticky="nsew")

frame_factorial = ttk.Frame(notebook)
notebook.add(frame_factorial, text="Factorial")
entry_factorial = ttk.Entry(frame_factorial)
entry_factorial.grid(row=0, column=0, padx=5, pady=5)
button_factorial = ttk.Button(frame_factorial, text="Calculate", command=calculate_factorial)
button_factorial.grid(row=0, column=1, padx=5, pady=5)
label_factorial_result = ttk.Label(frame_factorial, text="Result: ")
label_factorial_result.grid(row=1, column=0, columnspan=2, pady=5)

frame_inverse_factorial = ttk.Frame(notebook)
notebook.add(frame_inverse_factorial, text="Inverse Factorial")
entry_inverse_factorial = ttk.Entry(frame_inverse_factorial)
entry_inverse_factorial.grid(row=0, column=0, padx=5, pady=5)
button_inverse_factorial = ttk.Button(frame_inverse_factorial, text="Calculate", command=calculate_inverse_factorial)
button_inverse_factorial.grid(row=0, column=1, padx=5, pady=5)
label_inverse_factorial_result = ttk.Label(frame_inverse_factorial, text="Result: ")
label_inverse_factorial_result.grid(row=1, column=0, columnspan=2, pady=5)

frame_statistics = ttk.Frame(notebook)
notebook.add(frame_statistics, text="Statistics")
entry_median = ttk.Entry(frame_statistics)
entry_median.grid(row=0, column=0, padx=5, pady=5)
button_median = ttk.Button(frame_statistics, text="Calculate Median", command=calculate_median)
button_median.grid(row=0, column=1, padx=5, pady=5)
label_median_result = ttk.Label(frame_statistics, text="Median: ")
label_median_result.grid(row=1, column=0, columnspan=2, pady=5)
entry_mean = ttk.Entry(frame_statistics)
entry_mean.grid(row=2, column=0, padx=5, pady=5)
button_mean = ttk.Button(frame_statistics, text="Calculate Mean", command=calculate_mean)
button_mean.grid(row=2, column=1, padx=5, pady=5)
label_mean_result = ttk.Label(frame_statistics, text="Mean: ")
label_mean_result.grid(row=3, column=0, columnspan=2, pady=5)

frame_csv = ttk.Frame(notebook)
notebook.add(frame_csv, text="CSV Statistics")
button_load_csv = ttk.Button(frame_csv, text="Load CSV", command=load_csv)
button_load_csv.grid(row=0, column=0, padx=5, pady=5)
data_listbox = tk.Listbox(frame_csv, height=5)
data_listbox.grid(row=1, column=0, padx=5, pady=5)
button_calculate_csv = ttk.Button(frame_csv, text="Calculate", command=calculate_csv_statistics)
button_calculate_csv.grid(row=2, column=0, padx=5, pady=5)
label_csv_mean = ttk.Label(frame_csv, text="Mean: ")
label_csv_mean.grid(row=3, column=0, padx=5, pady=5)
label_csv_median = ttk.Label(frame_csv, text="Median: ")
label_csv_median.grid(row=4, column=0, padx=5, pady=5)

root.mainloop()
