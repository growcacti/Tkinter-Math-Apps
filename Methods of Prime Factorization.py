import tkinter as tk
from tkinter import ttk, messagebox
import math
import pyperclip
import random

class PrimeFactorizationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Prime Factorization Tool")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        # Title Label
        ttk.Label(root, text="Prime Factorization", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=3, pady=10)

        # Entry for input number
        ttk.Label(root, text="Enter Number:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_number = ttk.Entry(root, width=20)
        self.entry_number.grid(row=1, column=1, padx=10, pady=5)

        # Combobox for method selection
        ttk.Label(root, text="Method:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.method_var = tk.StringVar()
        self.method_combobox = ttk.Combobox(root, textvariable=self.method_var, state="readonly", width=25)
        self.method_combobox["values"] = ("Trial Division", "Sieve of Eratosthenes", "Pollard's Rho", "Fermat's Method")
        self.method_combobox.grid(row=2, column=1, padx=10, pady=5)
        self.method_combobox.current(0)  # Default selection

        # Compute Button
        self.compute_button = ttk.Button(root, text="Compute", command=self.compute_factors)
        self.compute_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Listbox for displaying results
        self.listbox = tk.Listbox(root, height=10, width=40)
        self.listbox.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

        # Scrollbar
        scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.listbox.yview)
        scrollbar.grid(row=4, column=2, sticky="ns")
        self.listbox.config(yscrollcommand=scrollbar.set)

        # Buttons
        self.clear_button = ttk.Button(root, text="Clear", command=self.clear_results)
        self.clear_button.grid(row=5, column=0, pady=10)

        self.copy_button = ttk.Button(root, text="Copy", command=self.copy_results)
        self.copy_button.grid(row=5, column=1, pady=10)

        self.exit_button = ttk.Button(root, text="Exit", command=root.quit)
        self.exit_button.grid(row=5, column=2, pady=10)

    def compute_factors(self):
        """Compute prime factors based on the selected method."""
        try:
            num = int(self.entry_number.get())
            if num <= 1:
                messagebox.showwarning("Invalid Input", "Enter a number greater than 1.")
                return

            method = self.method_var.get()
            self.listbox.delete(0, tk.END)

            if method == "Trial Division":
                factors = self.trial_division(num)
            elif method == "Sieve of Eratosthenes":
                factors = self.sieve_factorization(num)
            elif method == "Pollard's Rho":
                factors = self.pollards_rho(num)
            elif method == "Fermat's Method":
                factors = self.fermat_factorization(num)

            for factor in factors:
                self.listbox.insert(tk.END, factor)

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.")

    def trial_division(self, n):
        """Prime factorization using trial division."""
        factors = []
        while n % 2 == 0:
            factors.append(2)
            n //= 2
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                factors.append(i)
                n //= i
        if n > 1:
            factors.append(n)
        return factors

    def sieve_factorization(self, n):
        """Prime factorization using precomputed primes (Sieve of Eratosthenes)."""
        def sieve(limit):
            primes = []
            is_prime = [True] * (limit + 1)
            for num in range(2, limit + 1):
                if is_prime[num]:
                    primes.append(num)
                    for multiple in range(num * num, limit + 1, num):
                        is_prime[multiple] = False
            return primes

        primes = sieve(int(math.sqrt(n)) + 1)
        factors = []
        for p in primes:
            while n % p == 0:
                factors.append(p)
                n //= p
        if n > 1:
            factors.append(n)
        return factors

    def pollards_rho(self, n):
        """Pollard's Rho Algorithm for prime factorization."""
        if n % 2 == 0:
            return [2] + self.pollards_rho(n // 2)

        def f(x, c, mod):
            return (x * x + c) % mod

        x = random.randint(2, n - 1)
        y = x
        c = random.randint(1, n - 1)
        d = 1

        while d == 1:
            x = f(x, c, n)
            y = f(f(y, c, n), c, n)
            d = math.gcd(abs(x - y), n)

        if d == n:
            return [n]
        return self.pollards_rho(d) + self.pollards_rho(n // d)

    def fermat_factorization(self, n):
        """Fermat's factorization method."""
        factors = []
        if n % 2 == 0:
            while n % 2 == 0:
                factors.append(2)
                n //= 2

        x = math.isqrt(n)
        while x * x < n:
            x += 1

        y = math.sqrt(x * x - n)
        while not y.is_integer():
            x += 1
            y = math.sqrt(x * x - n)

        y = int(y)
        factors.append(x - y)
        factors.append(x + y)
        return factors

    def clear_results(self):
        """Clear listbox and input entry."""
        self.listbox.delete(0, tk.END)
        self.entry_number.delete(0, tk.END)

    def copy_results(self):
        """Copy results to clipboard."""
        factors = self.listbox.get(0, tk.END)
        if factors:
            pyperclip.copy(", ".join(map(str, factors)))
            messagebox.showinfo("Copied", "Prime factors copied to clipboard.")
        else:
            messagebox.showwarning("No Data", "Nothing to copy.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PrimeFactorizationApp(root)
    root.mainloop()
