import tkinter as tk
import math

class GraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Graphing Application")
        
        # Create a canvas widget
        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # Create sliders for frequency, amplitude, and phase shift adjustment
        self.freq_slider = tk.Scale(root, from_=1, to=200, orient=tk.HORIZONTAL, label="Frequency Hz", command=self.update_graph)
        self.freq_slider.grid(row=1, column=0, padx=10, pady=10)
        
        self.amp_slider = tk.Scale(root, from_=50, to=200, orient=tk.HORIZONTAL, label="Amplitude mV", command=self.update_graph)
        self.amp_slider.grid(row=1, column=1, padx=10, pady=10)
        
        self.phase_slider = tk.Scale(root, from_=0, to=360, orient=tk.HORIZONTAL, label="Phase Shift °", command=self.update_graph)
        self.phase_slider.grid(row=1, column=2, padx=10, pady=10)

        # Create a dropdown menu for waveform selection
        self.waveform_var = tk.StringVar(value="Sine")
        self.waveform_menu = tk.OptionMenu(root, self.waveform_var, "Sine", "Triangle", "Square", command=self.update_graph)
        self.waveform_menu.grid(row=1, column=3, padx=10, pady=10)
        
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
        # Get the current frequency, amplitude, phase shift, and waveform type
        frequency = self.freq_slider.get()
        amplitude = self.amp_slider.get()
        phase_shift = self.phase_slider.get()
        waveform = self.waveform_var.get()
        
        # Plot the selected waveform
        for x in range(500):
            x1 = 50 + x
            x2 = 50 + x + 1
            
            if waveform == "Sine":
                y1 = 200 - amplitude * math.sin(math.radians(x * frequency + phase_shift))
                y2 = 200 - amplitude * math.sin(math.radians((x + 1) * frequency + phase_shift))
            elif waveform == "Triangle":
                y1 = 200 - amplitude * (2 / math.pi) * math.asin(math.sin(math.radians(x * frequency + phase_shift)))
                y2 = 200 - amplitude * (2 / math.pi) * math.asin(math.sin(math.radians((x + 1) * frequency + phase_shift)))
            elif waveform == "Square":
                y1 = 200 - amplitude * (1 if math.sin(math.radians(x * frequency + phase_shift)) >= 0 else -1)
                y2 = 200 - amplitude * (1 if math.sin(math.radians((x + 1) * frequency + phase_shift)) >= 0 else -1)
            
            self.canvas.create_line(x1, y1, x2, y2, fill="blue")

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
