import tkinter as tk
from tkinter import ttk
import calendar
from datetime import datetime as dt, timedelta

class SpinDateTime():
    def __init__(self, parent):
        self.parent = parent
        self.now = dt.now().strftime("%m %d %Y %H %M %S")
        month, day, year, hour, minute, second = self.now.split()

        self.date_frame = ttk.LabelFrame(self.parent, text="Date")
        self.date_frame.grid(row=0, column=0, padx=10, pady=5, sticky='w')
        self.display_frame = ttk.Frame(self.parent)
        self.display_frame.grid(row=3, column=0)

        self.day_var = tk.StringVar(value=day)
        self.day_spin = ttk.Spinbox(self.date_frame, from_=1, to=31, width=2, textvariable=self.day_var)
        self.day_spin.grid(row=0, column=1)

        self.month_var = tk.StringVar(value=month)
        self.month_spin = ttk.Spinbox(self.date_frame, from_=1, to=12, width=2, textvariable=self.month_var)
        self.month_spin.grid(row=0, column=0)

        self.year_var = tk.StringVar(value=year)
        self.year_spin = ttk.Spinbox(self.date_frame, from_=1900, to=2100, width=4, textvariable=self.year_var)
        self.year_spin.grid(row=0, column=2)

        self.time_frame = ttk.LabelFrame(self.parent, text="Time")
        self.time_frame.grid(row=0, column=1, padx=10, pady=5, sticky='w')

        self.hour_var = tk.StringVar(value=hour)
        self.hour_spin = ttk.Spinbox(self.time_frame, from_=0, to=23, width=2, textvariable=self.hour_var)
        self.hour_spin.grid(row=0, column=2)

        self.minute_var = tk.StringVar(value=minute)
        self.minute_spin = ttk.Spinbox(self.time_frame, from_=0, to=59, width=2, textvariable=self.minute_var)
        self.minute_spin.grid(row=0, column=3)

        self.second_var = tk.StringVar(value=second)
        self.second_spin = ttk.Spinbox(self.time_frame, from_=0, to=59, width=2, textvariable=self.second_var)
        self.second_spin.grid(row=0, column=4)

        self.display1 = tk.Entry(self.display_frame, bd=7, width=40, bg="seashell")
        self.display2 = tk.Entry(self.display_frame, bd=7, width=40, bg="seashell")
        self.display3 = tk.Entry(self.display_frame, bd=7, width=40, bg="seashell")
        self.display1.grid(row=3, column=0)
        self.display2.grid(row=5, column=0)
        self.display3.grid(row=7, column=0)

        self.btn_frame = ttk.Frame(self.parent)
        self.btn_frame.grid(row=8, column=4)

        self.btn = tk.Button(self.btn_frame, text="Pick Date and Time", bd=4, bg="light blue", command=self.on_ok)
        self.btn.grid(row=8, column=2)
        self.btn2 = tk.Button(self.btn_frame, text="Clear", bd=4, bg="seashell", command=self.clear)
        self.btn2.grid(row=9, column=2)

    def clear(self):
        self.display1.delete(0, tk.END)
        self.display2.delete(0, tk.END)
        self.display3.delete(0, tk.END)

    def on_ok(self):
        self.date = f"{self.month_var.get()}/{self.day_var.get()}/{self.year_var.get()}"
        self.time = f"{self.hour_var.get()}:{self.minute_var.get()}:{self.second_var.get()}"
        self.pick()

    def find_day(self, month, day, year):
        daynum = calendar.weekday(year, month, day)
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return days[daynum]

    def pick(self):
        self.month = int(self.month_var.get())
        self.day = int(self.day_var.get())
        self.year = int(self.year_var.get())
        self.date = f"{self.month_var.get()}/{self.day_var.get()}/{self.year_var.get()}"
        self.time = f"{self.hour_var.get()}:{self.minute_var.get()}:{self.second_var.get()}"
        dayword = calendar.weekday(self.year, self.month, self.day)
        self.dayword = self.find_day(self.month, self.day, self.year)
        self.display1.insert(0, self.date)
        self.display2.insert(0, self.time)
        self.display3.insert(0, self.dayword)
        print(self.date)
        print(self.time)
        print(self.dayword)

