import tkinter as tk
from tkinter import *
"""A Collatz Sequence Program."""
r = tk.Tk()
r.geometry("800x1200")
r.title("Collatz Sequence Program to Prove it is not a waste of time")

lb = tk.Listbox(r, width=40, height=40)
lb.grid(row=5, column=2, rowspan=4, columnspan=3)
# Recursion-based version

def collatz(number):
    """Collatz the number and print each step and tracks the number of them."""
    if number > 1:
        steps = 0
        while number != 1:
            if number % 2 == 0:
                print(int(number / 2))
                lb.insert(5, int(number))
                lb.insert(4, int(number / 2))
                number = number / 2
                steps += 1
            else:
                print(int(number * 3 + 1))
                lb.insert(3, int(number * 3 +1))
                number = number * 3 + 1
                steps += 1
        print('Collatz sequence finished in ' + str(steps) + ' steps')
        
        lb.insert(1, 'Collatz sequence finished in ' + str(steps) + ' steps')
    else:
        lb.insert(6, "so Whatsssuupppp")
    
    

def clearlist():
    lb.delete(0, tk.END)


p = tk.IntVar()
sp = tk.Entry(r, textvariable=p)
sp.grid(row=1, column=1)
#number = int(p.get())
print(p.get())
bnt = tk.Button(r, text="Collatz Seq 3n+1", bg="light green", command=lambda:collatz(p.get()))
bnt.grid(row=2, column=0)
bnt2 = tk.Button(r, text="clear", bg="light blue", command=clearlist)
bnt2.grid(row=4, column=0)
tk.Label(r, text="837799 has 524 steps").grid(row=5,column=0)
tk.Label(r, text="Which may be most under 10e6").grid(row=6, column=0)    
