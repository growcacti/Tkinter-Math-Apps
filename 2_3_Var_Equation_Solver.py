import tkinter as tk
from tkinter import ttk, messagebox, filedialog, Toplevel, Button, Text
import platform
import os
import shutil

class EquationSolverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Equation Solver")
        self.create_files()
        self.create_menu()
        self.create_notebook()
        self.create_bindings()

    def create_files(self):
        # Create a history file if it doesn't exist
        open(os.path.join(os.getcwd(), "History.txt"), "a").close()

    def create_menu(self):
        main_menu = tk.Menu(self.root)

        # File menu
        file_menu = tk.Menu(main_menu, tearoff=0)
        main_menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="History location", command=self.show_history_location)
        file_menu.add_command(label="Change History location", command=self.askopen)
        file_menu.add_command(label="Exit", command=self.root.quit, accelerator="Ctrl+E")

        # Edit menu
        edit_menu = tk.Menu(main_menu, tearoff=0)
        main_menu.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Clear All", command=self.clear_all, accelerator="Ctrl+C")
        edit_menu.add_separator()
        edit_menu.add_command(label="Show History", command=self.show_history, accelerator="Ctrl+H")
        edit_menu.add_command(label="Clear History", command=self.clear_history, accelerator="Ctrl+D")

        # Background color submenu
        theme_menu = tk.Menu(edit_menu, tearoff=0)
        edit_menu.add_cascade(label='Background Colour', menu=theme_menu)
        for color in ["Black", "Red", "Blue", "Grey", "Default"]:
            theme_menu.add_command(label=color, command=lambda c=color: self.change_background(c))

        # Help menu
        help_menu = tk.Menu(main_menu, tearoff=0)
        main_menu.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="Help", command=self.show_help, accelerator="Ctrl+A")

        # Quit menu
        quit_menu = tk.Menu(main_menu, tearoff=0)
        main_menu.add_cascade(label="Quit", menu=quit_menu)
        quit_menu.add_command(label="Quit", command=self.close)

        self.root.config(menu=main_menu)

    def create_notebook(self):
        self.notebook = ttk.Notebook(self.root)
        self.page1 = tk.Frame()
        self.page2 = tk.Frame()
        self.notebook.add(self.page1, text="2 Equation 2 variable")
        self.notebook.add(self.page2, text="3 Equation 3 variable")
        self.notebook.pack(expand=True, fill="both")

        self.create_page_widgets(self.page1, 2)
        self.create_page_widgets(self.page2, 3)

    def create_page_widgets(self, page, num_eq):
        text_widget = tk.Text(page, bd=12, bg="light cyan")
        text_widget.grid(row=12, column=3)
        page.output_text = text_widget

        label_frame = tk.LabelFrame(page, text=f"{num_eq} Equation {num_eq} variable")
        label_frame.grid(row=0, column=0, padx=80, pady=40)
       

        # Create instructional labels
        instructions = [
            (f"Input must be in this manner: {' + '.join(['A' + chr(120 + i) for i in range(num_eq)])} = {'D' if num_eq == 3 else 'C'}", 0, 0, 40),
            ("EXAMPLE - ", 2, 0, 10),
            ("For the equations: ", 3, 0, 20),
            (" + ".join([f"{i+1}x + {i+2}y = {i+3}" for i in range(num_eq)]), 4, 5, 12),
            ("You would enter - ", 6, 0, 16),
            ("Equation 1 - " + " ".join([str(i+1) for i in range(num_eq)]), 7, 2, 17),
            ("Equation 2 - " + " ".join([str(i+2) for i in range(num_eq)]), 8, 2, 18),
            ("Click SOLVE for the answers:", 10, 0, 28),
            ("x = 3", 11, 7, 5),
            ("y = 2", 11, 13, 5),
            ("Equation 1 - ", 15, 0, 14),
            ("A = ", 15, 12, 6),
            ("B = ", 15, 18, 6),
            ("C = ", 15, 24, 6),
            ("Equation 2 - ", 17, 0, 14),
            ("A = ", 17, 12, 6),
            ("B = ", 17, 18, 6),
            ("C = ", 17, 24, 6)
        ]

        for text, row, col, colspan in instructions:
            ttk.Label(label_frame, text=text, foreground="#000066" if "EXAMPLE" not in text else "#D03928").grid(row=row, column=col, columnspan=colspan, sticky=tk.W)

        # Create entry fields for equations
        vars_list = [[tk.StringVar() for _ in range(num_eq + 1)] for _ in range(num_eq)]
        for i in range(num_eq):
            for j in range(num_eq + 1):
                tk.Entry(label_frame, bd=7,width=5, textvariable=vars_list[i][j]).grid(row=15 + 2 * i, column=16 + 6 * j)

        # Store the variables in the page's attribute
        page.vars = vars_list

        # Create SOLVE and RESET buttons
        tk.Button(page,bd=4, bg="orange", text="SOLVE", width=12, command=lambda: self.solve_eq(page, num_eq)).grid(row=1, column=0)
        tk.Button(page, text="RESET",bd=4, bg="light blue", width=12, command=lambda: self.clear_eq(page, num_eq)).grid(row=2, column=0)
       
    def create_bindings(self):
        # Bind keyboard shortcuts
        self.root.bind("<Control-c>", self.clear_all)
        self.root.bind("<Control-C>", self.clear_all)
        self.root.bind("<Control-h>", self.show_history)
        self.root.bind("<Control-H>", self.show_history)
        self.root.bind("<Control-d>", self.clear_history)
        self.root.bind("<Control-D>", self.clear_history)
        self.root.bind("<Control-a>", self.show_help)
        self.root.bind("<Control-A>", self.show_help)
        self.root.bind("<Control-e>", self.root.quit)
        self.root.bind("<Control-E>", self.root.quit)

    def show_history_location(self):
        # Display the location of the history file
        messagebox.showinfo("History location", os.getcwd())

    def askopen(self):
        # Ask the user to select a new directory for the history file
        result = filedialog.askdirectory(parent=self.root, initialdir=os.getcwd(), title="Select a Folder")
        try:
            shutil.move(os.path.join(os.getcwd(), "History.txt"), os.path.join(result, "History.txt"))
        except (FileNotFoundError, PermissionError) as e:
            messagebox.showerror("Error", str(e))
        else:
            os.chdir(result)

    def clear_all(self, event=None):
        # Clear all input fields
        for page in [self.page1, self.page2]:
            for var_list in page.vars:
                for var in var_list:
                    var.set("")

    def show_history(self, event=None):
        # Open the history file with the default application
        file = os.path.join(os.getcwd(), "History.txt")
        current_os = platform.system()

        try:
            if current_os == 'Windows':
                os.startfile(file)
            elif current_os == 'Darwin':  # macOS
                subprocess.call(['open', file])
            elif current_os == 'Linux':
                subprocess.call(['xdg-open', file])
            else:
                raise OSError(f"Unsupported operating system: {current_os}")
        except Exception as e:
            print(f"An error occurred while trying to open the file: {e}")

    def clear_history(self, event=None):
        # Clear the history file
        history_file = os.path.join(os.getcwd(), "History.txt")
        if os.stat(history_file).st_size == 0:
            messagebox.showerror("Error", "Nothing to clear")
        else:
            open(history_file, "w").close()
            messagebox.showinfo("History", "Cleared")

    def show_help(self, event=None):
        # Display the help information
        def close_help():
            top.destroy()

        help_text = """
        Equation solver is an application which helps us to solve 2 equations in 2 variables or
        3 equations in 3 variables in just a click.

        For 2 equations 2 variables: 
        Equation 1 - a1x + b1y = c1
        Equation 2 - a2x + b2y = c2

        First equation A is "enter number", B is "enter number", C is "enter number"
        Second Equation A is "enter number", B is "enter number", C is "enter number"

        For 3 equations 3 variables: 
        Equation 1 - a1x + b1y + c1z = d1
        Equation 2 - a2x + b2y + c2z = d2
        Equation 3 - a3x + b3y + c3z = d3

        First equation A is "enter number", B is "enter number", C is "enter number", D is "enter number"
        Second Equation A is "enter number", B is "enter number", C is "enter number", D is "enter number"
        Third Equation A is "enter number", B is "enter number", C is "enter number", D is "enter number"
        """
        top = Toplevel()
        txt = Text(top, bd=8, width=100, height=35)
        txt.grid(row=1, column=1)
        txt.insert("1.0", help_text)
        btn = Button(top, bd=6, bg="orange", command=close_help)
        btn.grid(row=12, column=1)

    def change_background(self, color):
        # Change background color of the pages
        self.page1.config(background=color)
        self.page2.config(background=color)

    def solve_eq(self, page, num_eq):
        # Solve the equations based on the number of variables
        coefficients = []
        for var_list in page.vars:
            row = []

            for var in var_list:
                try:
                    # Convert the input to float to handle both integers and floating-point numbers
                    row.append(float(var.get()))
                except ValueError:
                    # Show an error message if the input is not a valid number
                    messagebox.showerror("Error", "Please enter valid numbers in all fields.")
                    return
            coefficients.append(row)

        if num_eq == 2:
            a1, b1, c1 = coefficients[0]
            a2, b2, c2 = coefficients[1]
            try:
                # Calculate the determinant
                det = (a1 * b2) - (a2 * b1)
                if det == 0:
                    raise ZeroDivisionError
                # Calculate the values of x and y
                x = ((c1 * b2) - (c2 * b1)) / det
                y = ((c2 * a1) - (a2 * c1)) / det
            except ZeroDivisionError:
                # Show an error message if the determinant is zero
                messagebox.showerror("Error", "The equations are either dependent or inconsistent (division by zero).")
                return

            # Show the result in a message box
            

            messagebox.showinfo("Result", f"x = {x} and y = {y}")
            answer = f"Equations:\n{a1}x + {b1}y = {c1}, {a2}x + {b2}y = {c2}\nSolution - x = {x}, y = {y}\n)"
            page.output_text.delete("1.0", tk.END)
            page.output_text.insert(tk.END, answer)

            page.output_text.delete(0, tk.END)
            page.output_text.insert(tk.END, answer)

            # Save the result to the history file
            with open(os.path.join(os.getcwd(), "History.txt"), "a") as f:
                f.write(f"Equations:\n{a1}x + {b1}y = {c1}, {a2}x + {b2}y = {c2}\nSolution - x = {x}, y = {y}\n")

        elif num_eq == 3:
            a1, b1, c1, d1 = coefficients[0]
            a2, b2, c2, d2 = coefficients[1]
            a3, b3, c3, d3 = coefficients[2]
            try:
                # Calculate the determinant
                det = (a1 * b2 * c3) - (a1 * b3 * c2) - (b1 * a2 * c3) + (b1 * a3 * c2) + (c1 * a2 * b3) - (c1 * a3 * b2)
                if det == 0:
                    raise ZeroDivisionError
                # Calculate the values of x, y, and z
                x = (((d1 * b2 * c3) - (d1 * b3 * c2) - (b1 * d2 * c3) + (b1 * d3 * c2) + (c1 * d2 * b3) - (c1 * d3 * b2)) / det)
                y = (((a1 * d2 * c3) - (a1 * d3 * c2) - (d1 * a2 * c3) + (d1 * a3 * c2) + (c1 * a2 * d3) - (c1 * a3 * d2)) / det)
                z = (((a1 * b2 * d3) - (a1 * b3 * d2) - (b1 * a2 * d3) + (b1 * a3 * d2) + (d1 * a2 * b3) - (d1 * a3 * b2)) / det)
            except ZeroDivisionError:
                # Show an error message if the determinant is zero
                messagebox.showerror("Error", "The equations are either dependent or inconsistent (division by zero).")
                return

            # Show the result in a message boxpage.
            
            answer =  f"x = {x}, y = {y}, z = {z}"
            messagebox.showinfo("Result", f"x = {x}, y = {y}, z = {z}")
            equation = (f"Equations:\n{a1}x + {b1}y + {c1}z = {d1}, {a2}x + {b2}y + {c2}z = {d2}, {a3}x + {b3}y + {c3}z = {d3}\nSolution - x = {x}, y = {y}, z = {z}\n")

            answer= (f"- x = {x}, y = {y}, z = {z}\n")
            page.output_text.delete("1.0", tk.END)
            page.output_text.insert(tk.END, equation)
            page.output_text.insert(tk.END, answer)

            # Save the result to the history file
            with open(os.path.join(os.getcwd(), "History.txt"), "a") as f:
                f.write(f"Equations:\n{a1}x + {b1}y + {c1}z = {d1}, {a2}x + {b2}y + {c2}z = {d2}, {a3}x + {b3}y + {c3}z = {d3}\nSolution - x = {x}, y = {y}, z = {z}\n")

    def clear_eq(self, page, num_eq):
        # Clear the input fields for the equations
        for var_list in page.vars:
            for var in var_list:
                var.set("")

    def close(self):
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = EquationSolverApp(root)
    root.mainloop()
