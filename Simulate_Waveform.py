import tkinter as tk
import math
import random

class GraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Graphing Application")
        
        # Create a canvas widget
        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # Create sliders for frequency, amplitude, and phase shift adjustment for waveform 1
        self.freq_slider1 = tk.Scale(root, from_=1, to=250, orient=tk.HORIZONTAL, label="Frequency 1", command=self.update_graph)
        self.freq_slider1.grid(row=1, column=0, padx=10, pady=10)
        
        self.amp_slider1 = tk.Scale(root, from_=50, to=200, orient=tk.HORIZONTAL, label="Amplitude 1", command=self.update_graph)
        self.amp_slider1.grid(row=1, column=1, padx=10, pady=10)
        
        self.phase_slider1 = tk.Scale(root, from_=0, to=360, orient=tk.HORIZONTAL, label="Phase Shift 1", command=self.update_graph)
        self.phase_slider1.grid(row=1, column=2, padx=10, pady=10)

        # Create a dropdown menu for waveform selection for waveform 1
        self.waveform_var1 = tk.StringVar(value="Sine")
        self.waveform_menu1 = tk.OptionMenu(root, self.waveform_var1, "Sine", "Triangle", "Square", "Random", "User Made", command=self.update_graph)
        self.waveform_menu1.grid(row=1, column=3, padx=10, pady=10)

        # Entry for user-made waveform for waveform 1
        self.user_waveform_entry1 = tk.Entry(root)
        self.user_waveform_entry1.grid(row=2, column=0, columnspan=4, padx=10, pady=10)
        self.user_waveform_entry1.insert(0, "math.sin(math.radians(x * frequency + phase_shift))")

        # Checkbox to enable/disable waveform 2
        self.enable_waveform2 = tk.BooleanVar()
        self.enable_waveform2.set(False)
        self.waveform2_check = tk.Checkbutton(root, text="Enable Waveform 2", variable=self.enable_waveform2, command=self.update_graph)
        self.waveform2_check.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

        # Create sliders for frequency, amplitude, and phase shift adjustment for waveform 2
        self.freq_slider2 = tk.Scale(root, from_=1, to=250, orient=tk.HORIZONTAL, label="Frequency 2", command=self.update_graph)
        self.freq_slider2.grid(row=4, column=0, padx=10, pady=10)
        
        self.amp_slider2 = tk.Scale(root, from_=50, to=200, orient=tk.HORIZONTAL, label="Amplitude 2", command=self.update_graph)
        self.amp_slider2.grid(row=4, column=1, padx=10, pady=10)
        
        self.phase_slider2 = tk.Scale(root, from_=0, to=360, orient=tk.HORIZONTAL, label="Phase Shift 2", command=self.update_graph)
        self.phase_slider2.grid(row=4, column=2, padx=10, pady=10)

        # Create a dropdown menu for waveform selection for waveform 2
        self.waveform_var2 = tk.StringVar(value="Sine")
        self.waveform_menu2 = tk.OptionMenu(root, self.waveform_var2, "Sine", "Triangle", "Square", "Random", "User Made", command=self.update_graph)
        self.waveform_menu2.grid(row=4, column=3, padx=10, pady=10)

        # Entry for user-made waveform for waveform 2
        self.user_waveform_entry2 = tk.Entry(root)
        self.user_waveform_entry2.grid(row=5, column=0, columnspan=4, padx=10, pady=10)
        self.user_waveform_entry2.insert(0, "math.sin(math.radians(x * frequency + phase_shift))")

        # Draw the axes
        self.draw_axes()
        
        # Initial plot of the sine wave
        self.plot_waveform()
    
    def draw_axes(self):
        # Clear the canvas before drawing
        self.canvas.delete("all")
        
        # X-axis
        self.canvas.create_line(50, 200, 550, 200, fill="black")
        
        # Y-axis
        self.canvas.create_line(300, 50, 300, 350, fill="black")
        
        # X-axis labels
        for i in range(11):
            x = 50 + i * 50
            self.canvas.create_line(x, 195, x, 205, fill="black")
            self.canvas.create_text(x, 215, text=str(i-5), fill="black")
        
        # Y-axis labels
        for i in range(9):
            y = 50 + i * 50
            self.canvas.create_line(295, y, 305, y, fill="black")
            self.canvas.create_text(285, y, text=str(4-i), fill="black")
    
    def plot_waveform(self):
        # Get the current frequency, amplitude, phase shift, and waveform type for waveform 1
        frequency1 = self.freq_slider1.get()
        amplitude1 = self.amp_slider1.get()
        phase_shift1 = self.phase_slider1.get()
        waveform1 = self.waveform_var1.get()
        
        # Plot the selected waveform for waveform 1
        for x in range(500):
            x1 = 50 + x
            x2 = 50 + x + 1
            
            y1, y2 = self.calculate_waveform(waveform1, frequency1, amplitude1, phase_shift1, x)
            
            self.canvas.create_line(x1, y1, x2, y2, fill="blue")

        # Plot waveform 2 if enabled
        if self.enable_waveform2.get():
            frequency2 = self.freq_slider2.get()
            amplitude2 = self.amp_slider2.get()
            phase_shift2 = self.phase_slider2.get()
            waveform2 = self.waveform_var2.get()

            for x in range(500):
                x1 = 50 + x
                x2 = 50 + x + 1
                
                y1, y2 = self.calculate_waveform(waveform2, frequency2, amplitude2, phase_shift2, x)
                
                self.canvas.create_line(x1, y1, x2, y2, fill="red")

    def calculate_waveform(self, waveform, frequency, amplitude, phase_shift, x):
        if waveform == "Sine":
            y1 = 200 - amplitude * math.sin(math.radians(x * frequency + phase_shift))
            y2 = 200 - amplitude * math.sin(math.radians((x + 1) * frequency + phase_shift))
        elif waveform == "Triangle":
            y1 = 200 - amplitude * (2 / math.pi) * math.asin(math.sin(math.radians(x * frequency + phase_shift)))
            y2 = 200 - amplitude * (2 / math.pi) * math.asin(math.sin(math.radians((x + 1) * frequency + phase_shift)))
        elif waveform == "Square":
            y1 = 200 - amplitude * (1 if math.sin(math.radians(x * frequency + phase_shift)) >= 0 else -1)
            y2 = 200 - amplitude * (1 if math.sin(math.radians((x + 1) * frequency + phase_shift)) >= 0 else -1)
        elif waveform == "Random":
            y1 = 200 - amplitude * (random.uniform(-1, 1))
            y2 = 200 - amplitude * (random.uniform(-1, 1))
        elif waveform == "User Made":
            user_formula = self.user_waveform_entry1.get() if waveform == "User Made" else self.user_waveform_entry2.get()
            try:
                y1 = 200 - amplitude * eval(user_formula)
                y2 = 200 - amplitude * eval(user_formula.replace(f"x * frequency + phase_shift", f"(x + 1) * frequency + phase_shift"))
            except Exception as e:
                y1 = y2 = 200 # If there's an error in the user formula, default to a flat line
                print(f"Error in user waveform formula: {e}")
        return y1, y2

    def update_graph(self, event=None):
        # Clear the canvas before re-plotting
        self.canvas.delete("all")
        # Redraw the axes
        self.draw_axes()
        # Re-plot the waveform with the new settings
        self.plot_waveform()

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphApp(root)
    root.mainloop()
