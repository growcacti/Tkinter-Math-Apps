
import tkinter as tk
from tkinter import messagebox





class CollatzCalculator:
    def __init__(self):
        # You can add initialization logic if needed
        pass

    def generate_collatz_sequence(self, number):
        if number is None or not isinstance(number, int):
            raise ValueError(f"Invalid input {number}, this should be an integer")

        sequence = [number]

        if number == 1:
            return sequence

        # if the number is already 1, return it in a list
        while number != 1:
            # if the number is even, ie. number %2 == 0
            if number % 2 == 0:
                number //= 2
                sequence.append(number)

            # if number is odd
            elif number % 2 != 0:
                number = (3 * number) + 1
                sequence.append(number)

        return sequence
            

    def find_starting_number(self, limit):
          if limit < 0 or limit is None:
              raise ValueError(f"Expected limit to be greater than one or not None instead found {limit}")

          if limit == 1:
            # short circuit, we already have the starting point
              return limit

            # cache = {}
          current_longest = 0
          starting_num = 0
          for x in range(limit, 1, -1):
              sequence = self.generate_collatz_sequence(x)
              seq_len = len(sequence)

            # cache[x] = sequence
              if seq_len > current_longest:
                  current_longest = seq_len
                  starting_num = x
                  return starting_num

           



class CollatzGUI(tk.Tk):
    def __init__(self, collatz_calculator):
        super().__init__()
        self.collatz_calculator = collatz_calculator
        self.title("Collatz Sequence Calculator")
        self.create_widgets()

    def create_widgets(self):
        # Input for the number
        self.limit_label = tk.Label(self, text="Enter Number:")
        self.limit_label.grid(row=0, column=0)

        self.limit_entry = tk.Entry(self)
        self.limit_entry.grid(row=0, column=1)

        # Button to trigger calculation
        self.calculate_button = tk.Button(self, text="Calculate", command=self.on_calculate)
        self.calculate_button.grid(row=1, column=0, columnspan=2)

        # Label to display the number of steps
        self.steps_label = tk.Label(self, text="Number of steps will be shown here")
        self.steps_label.grid(row=2, column=0, columnspan=2)

        # Label to display the result
        self.result_label = tk.Label(self, text="Result will be shown here")
        self.result_label.grid(row=3, column=0, columnspan=2)

    def on_calculate(self):
        try:
            number = int(self.limit_entry.get())
            sequence = self.collatz_calculator.generate_collatz_sequence(number)
            num_steps = len(sequence)
            self.steps_label.config(text=f"Number of steps: {num_steps}")
            self.result_label.config(text=f"Longest Collatz sequence starts with: {number}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    collatz_calculator = CollatzCalculator()
    app = CollatzGUI(collatz_calculator)
    app.mainloop()
