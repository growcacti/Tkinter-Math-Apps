import tkinter as tk
from tkinter import messagebox
import heapq

class MaxProd(object):
    def __init__(self, array):
        self.array = array

    # slowest implementation
    def max_product_slow(self):
        n = sorted(self.array, reverse=True)
        return n[0] * n[1]

    # average of the three solutions
    def max_product_avg(self):
        count = 0
        m1 = m2 = float("-inf")
        for x in self.array:
            count += 1
            if x > m2:
                if x >= m1:
                    m1, m2 = x, m1
                else:
                    m2 = x
        return m1 * m2

    # faster solution
    def max_product_fast(self):
        first = max(self.array)
        second = max(n for n in self.array if n != first)
        return first * second

    # fastest solution
    def max_product_fastest(self):
        x = heapq.nlargest(2, self.array)
        return x[0] * x[1]



class GridMathOperations:
    def __init__(self):
        pass
    
        
        # Initialization if needed

    def find_largest_palindrome_product(self, n):
            
        # lower limit is 1 + the upper limit floor division of 10
        lower_limit = 1 + upper_limit // 10

        # initialize the max product
        max_product = 0

        for x in range(upper_limit, lower_limit - 1, -1):
            for y in range(x, lower_limit - 1, -1):
                product = x * y

                # short circuit early if the product is less than the max_product, no need to continue computation as this
                # already fails
                if product < max_product:
                    break

                number_str = str(product)

                # check if this is a palindrome and is greater than the max_product currently
                if number_str == number_str[::-1] and product > max_product:
                    max_product = product

        return max_product
          
    def largest_product_in_grid(self, grid):
        max_product = 0

        for x in range(20):
            for y in range(17):
                horizontal_product = (
                    grid[x][y] * grid[x][y + 1] * grid[x][y + 2] * grid[x][y + 3]
                )
                vertical_product = (
                    grid[y][x] * grid[y + 1][x] * grid[y + 2][x] * grid[y + 3][x]
                )

                if horizontal_product > max_product:
                    max_product = horizontal_product

                if vertical_product > max_product:
                    max_product = vertical_product

        for a in range(17):
            for b in range(17):
                diag_left_product = (
                    grid[a][b]
                    * grid[a + 1][b + 1]
                    * grid[a + 2][b + 2]
                    * grid[a + 3][b + 3]
                )
                diag_right_product = (
                    grid[a][b + 3]
                    * grid[a + 1][b + 2]
                    * grid[a + 2][b + 1]
                    * grid[a + 3][b]
                )

                if diag_left_product > max_product:
                    max_product = diag_left_product

                if diag_right_product > max_product:
                    max_product = diag_right_product

        return max_product


  

    def largest_product(self, num_str, sub_length):
        return (max(reduce(lambda x, y: x * y, sli) for sli in slice_me(num_str, sub_length))
        if sub_length != 0
        else 1)



class MathGUI(tk.Tk):
    def __init__(self, max_prod, grid_operations):
        super().__init__()
        self.max_prod = max_prod
        self.grid_operations = grid_operations
        self.title("Math Operations GUI")
        self.create_widgets()

    def create_widgets(self):
        # Add widgets for MaxProd operations
        # E.g., Max Product from List:
        tk.Label(self, text="Enter List for Max Product:").grid(row=0, column=0)
        self.array_entry = tk.Entry(self)
        self.array_entry.grid(row=0, column=1)
        tk.Button(self, text="Calculate Max Product", command=self.calculate_max_product).grid(row=0, column=2)

        # Add more widgets for other operations similarly...

        # Result Label
        self.result_label = tk.Label(self, text="Result will be shown here")
        self.result_label.grid(row=10, column=0, columnspan=3)

    def calculate_max_product(self):
        try:
            array = [int(item) for item in self.array_entry.get().split(',')]
            self.max_prod.array = array
            result = self.max_prod.max_product_fastest() # Choose the method you prefer
            self.result_label.config(text=f"Max Product: {result}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a list of numbers.")

        # Define methods for other operations similarly...

if __name__ == "__main__":
    max_prod = MaxProd([])
    grid_operations = GridMathOperations()
    app = MathGUI(max_prod, grid_operations)
    app.mainloop()
