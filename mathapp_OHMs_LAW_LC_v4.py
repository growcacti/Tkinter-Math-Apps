import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
import math

r = tk.Tk()
r.geometry('1200x800')
r.title("Electro PY JH APPS")
notebook = ttk.Notebook(r)
notebook.grid(row=0, column=0)
f0 = ttk.Frame(notebook)
notebook.add(f0, text="MAIN")
f1 = ttk.Frame(notebook)
f2 = ttk.Frame(notebook)
notebook.add(f1, text='Ohms law V/I')
notebook.add(f2, text='Ohms law V/R')

f3 = ttk.Frame(notebook)
notebook.add(f3, text='Ohms law I/R')
f4 = ttk.Frame(notebook, height=100, width=100)
notebook.add(f4, text='Resonant Freq Calc')
f5 = ttk.Frame(notebook)
notebook.add(f5, text='Resistor Calc')
f6 = ttk.Frame(notebook)
notebook.add(f6, text='6')
f7 = ttk.Frame(notebook)
notebook.add(f7, text='7')
f8 = ttk.Frame(notebook)
notebook.add(f8, text='8')
f8 = ttk.Frame(notebook)
notebook.add(f8, text='8')
f9 = ttk.Frame(notebook)
notebook.add(f9, text='9')
f10 = ttk.Frame(notebook)
notebook.add(f10, text='10')



      

def generate():
    try:
        result = float(num1.get()) / float(num2.get())
        result2 = float(num1.get()) * float(num2.get())
    except Exception as ex:
        print(ex)
        result = 'error'

    num3.set(result)
    num4.set(result2)

# --- main ---



num1 = tk.StringVar()
num2 = tk.StringVar()
num3 = tk.StringVar()
num4 = tk.StringVar()
tk.Label(f1, text=" Input Volts:").grid(row=0, column=0)
tk.Label(f1, text="Input Current in Amps:").grid(row=1, column=0)
tk.Label(f1, text=" Output Ohms:").grid(row=2, column=0)
tk.Label(f1, text="Output Watts:").grid(row=3, column=0)

tk.Entry(f1, textvariable=num1).grid(row=0, column=1)
tk.Entry(f1, textvariable=num2).grid(row=1, column=1)
tk.Entry(f1, textvariable=num3).grid(row=2, column=1)
tk.Entry(f1, textvariable=num4).grid(row=3, column=1)
lb1 = tk.Listbox(f1)
lb1.grid(row=6,  column=1) 
def showcontent(*args):
    a = num1.get()
    b = num2.get()
    c = num3.get()
    d = num4.get()
 
    lb1.insert(1, a)
    lb1.insert(2, b)
    lb1.insert(3, c)
    lb1.insert(4, d)

btn1= tk.Button(f1, text="Calculate", command=generate)
btn1.grid(row=4, column=1)


btn2 = tk.Button(f1, text="Send txt", command=showcontent)
btn2.grid(row=5, column=1)




def generate2():
    try:
        result = float(num5.get()) / float(num6.get())
        result2 = float(num5.get()) * float(num5.get()) / float(num6.get())
    except Exception as ex:
        print(ex)
        result = 'error'

    num7.set(result)
    num8.set(result2)

# --- main ---



num5 = tk.StringVar()
num6 = tk.StringVar()
num7 = tk.StringVar()
num8 = tk.StringVar()
tk.Label(f2, text=" Input Volts:").grid(row=0, column=0)
tk.Label(f2, text="Input Ohms:").grid(row=1, column=0)
tk.Label(f2, text=" Output Amps:").grid(row=2, column=0)
tk.Label(f2, text="Output Watts:").grid(row=3, column=0)

