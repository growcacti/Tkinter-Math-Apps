from tkinter import *

class BinaryCalculator:
    def __init__(self, window):
        self.window = window
        self.window.title("Standard Binary Calculator")
        self.window.resizable(0, 0)

        # Creating a StringVar to store the value of the entry field
        self.e1_val = StringVar()

        # Creating the entry field
        self.e1 = Entry(self.window, textvariable=self.e1_val, width=50)
        self.e1.grid(row=0, column=0, columnspan=4)

        # Creating number buttons
        self.create_button("1", 1, 0, self.f2)
        self.create_button("0", 1, 1, self.f3)
        self.create_button("C", 1, 2, self.f1)
        self.create_button("=", 1, 3, self.f4)

        # Creating operator buttons
        self.create_button("+", 2, 0, self.f5)
        self.create_button("-", 2, 1, self.f6)
        self.create_button("X", 2, 2, self.f8)
        self.create_button("/", 2, 3, self.f7)

        # Creating additional buttons
        self.create_button("+/-", 3, 0, self.negate)
        self.create_button("⌫", 3, 1, self.backspace)
        self.create_button("Bin to Dec", 3, 2, self.on_binary, 12)
        self.create_button("Dec to Bin", 3, 3, self.on_decimal, 12)

    def create_button(self, text, row, column, command, width=8, height=2):
        Button(self.window, text=text, width=width, height=height, command=command).grid(row=row, column=column)

    # Function to clear the entry field
    def f1(self):
        self.e1.delete(first=0, last=len(self.e1_val.get()))

    # Function to add "1" to the entry field
    def f2(self):
        self.e1.insert(END, "1")

    # Function to add "0" to the entry field
    def f3(self):
        self.e1.insert(END, "0")

    # Function to evaluate the expression and display the result
    def f4(self):
        s = self.e1_val.get()
        result = self.evaluate_expression(s)
        self.e1.delete(first=0, last=len(s))
        self.e1.insert(END, result)

    # Functions to add operators to the entry field
    def f5(self):
        self.e1.insert(END, "+")

    def f6(self):
        self.e1.insert(END, "-")

    def f7(self):
        self.e1.insert(END, "/")

    def f8(self):
        self.e1.insert(END, "X")

    # Function to negate the sign of the number
    def negate(self):
        s = self.e1_val.get()
        if s.startswith("-"):
            self.e1_val.set(s[1:])
        else:
            self.e1_val.set("-" + s)

    # Function to delete the last character in the entry field
    def backspace(self):
        s = self.e1_val.get()
        self.e1_val.set(s[:-1])

    # Function to convert binary to decimal
    def binary_to_decimal(self, n):
        num = int(n)
        dec_value = 0
        base = 1
        while num:
            last_digit = num % 10
            num = num // 10
            dec_value += last_digit * base
            base = base * 2
        return dec_value

    # Function to convert decimal to binary
    def decimal_to_binary(self, n):
        if n == 0:
            return '0'
        binary = ''
        while n > 0:
            binary = str(n % 2) + binary
            n = n // 2
        return binary

    # Function to evaluate the expression
    def evaluate_expression(self, expression):
        flag = 1
        for i in range(len(expression)):
            if expression[i] in ['/', 'X', '+', '-']:
                flag = 0
                a = expression[:i]
                b = expression[i + 1:]
                if expression[i] == '-':
                    return self.sub(int(a), int(b))
                elif expression[i] == '/':
                    return str(int(int(a) / int(b)))
                elif expression[i] == 'X':
                    return str(int(int(a) * int(b)))
                elif expression[i] == '+':
                    return self.add(int(a), int(b))
        return ""

    # Function to perform binary addition
    def add(self, x, y):
        a = self.binary_to_decimal(x)
        b = self.binary_to_decimal(y)
        c = a + b
        return self.decimal_to_binary(c)

    # Function to perform binary subtraction
    def sub(self, x, y):
        a = self.binary_to_decimal(x)
        b = self.binary_to_decimal(y)
        c = a - b
        return self.decimal_to_binary(c)

    # Function to convert binary to decimal and update entry field
    def on_binary(self):
        s = self.e1_val.get()
        decimal = self.binary_to_decimal(s)
        self.e1_val.set(str(decimal))

    # Function to convert decimal to binary and update entry field
    def on_decimal(self):
        s = self.e1_val.get()
        binary = self.decimal_to_binary(int(s))
        self.e1_val.set(binary)

# Main program execution
if __name__ == "__main__":
    window = Tk()
    calculator = BinaryCalculator(window)
    window.mainloop()
