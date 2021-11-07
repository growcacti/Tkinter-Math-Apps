#Import tkinter library
from tkinter import *
from tkinter import ttk
#Create an instance of tkinter frame or window
r= Tk()
#Set the geometry of tkinter frame
r.geometry("750x550")
# Function that take interger up 255 and show it's binary equivalent
def get_value():
    
    number=int(entry.get())
    Label(r, text=number, font= ('Century 15 bold')).pack(pady=20)
    n = int(number)
    try:
         n = "{0:b}".format(number) if number in range(0, 256) else "Invalid input"
         Label(r, text=n, font= ('Century 15 bold')).pack(pady=13)
         return n
    except TypeError:
        return "Invalid input"
    
#Create an Label and Entry Widget
Label(r, text="Convert to binary Enter number between 1 and 255", font= ('Century 15 bold')).pack(pady=32)
entry= ttk.Entry(r,font=('Century 12'),width=40)
entry.pack(pady= 30)
#Create a button to display send value to function to convert interger binary
button= ttk.Button(r, text="Enter", command= get_value)
button.pack()
# continue to loop this program so other entires can be entered
r.mainloop()