tk.Entry(f2, textvariable=num5).grid(row=0, column=1)
tk.Entry(f2, textvariable=num6).grid(row=1, column=1)
tk.Entry(f2, textvariable=num7).grid(row=2, column=1)
tk.Entry(f2, textvariable=num8).grid(row=3, column=1)
lb2 = tk.Listbox(f2)
lb2.grid(row=6,  column=1) 
def show2(*args):
    a = num5.get()
    b = num6.get()
    c = num7.get()
    d = num8.get()
 
    lb2.insert(1, a)
    lb2.insert(2, b)
    lb2.insert(3, c)
    lb2.insert(4, d)

btn4= tk.Button(f2, text="Calculate", command=generate2)
btn4.grid(row=4, column=1)


btn6 = tk.Button(f2, text="Send txt", command=show2)
btn6.grid(row=5, column=1)


def generate3():
    try:
        result = float(num11.get()) * float(num22.get())
        result2 =  float(num22.get()) * float(num22.get()) / float(num11.get())
    except Exception as ex:
        print(ex)
        result = 'error'

    num33.set(result)
    nume44.set(result2)

# --- main ---



num11 = tk.StringVar()
num22 = tk.StringVar()
num33 = tk.StringVar()
nume44 = tk.StringVar()
tk.Label(f3, text=" Input Ohms:").grid(row=0, column=0)
tk.Label(f3, text="Input Current in Amps:").grid(row=1, column=0)
tk.Label(f3, text=" Output Volts:").grid(row=2, column=0)
tk.Label(f3, text="Output Watts:").grid(row=3, column=0)

tk.Entry(f3, textvariable=num11).grid(row=0, column=1)
tk.Entry(f3, textvariable=num22).grid(row=1, column=1)
tk.Entry(f3, textvariable=num33).grid(row=2, column=1)
tk.Entry(f3, textvariable=nume44).grid(row=3, column=1)
lb3 = tk.Listbox(f3)
lb3.grid(row=6,  column=1) 
def showcontent3(*args):
    a = num11.get()
    b = num22.get()
    c = num33.get()
    d = nume44.get()
 
    lb3.insert(1, a)
    lb3.insert(2, b)
    lb3.insert(3, c)
    lb3.insert(4, d)

btn22= tk.Button(f3, text="Calculate", command=generate3)
btn22.grid(row=4, column=1)


btn33 = tk.Button(f3, text="Send txt", command=showcontent3)
btn33.grid(row=5, column=1)

#--------------------------------------
#   TAB4
#--------------------------------------

#can = tk.Canvas(f4, height=100, width=100)
#can.grid(column=5, row=9)


