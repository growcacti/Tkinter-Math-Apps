import tkinter as tk
from tkinter import *

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


class EquationSolverApp:
    def __init__(self):
        self.root = tk.Tk()

        self.display = Entry(self.root)
        self.display1 = Entry(self.root)
        self.display.grid(row=11, columnspan=6, sticky=W + E)
        self.display1.grid(row=29, columnspan=6, sticky=W + E)

        self.label0 = Label(self.root, text="Enter the value of the equation in the format 'x1'x + 'y1'y = a and 'x2'x + 'y2'y = b.")
        self.label1 = Label(self.root, text="x1 Value : ")
        self.label2 = Label(self.root, text="y1 Value : ")
        self.label3 = Label(self.root, text="x2 Value : ")
        self.label4 = Label(self.root, text="y2 Value : ")
        self.label5 = Label(self.root, text="a Value : ")
        self.label6 = Label(self.root, text="b Value : ")
        self.label7 = Label(self.root)
        self.label8 = Label(self.root)
        self.label9 = Label(self.root)
        self.label10 = Label(self.root)
        self.label11 = Label(self.root)

        self.entry1 = Entry(self.root)
        self.entry2 = Entry(self.root)
        self.entry3 = Entry(self.root)
        self.entry4 = Entry(self.root)
        self.entry5 = Entry(self.root)
        self.entry6 = Entry(self.root)

        self.label0.grid(row=0, columnspan=6)
        self.label1.grid(row=1, column=0)
        self.label2.grid(row=1, column=2)
        self.label3.grid(row=2, column=0)
        self.label4.grid(row=2, column=2)
        self.label5.grid(row=1, column=4)
        self.label6.grid(row=2, column=4)
        self.label7.grid(row=10, column=0)
        self.label9.grid(row=10, column=1)
        self.label10.grid(row=12, columnspan=6)
        self.label11.grid(row=10, column=2)

        self.entry1.grid(row=1, column=1)
        self.entry2.grid(row=2, column=1)
        self.entry3.grid(row=1, column=3)
        self.entry4.grid(row=2, column=3)
        self.entry5.grid(row=1, column=5)
        self.entry6.grid(row=2, column=5)

        self.button1 = Button(self.label7, text="Show Entries", command=self.show_entry)
        self.button2 = Button(self.label9, text="Show Graph", command=self.show_graph)
        self.button3 = Button(self.label11, text="Show Solution", command=self.solve_eq)
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()

    def solve_eq(self):
        self.display1.delete(0, 'end')

        x1 = int(self.entry1.get())
        y1 = int(self.entry3.get())
        a = int(self.entry5.get())
        x2 = int(self.entry2.get())
        y2 = int(self.entry4.get())
        b = int(self.entry6.get())

        str1 = "The two equations do not intersect each other. They are parallel lines."
        str2 = "The two equations are the same and every point on the line is the solution."

        if (x1 == x2) and (y1 == y2) and (a != b):
            self.display1.insert(0, str1)
        elif (x1 == x2) and (y1 == y2) and (a == b):
            self.display1.insert(0, str2)
        elif x1 != x2 or y1 != y2:
            A = np.matrix([[x1, y1], [x2, y2]])
            B = np.matrix([[a], [b]])
            self.display1.insert(0, "The solution is: ")
            self.display1.insert('end', np.linalg.solve(A, B))

    def show_graph(self):
        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(1, 1, 1)
        x = np.linspace(-5, 5, 100)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('center')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')

        x1 = int(self.entry1.get())
        y1 = int(self.entry3.get())
        a = int(self.entry5.get())
        x2 = int(self.entry2.get())
        y2 = int(self.entry4.get())
        b = int(self.entry6.get())

        ya = -((x1 / y1) * x) + (a / y1)
        fig.add_subplot(1, 1, 1).plot(x, ya, label=self.entry1.get() + "x + " + self.entry3.get() + "y = " + self.entry5.get())
        yb = -((x2 / y2) * x) + (b / y2)
        fig.add_subplot(1, 1, 1).plot(x, yb, label=self.entry2.get() + "x + " + self.entry4.get() + "y = " + self.entry6.get())
        fig.legend(loc='upper left')
        canvas = FigureCanvasTkAgg(fig, master=self.label10)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack()

        toolbar = NavigationToolbar2Tk(canvas, self.label10)
        toolbar.update()
        canvas.get_tk_widget().pack()

    def show_entry(self):
        self.display.delete(0, 'end')
        t1 = "The equations are: " + self.entry1.get() + "x + " + self.entry3.get() + "y" + " = " + self.entry5.get() + " and " + self.entry2.get() + "x + " + self.entry4.get() + "y = " + self.entry6.get() + "."
        self.display.insert(0, t1)

    def run(self):
        self.root.mainloop()


app = EquationSolverApp()
app.run()
