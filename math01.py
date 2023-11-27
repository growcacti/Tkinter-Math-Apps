import tkinter as tk
from tkinter import messagebox

# Include your mathematical functions here
# ...

def sum_of_divisors(n):
    return sum(divisor_generator(n)) + 1


def abundance_of_num(n):
    return sum_of_divisors(n) - n


def abundance(n):
    if n == 0:
        return []

    abundant_numbers = []
    start_number = 12

    while len(abundant_numbers) < n:
        if is_abundant(start_number):
            abundant_numbers.append((start_number, abundance_of_num(start_number)))
        start_number += 1

    return list(map(itemgetter(0), sorted(abundant_numbers, key=lambda x: x[1])))



def is_deficient(n):
    """
    Checks if a number is deficient, i.e. has sum of divisors that is less than n
    Example:

    >>> is_deficient(35)
    True

    :param n: Number to check for deficiency
    :type n int
    :return: True if the sum is less than the number, False otherwise
    :rtype: bool
    """

    return sum_of_divisors(n) < n


def is_abundant(n):
    """
    Checks if a number is abundant, i.e. has sum of divisors that exceed n
    Example:

    >>> is_abundant(12)
    True

    :param n: Number to check for abundancy
    :type n int
    :return: True if the sum exceeds the number, False otherwise
    :rtype: bool
    """
    return sum_of_divisors(n) > n

# Event handler for the calculate button
def on_calculate():
    try:
        number = int(number_entry.get())
        function = function_var.get()
        if function == 'Deficient':
            result = is_deficient(number)
        elif function == 'Abundant':
            result = is_abundant(number)
        # Add more conditions for other functions
        else:
            result = "Function not selected"
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

# Main window
root = tk.Tk()
root.title("Math Function Processor")

# Widgets
number_label = tk.Label(root, text="Enter a Number:")
number_label.grid(row=0, column=0)

number_entry = tk.Entry(root)
number_entry.grid(row=0, column=1)

function_var = tk.StringVar()
function_choices = ['Deficient', 'Abundant']  # Add more function names
function_var.set(function_choices[0])  # default value

function_menu = tk.OptionMenu(root, function_var, *function_choices)
function_menu.grid(row=1, column=0, columnspan=2)

calculate_button = tk.Button(root, text="Calculate", command=on_calculate)
calculate_button.grid(row=2, column=0, columnspan=2)

result_label = tk.Label(root, text="Result:")
result_label.grid(row=3, column=0, columnspan=2)

# Start the application
root.mainloop()