options = [" ", "m", "u", "n", "p"]
n = ttk.Combobox(f4, values=options, font=("Arial", 14))
n.set("u")
n.grid(row=1, column=3)
n2 = ttk.Combobox(f4, values=options, font=("Arial", 14))
n2.set("p")
n2.grid(row=4, column=3)
l1 = tk.Label(f4, text="Inductance Value)", font=("Arial", 14))
l1.grid(row=0, column=2)
l = tk.Entry(f4, bg="yellow", font=("Arial", 14))
l.grid(row=1, column=2)
c1 = tk.Label(f4, text="Capcitance Value", font=("Arial", 14))
c1.grid(row=3, column=2)
c = tk.Entry(f4, bg="light blue", font=("Arial", 14))
c.grid(row=4, column=2)
zz = tk.Label(f4, text="               ")
zz.grid(row=0,column=0)
unitlabel_l = tk.Label(f4, text="Heneries", font=("Arial Black", 10))
unitlabel_l.grid(row=1, column=4)
unitlabel_c = tk.Label(f4, text="Farads", font=("Arial Black", 10))
unitlabel_c.grid(row=4, column=4)
eq = tk.Label(f4, text=" Equation Resonant Frequency is 1 /  2pi x SQRT LxC", font=("Arial", 10))
eq.grid(row=1, column=6)
calc_button = tk.Button(f4, text='Calculate>>', bg="orange", font=("Arial Black", 12), command = lambda: combo_calc(l.get(), c.get(), n.get(), n2.get()))
calc_button.grid(row=5, column=5)
lb5 = tk.Listbox(f4)
lb5.grid(row=16,  column=4)
def combo_calc(l, c, n, n2, *args):
    # Testing the passing arguements with print statements
    print(l, c, n, n2)
    # conditions below to adjust entry by converting string to interger and divide
    # by the value assoicated by the text from the combobox.
    # Could not convert the string to float, this failed.
    # It appears to must conver string to interger then to float.
    # This is why there is so much extra math done.

    if n == " ":
        a2 = c
        a = l

    elif n == "m":

        a = str(int(l)  / 1000)

    elif n == "u":

        a = str(int(l)  / 1000000)

    elif n == "n":

        a = str(int(l) / 1000000000)

    elif n == "p":

        a = str(int(l) / 1000000000000)



    if n2 == " ":

        a2 = str(int(c) * 1)

    elif n2 == "m":

        a2 = str(int(c) / 1000)

    elif n2 == "u":

        a2 = str(int(c) / 1000000)

    elif n2 == "n":

        a2 = str(int(c) / 1000000000)

    elif n2 == "p":

        a2 = str(int(c) / 1000000000000)

    else:
        contnue
        
    print (a)



    print(a2)

    na = a

    na2 = a2

    ttrl = tk.Label(f4, text="Engineering Notation Set", font=("Arial Black", 8))

    ttrl.grid(row=2, column=7)



    na = tk.Label(f4, text=na, font=("Arial Black", 8))

    na.grid(row=3, column=7)

    print(a, a2)
    lb5.insert(1, a)
    lb5.insert(2, a2)
    na2 = tk.Label(f4, text=na2, font=("Arial Black", 8))

    na2.grid(row=4 ,column=7)

    llcc = float(a) * float(a2)
    qq2 = math.sqrt(llcc)
    pi2 = math.pi * 2

    invfreq = math.sqrt(llcc) * pi2

    print(pi2)

    freq = 1 / float(invfreq)

    print(freq)
    lb5.insert(3, freq)
    l_reactance = pi2 * freq * float(a)
    c_reactance = 1 / (pi2 * freq * float(a2))
    l_admittance = 1 / l_reactance
    c_admittance = 1 / c_reactance
    kHz = freq / 1000
    Mhz = kHz / 1000
    a8 = kHz
    a10 = Mhz
    a4 = freq
    a4 = Label(f4, text=freq, font=("Arial Black", 12))
    a4.grid(row=11, column=2)
    a6 = Label(f4, text="Hz", font=("Arial Black", 12))
    a6.grid(row=11, column=3)
    a8 = Label(f4, text=kHz, font=("Arial Black", 12))
    a8.grid(row=12, column=2)
    a9 = Label(f4, text="kHz", font=("Arial Black", 12))
    a9.grid(row=12, column=3)
    a10 = Label(f4, text=Mhz, font=("Arial Black", 12))
    a10.grid(row=13, column=2)
    a11 = Label(f4, text="MHz", font=("Arial Black", 12))
    a11.grid(row=13, column=3)
    a12 = Label(f4, text=l_reactance, font=("Arial", 10))
    a12.grid(row=9,column=7)
    a13 = Label(f4, text=" LC Reactance Impedance in OHMS", font=("Arial", 10))
    a13.grid(row=9,column=7)
    a14 = Label(f4, text=c_reactance, font=("Arial", 10))
    a14.grid(row=10,column=7)
    
    a17 = Label(f4, text="Admittance Values for XL & XC", font=("Arial", 10))
    a17.grid(row=13 ,column=7)
    a18 = Label(f4, text=l_admittance, font=("Arial", 10))
    a18.grid(row=14 ,column=7)
    a19 = Label(f4, text=c_admittance, font=("Arial", 10))
    a19.grid(row=15 ,column=7)

    # Goal is top present every caculation answer for future math apps
    
    lb5.insert(4, kHz)
    lb5.insert(5, Mhz)
    lb5.insert(6, l_reactance)
    lb5.insert(7, c_reactance)
    lb5.insert(8, l_admittance)
    lb5.insert(9, c_admittance)
    lb5.insert(10, invfreq)
              
    return