class CalendarDatePicker():
    def __init__(self, parent):
        self.parent = parent
        self.current_month = dt.now().month
        self.current_year = dt.now().year

        nav_frame = tk.Frame(self.parent)
        nav_frame.grid(row=0, column=5)

        prev_month_btn = tk.Button(nav_frame, text="< Prev", command=self.prev_month)
        prev_month_btn.grid(row=1, column=5)

        self.month_year_label = tk.Label(nav_frame, text="", font=("Helvetica", 16))
        self.month_year_label.grid(row=1, column=6)

        next_month_btn = tk.Button(nav_frame, text="Next >", command=self.next_month)
        next_month_btn.grid(row=1, column=7)

        self.calendar_frame = tk.Frame(self.parent)
        self.calendar_frame.grid(row=2, column=5)

        self.display_calendar(self.current_year, self.current_month)

        self.time_frame = ttk.LabelFrame(self.parent, text="Time")
        self.time_frame.grid(row=10, column=1, padx=10, pady=5, sticky='w')

        self.hour_var = tk.StringVar(value=dt.now().hour)
        self.hour_spin = ttk.Spinbox(self.time_frame, from_=0, to=23, width=10, textvariable=self.hour_var)
        self.hour_spin.grid(row=10, column=2)

        self.minute_var = tk.StringVar(value=dt.now().minute)
        self.minute_spin = ttk.Spinbox(self.time_frame, from_=0, to=59, width=10, textvariable=self.minute_var)
        self.minute_spin.grid(row=10, column=3)

        self.second_var = tk.StringVar(value=dt.now().second)
        self.second_spin = ttk.Spinbox(self.time_frame, from_=0, to=59, width=10, textvariable=self.second_var)
        self.second_spin.grid(row=10, column=4)

        self.selected_date = None

    def prev_month(self):
        if self.current_month == 1:
            self.current_month = 12
            self.current_year -= 1
        else:
            self.current_month -= 1
        self.display_calendar(self.current_year, self.current_month)

    def next_month(self):
        if self.current_month == 12:
            self.current_month = 1
            self.current_year += 1
        else:
            self.current_month += 1
        self.display_calendar(self.current_year, self.current_month)

    def display_calendar(self, year, month):
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()

        self.month_year_label.config(text=f"{calendar.month_name[month]} {year}")

        weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        for i, day in enumerate(weekdays):
            tk.Label(self.calendar_frame, text=day).grid(row=0, column=i)

        month_days = calendar.monthcalendar(year, month)
        for row_index, week in enumerate(month_days):
            for col_index, day in enumerate(week):
                if day == 0:
                    continue
                btn = tk.Button(self.calendar_frame, text=str(day), width=5, bd=8, bg="alice blue", command=lambda d=day: self.select_date(year, month, d))
                btn.grid(row=row_index + 1, column=col_index)

    def select_date(self, year, month, day):
        self.selected_date = dt(year, month, int(day), int(self.hour_var.get()), int(self.minute_var.get()), int(self.second_var.get()))
        day_of_the_week = self.selected_date.strftime('%A')
        print(f"Selected Date: {self.selected_date.strftime('%Y-%m-%d %H:%M:%S')} ({day_of_the_week})")

class AppSelector(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Time Explorer')
        self.nb = ttk.Notebook(self)

        self.f1 = ttk.Frame(self.nb)
        self.f1.grid(row=0, column=1)
        self.f2 = ttk.Frame(self.nb)
        self.f2.grid(row=0, column=2)
        self.f3 = ttk.Frame(self.nb)
        self.f3.grid(row=0, column=3)

        self.nb.add(self.f1, text='Start')
        self.nb.add(self.f2, text='Stop')
        self.nb.add(self.f3, text='Results')
        self.nb.grid(row=2, column=1)

        self.start_picker = CalendarDatePicker(self.f1)
        self.stop_picker = CalendarDatePicker(self.f2)

        self.calculate_btn = tk.Button(self.f3, text="Calculate Duration", command=self.calculate_duration)
        self.calculate_btn.grid(row=0, column=0)

        self.result_display = tk.Entry(self.f3, bd=7, width=40, bg="seashell")
        self.result_display.grid(row=1, column=0)

    def calculate_duration(self):
        start_date = self.start_picker.selected_date
        stop_date = self.stop_picker.selected_date
        if start_date and stop_date:
            duration = stop_date - start_date
            self.result_display.delete(0, tk.END)
            self.result_display.insert(0, str(duration))
        else:
            self.result_display.delete(0, tk.END)
            self.result_display.insert(0, "Please select both start and stop dates")

if __name__ == "__main__":
    app = AppSelector()
    app.mainloop()
