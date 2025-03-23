import tkinter as tk
from tkinter import ttk
import time

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer App")

        # Create a label to display the time
        self.time_label = ttk.Label(root, text="00:00:00:000", font=("Helvetica", 48))
        self.time_label.pack(pady=20)

        # Create entries to set the countdown duration
        self.hours_entry = ttk.Entry(root, width=3, font=("Helvetica", 24))
        self.hours_entry.pack(side=tk.LEFT, padx=5)
        self.hours_entry.insert(0, "00")  # Default to 0 hours

        self.minutes_entry = ttk.Entry(root, width=3, font=("Helvetica", 24))
        self.minutes_entry.pack(side=tk.LEFT, padx=5)
        self.minutes_entry.insert(0, "01")  # Default to 1 minute

        self.seconds_entry = ttk.Entry(root, width=3, font=("Helvetica", 24))
        self.seconds_entry.pack(side=tk.LEFT, padx=5)
        self.seconds_entry.insert(0, "00")  # Default to 0 seconds

        # Create a button that will change color when the timer ends
        self.alarm_button = ttk.Button(root, text="Alarm Button", command=self.reset_timer)
        self.alarm_button.pack(pady=20)

        # Create a start button to start the timer
        self.start_button = ttk.Button(root, text="Start Timer", command=self.start_timer)
        self.start_button.pack(pady=20)

        # Create a stop button to stop the timer
        self.stop_button = ttk.Button(root, text="Stop Timer", command=self.stop_timer)
        self.stop_button.pack(pady=20)

        # Create a reset button to reset the timer
        self.reset_button = ttk.Button(root, text="Reset Timer", command=self.reset_timer)
        self.reset_button.pack(pady=20)

        # Initialize timer variables
        self.duration = 0  # Duration in milliseconds
        self.start_time = None
        self.running = False

    def start_timer(self):
        if not self.running:
            # Parse the duration from the entry widgets
            try:
                hours = int(self.hours_entry.get())
                minutes = int(self.minutes_entry.get())
                seconds = int(self.seconds_entry.get())
                self.duration = (hours * 3600 + minutes * 60 + seconds) * 1000  # Convert to milliseconds
            except ValueError:
                self.duration = 60000  # Default to 1 minute if parsing fails

            self.start_time = time.time()
            self.running = True
            self.update_timer()

    def update_timer(self):
        if self.running:
            elapsed_time = int((time.time() - self.start_time) * 1000)  # Convert to milliseconds
            remaining_time = self.duration - elapsed_time

            if remaining_time <= 0:
                self.time_label.config(text="00:00:00:000")
                self.alarm_button.config(style="Alarm.TButton")
                self.running = False
            else:
                hours, remainder = divmod(remaining_time, 3600000)
                minutes, remainder = divmod(remainder, 60000)
                seconds, milliseconds = divmod(remainder, 1000)
                time_str = f"{hours:02}:{minutes:02}:{seconds:02}:{milliseconds:03}"
                self.time_label.config(text=time_str)
                self.root.after(10, self.update_timer)  # Update every 10 milliseconds

    def stop_timer(self):
        self.running = False

    def reset_timer(self):
        self.running = False
        self.time_label.config(text="00:00:00:000")
        self.alarm_button.config(style="TButton")

if __name__ == "__main__":
    root = tk.Tk()

    # Define a style for the alarm button when the timer ends
    style = ttk.Style()
    style.configure("Alarm.TButton", background="red")

    app = TimerApp(root)
    root.mainloop()