# --- functions ---
#---GUI for adding two resistors in parallel and in series
# Future project with be with 3 or more resistors
# Would also like to make a reverse calculation which give parallel resistor for ohm value desired
def generate():
    try:
        r1 = num111.get()
        r2 = num222.get()
        vv1 = vvv1.get()
        con1 = 1 / float(r1) # seems to work better if done in steps
        con2 = 1 / float(r2) # con is for conductance
        consum = float(con1) + float(con2)       
        num333 = 1/float(consum)
        num444 = float(r1) + float(r2) #using float is obvious way
        result3 = float(r2) / float(num444)
        I2 = float(vv1) / float(num444)
        vdiv1 = float(I2) * float(r1)
        vdiv11 = float(I2) * float(r2)
        pwr1 = float(I2) * float(vv1)
        lb7.insert(1, r1)
        lb7.insert(2, r2)
        lb7.insert(3, vv1)
        lb7.insert(4, con1)
        lb7.insert(5, con2)
        lb7.insert(6, consum)
        lb7.insert(7, num333)
        lb7.insert(8, num444)
        lb7.insert(9, result3)
        lb7.insert(10, I2)
        lb7.insert(11, vdiv1)
        lb7.insert(12, vdiv11)
        lb7.insert(13, pwr1)
        lb9.insert(1, "R1")
        lb9.insert(2, "R2")
        lb9.insert(3, "Vin")
        lb9.insert(4, "1/R1")
        lb9.insert(5, "1/R2")
        lb9.insert(6, "1/R +1/R2")
        lb9.insert(7, "RT Parallel")
        lb9.insert(8, "Series R1 + R2")
        lb9.insert(9, "R2 / R1 + R2")
        lb9.insert(10, "I2 Vin / Rt Series")
        lb9.insert(11, "VR1")
        lb9.insert(12, "VR2")
        lb9.insert(13, "Power")
    except Exception as ex: 
        print(ex)
        result = 'error'
                   
                
def gen2():
    try:
        r01 = num1234.get()
        r02 = num4567.get()
        r03 = num7891.get()
        r04 = num1112.get() 
        vv2 = vvv2.get()        
        ccon1 = 1 / float(r01) # seems to work better if done in steps
        ccon2 = 1 / float(r02) # con is for conductance
        ccon3 = 1 / float(r03) # con is for conductance
        ccon4 = 1 / float(r04) # con is for conductance
        num333 = float(ccon1) + float(ccon2) + float(ccon3) + float(ccon4)     
        num444 = 1 / float(num333)
        rtotal2 = float(r01) + float(r02) + float(r03) + float(r04)
        numout44 = float(rtotal2)
        I4 = float(vv2) / float(numout44)
        num9999 = float(I4) * float(r01)
        num8888 = float(I4) * float(r02)
        num7777 = float(I4) * float(r03)         
        num6666 = float(I4) * float(r04)
        pwr2 = float(I4) * float(vv2)
        lb8.insert(1, r01)
        lb8.insert(2, r02)
        lb8.insert(3, r03)
        lb8.insert(4, r04)
        lb8.insert(5, vv2)
        lb8.insert(6, ccon1)
        lb8.insert(7, ccon2)
        lb8.insert(8, ccon3)
        lb8.insert(9, ccon4)
        lb8.insert(10, num333)
        lb8.insert(11, num444)
        lb8.insert(12, rtotal2)
        lb8.insert(13, I4)
        lb8.insert(14, num9999)
        lb8.insert(15, num8888)
        lb8.insert(16, num7777)
        lb8.insert(17, num6666)
        lb8.insert(18, pwr2)
       
       

        lb10.insert(1, "R1")
        lb10.insert(2, "R2")
        lb10.insert(3, "R3")
        lb10.insert(4, "R4")
        lb10.insert(5, "Vin")
        lb10.insert(6, "1/R1")
        lb10.insert(7, "1/R2")
        lb10.insert(8, "1/R3")
        lb10.insert(9, "1/R4")
        lb10.insert(10, "SUM INV R1-R4")
        lb10.insert(11, "RT Parallel")
        lb10.insert(12, "RT series")
        lb10.insert(13, "Current")
        lb10.insert(14, "VR1")
        lb10.insert(15, "VR2")
        lb10.insert(16, "VR3")
        lb10.insert(17, "VR4")
        lb10.insert(18, "Power")
        
        
                   
    except Exception as ex: 
        print(ex)
        result = 'error'
def clearlist1():
    lb7.delete(0, END)
    lb9.delete(0, END)
def clearlist2():
    lb8.delete(0, END)
    lb10.delete(0, END)

# --- main ---
num111 = tk.StringVar()
num222 = tk.StringVar()
num333 = tk.StringVar()
num444 = tk.StringVar()
numout33 = tk.StringVar()
numout44 = tk.StringVar()
vvv1 = tk.StringVar()
vdiv1 = tk.StringVar()
tk.Label(f5, text=" Input R1:").grid(row=0, column=0)
tk.Label(f5, text="Input R2:").grid(row=1, column=0)
tk.Label(f5, text="Vin for Vdiv").grid(row=2, column=0)
tk.Entry(f5, textvariable=num111, bg="yellow").grid(row=0, column=1)
tk.Entry(f5, textvariable=num222, bg="yellow").grid(row=1, column=1)

tk.Entry(f5, textvariable=vvv1, bg="yellow").grid(row=2, column=1)
lb7 = tk.Listbox(f5, height=20)
lb7.grid(row=6,  column=2)
lb9 = tk.Listbox(f5, height=20)
lb9.grid(row=6,  column=1)
b1 = tk.Button(f5, text="Calculate", command=generate)
b1.grid(row=6, column=0)
b3 = tk.Button(f5, text="Clear", command=clearlist1)
b3.grid(row=7, column=0)
num1234 = tk.StringVar()
num4567 = tk.StringVar()
num7891 = tk.StringVar()
num1112 = tk.StringVar()
vvv2 = tk.StringVar()
num9999 = tk.StringVar()
num8888 = tk.StringVar()
num7777 = tk.StringVar()
num6666= tk.StringVar()

vdiv2 = tk.StringVar()
tk.Label(f5, text=" Input R1:").grid(row=0, column=4)
tk.Label(f5, text="Input R2:").grid(row=1, column=4)
tk.Label(f5, text="Input R3:").grid(row=2, column=4)
tk.Label(f5, text="Input R4").grid(row=3, column=4)
tk.Label(f5, text="Vin").grid(row=4, column=4)
tk.Entry(f5, textvariable=num1234, bg="yellow").grid(row=0, column=5)
tk.Entry(f5, textvariable=num4567, bg="yellow").grid(row=1, column=5)
tk.Entry(f5, textvariable=num7891, bg="yellow").grid(row=2, column=5)
tk.Entry(f5, textvariable=num1112, bg="yellow").grid(row=3, column=5)
tk.Entry(f5, textvariable=vvv2, bg="yellow").grid(row=4, column=5)
lb8 = tk.Listbox(f5, height=20)
lb8.grid(row=6,  column=7)
lb10 = tk.Listbox(f5, height=20)
lb10.grid(row=6,  column=6)
b2 = tk.Button(f5, text="Calculate 4 Resistor", command=gen2)
b2.grid(row=6, column=5)
b4 = tk.Button(f5, text="Clear", command=clearlist2)
b4.grid(row=7, column=5)


if __name__ == '__main__':
    r.mainloop()

