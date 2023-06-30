import tkinter as tk
from tkinter import ttk
import math

class ElectroPYApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('1200x800')
        self.root.title("Electro PY JH APPS")
        self.notebook = ttk.Notebook(self.root)
        self.notebook.grid(row=0, column=0)
        
        self.create_main_tab()
        self.create_resonant_freq_tab()
        self.create_resistor_tab()
        self.create_dBm2WV_tab()
        self.create_sci_calc_tab()
        self.create_tab8()
        self.create_tab9()
        self.create_tab10()
        self.create_tab11()
        self.create_tab12()
        self.create_tab13()
        self.create_tab14()
    def create_main_tab(self):
        self.f0 = ttk.Frame(self.notebook)
       
        self.notebook.add(self.f0, text="MAIN")
        self.f1= ttk.Frame(self.notebook)
        self.notebook.add(self.f1, text="Ohms Law")
        self.ohms = Ohms_Law(self.f1)
        tk.Label(self.f0, text="              ", font=("Arial", 14)).grid(row=2, column=0)
        tk.Label(self.f0, text="              ", font=("Arial", 14)).grid(row=1, column=0)
        tk.Label(self.f0, text="              ", font=("Arial", 14)).grid(row=3, column=0)
        
        tk.Label(self.f0, text="Electro PY Notebook Math App", bg="light blue", font=("Arial Black", 16)).grid(row=0, column=5)
        tk.Label(self.f0, text="JH APPS", bg="light blue", font=("Arial", 16)).grid(row=1, column=5)
        tk.Label(self.f0, text=" Various Tabs have different engineering calculators", bg="light green", font=("Arial", 14)).grid(row=3, column=5)
        
        tkbtn1 = tk.Button(self.f0, text='-')
        tkbtn1.grid(column=5, row=5)
        tkbtn2 = tk.Button(self.f0, text='-')
        tkbtn2.grid(column=5, row=6)
        tkbtn3 = tk.Button(self.f0, text='--')
        tkbtn3.grid(column=5, row=7)
        tkbtn4 = tk.Button(self.f0, text='-')
        tkbtn4.grid(column=5, row=8)
        self.f4 = ttk.Frame(self.notebook,width=400,height=200)
        self.notebook.add(self.f4, text='Resonant Freq Calc')
    def create_resonant_freq_tab(self):
        options = [" ", "m", "u", "n", "p"]
        self.n = ttk.Combobox(self.f4, values=options, font=("Arial", 14))
        self.n.set("u")
        self.n.grid(row=1, column=3)
        self.n2 = ttk.Combobox(self.f4, values=options, font=("Arial", 14))
        self.n2.set("p")
        self.n2.grid(row=4, column=3)
        
        tk.Label(self.f4, text="Inductance Value)", font=("Arial", 14)).grid(row=0, column=2)
        tk.Label(self.f4, text="Capacitance Value", font=("Arial", 14)).grid(row=3, column=2)
        
        self.l = tk.Entry(self.f4, bg="yellow", font=("Arial", 14))
        self.l.grid(row=1, column=2)
        self.c = tk.Entry(self.f4, bg="light blue", font=("Arial", 14))
        self.c.grid(row=4, column=2)
        
        tk.Label(self.f4, text="               ").grid(row=0, column=0)
        tk.Label(self.f4, text="Heneries", font=("Arial Black", 10)).grid(row=1, column=4)
        tk.Label(self.f4, text="Farads", font=("Arial Black", 10)).grid(row=4, column=4)
        
        tk.Label(self.f4, text=" Equation Resonant Frequency is 1 /  2pi x SQRT LxC", font=("Arial", 10)).grid(row=1, column=6)
        
        calc_button = tk.Button(self.f4, text='Calculate>>', bg="orange", font=("Arial Black", 12), command=self.combo_calc)
        calc_button.grid(row=5, column=5)
        
        self.lb5 = tk.Listbox(self.f4,width=50,height=40)
        self.lb5.grid(row=16, column=4)
        
    def combo_calc(self):
        try:
            l = float(self.l.get())
            c = float(self.c.get())
            n = self.n.get()
            n2 = self.n2.get()
            
            if n == " ":
                a2 = c
                a = l
            elif n == "m":
                a = l / 1000
            elif n == "u":
                a = l / 1000000
            elif n == "n":
                a = l / 1000000000
            elif n == "p":
                a = l / 1000000000000
                
            if n2 == " ":
                a2 = c
            elif n2 == "m":
                a2 = c / 1000
            elif n2 == "u":
                a2 = c / 1000000
            elif n2 == "n":
                a2 = c / 1000000000
            elif n2 == "p":
                a2 = c / 1000000000000

            na = a
            na2 = a2

            self.na_label = tk.Label(self.f4, text=na, font=("Arial Black", 8))
            self.na_label.grid(row=3, column=7)

            self.na2_label = tk.Label(self.f4, text=na2, font=("Arial Black", 8))
            self.na2_label.grid(row=4, column=7)

            llcc = a * a2
            qq2 = math.sqrt(llcc)
            pi2 = math.pi * 2
            invfreq = math.sqrt(llcc) * pi2
            freq = 1 / invfreq
            l_reactance = pi2 * freq * a
            c_reactance = 1 / (pi2 * freq * a2)
            l_admittance = 1 / l_reactance
            c_admittance = 1 / c_reactance
            kHz = freq / 1000
            Mhz = kHz / 1000
            
            self.freq_label = tk.Label(self.f4, text=freq, font=("Arial Black", 12))
            self.freq_label.grid(row=11, column=2)
            self.freq_unit_label = tk.Label(self.f4, text="Hz", font=("Arial Black", 12))
            self.freq_unit_label.grid(row=11, column=3)
            
            self.khz_label = tk.Label(self.f4, text=kHz, font=("Arial Black", 12))
            self.khz_label.grid(row=12, column=2)
            self.khz_unit_label = tk.Label(self.f4, text="kHz", font=("Arial Black", 12))
            self.khz_unit_label.grid(row=12, column=3)
            
            self.mhz_label = tk.Label(self.f4, text=Mhz, font=("Arial Black", 12))
            self.mhz_label.grid(row=13, column=2)
            self.mhz_unit_label = tk.Label(self.f4, text="MHz", font=("Arial Black", 12))
            self.mhz_unit_label.grid(row=13, column=3)
            
            
            
            self.lb5.insert(0, "Resonant Frequency (Hz):")
            self.lb5.insert(1, freq)
            self.lb5.insert(2, "Resonant Frequency (kHz):")
            self.lb5.insert(3, kHz)
            self.lb5.insert(4, "Resonant Frequency (MHz):")
            self.lb5.insert(5, Mhz)
            self.lb5.insert(6, "Inductance Reactance (Ohms):")
            self.lb5.insert(7, l_reactance)
            self.lb5.insert(8, "Capacitance Reactance (Ohms):")
            self.lb5.insert(9, c_reactance)
            self.lb5.insert(10, "Inductance Admittance(siemens):")
            self.lb5.insert(11, l_admittance)
            self.lb5.insert(12, "Capacitance Admittance(siemens):")
            self.lb5.insert(13, c_admittance)
            
            
        except Exception as ex:
            print(ex)
            result = 'error'
    
    def create_resistor_tab(self):
        self.f5 = ttk.Frame(self.notebook)
        self.notebook.add(self.f5, text='Resistor Calc')
        vdivider = Vdiv(self.f5)
        
        # Rest of the code for the resistor calculator tab
        
    def create_dBm2WV_tab(self):
        self.f6 = ttk.Frame(self.notebook)
        self.notebook.add(self.f6, text='dBm2W&V')
        self.dBm =dBm2Watts(self.f6)
      
        # Rest of the code for the dBm to W & V calculator tab
        
    def create_sci_calc_tab(self):
        f7 = ttk.Frame(self.notebook)
        self.notebook.add(f7, text='scicalc')
        
        # Rest of the code for the scientific calculator tab
    def create_tab8(self):
        self.f8 = ttk.Frame(self.notebook)
        self.notebook.add(self.f8, text='---')
    def create_tab9(self):
        self.f9 = ttk.Frame(self.notebook)
        self.notebook.add(self.f9, text='---')
    def create_tab10(self):
        self.f10 = ttk.Frame(self.notebook)
        self.notebook.add(self.f10, text='---')

    def create_tab11(self):
        self.f11 = ttk.Frame(self.notebook)
        self.notebook.add(self.f11, text='---')

    def create_tab12(self):
        self.f12 = ttk.Frame(self.notebook)
        self.notebook.add(self.f12, text='---')


    def create_tab13(self):
        self.f13 = ttk.Frame(self.notebook)
        self.notebook.add(self.f13, text='---')


    def create_tab14(self):
        self.f14 = ttk.Frame(self.notebook)
        self.notebook.add(self.f14, text='---')


    def create_tab15(self):
        self.f15 = ttk.Frame(self.notebook)
        self.notebook.add(self.f15, text='---')

          
class Ohms_Law:
    def __init__(self, f1):
        self.f1 = f1
        self.n1 = 1
        self.n2 =1
        self.n3 =1
        self.n4 =1
        self.x = tk.StringVar()
        self.y = tk.StringVar()
        self.options1 = ["Volts ", "Watts", "Amps"]
        self.options2 = ["Amps", "Ohms", "Volts"]
        self.n = ttk.Combobox(self.f1, values=self.options1, font=("Arial", 8))
        self.n.set("Volts")
        self.n.grid(row=1, column=2)
        self.n2 = ttk.Combobox(self.f1, values=self.options2, font=("Arial", 8))
        self.n2.set("Ohms")
        self.n2.grid(row=2, column=2)
        self.x = tk.Entry(self.f1, bg="yellow", font=("Arial", 8))
        self.x.grid(row=1, column=1)
        self.y = tk.Entry(self.f1, bg="yellow", font=("Arial", 8))
        self.y.grid(row=2, column=1)
        self.btn1 = tk.Button(self.f1, text="calculate", bg = 'cyan', font=("Arial", 8), command=self.operations)
        self.btn1.grid(row=3, column=1)
        self.btn2 = tk.Button(self.f1, text="Clear Answers", bg = 'light green', font=("Arial", 8), command=self.clearlist1)
        self.btn2.grid(row=3, column=0)

        self.lboxx1 = tk.Listbox(self.f1)
        self.lboxx1.grid(row=4, column=1)
        self.lboxx2 = tk.Listbox(self.f1)
        self.lboxx2.grid(row=4, column=2)
        self.str1 = ""
        self.str2 = ""
      
    def clearlist1(self):
        self.lboxx1.delete(0, END)
        self.lboxx2.delete(0, END)


   
       
    def operations(self):   
        self.num1 = float(self.x.get())
        self.num2 = float(self.y.get())
        self.cb1 = self.n.get()
        self.cb2 = self.n2.get()
        if self.cb1 == "Volts" and self.cb2 == "Amps":
           
            self.num3 = float(self.num1) / float(self.num2)
            self.num4 = float(self.num1) * float(self.num2)
            self.str1 =  "Ohms"
            self.str2 = "Watts"
        elif self.cb1 == "Volts" and self.cb2 == "Ohms":
             self.num3 = float(self.num1) / float(self.num2)
             self.num4 = float(self.num1) * float(self.num1) / float(self.num2)
             self.str1 = "Amps"
             self.str2 = "Watts"
        elif self.cb1 == "Volts" and self.cb2 == "Watts":
             self.num3 = float(self.num1) * float(self.num1) / float(self.num2)
             self.str1 = "Ohms"
             self.num4 = float(self.num2) / float(self.num1)
             self.str2 = "Amps"
        elif self.cb1 == "Amps" and self.cb2 == "Ohms":
             self.num3 = float(self.num1) * float(self.num2)
             self.str1 = "Volts"
             self.num4 = float(self.num1) * float(self.num1) / float(self.num2)
             self.str2 = "Watts"
        elif self.cb1 == "Watts" and self.cb2 == "Amps":
             self.num3 = float(self.num1) / float(self.num2) ** 2
             self.str1 = "Ohms"
             self.num4 = float(self.num1) / float(self.num2)
             self.str = "Volts"
        elif self.cb1 == "Watts" and self.cb2 == "Volts":
             self.num3 = float(self.num1) * float(self.num1) / float(self.num2)
             self.str1 = "Ohms"
             self.num4 = float(self.num2) / float(self.num1)
        elif self.cb1 == "Watts" and self.cb2 == "Ohms":
             self.num3 = math.sqrt(float(self.num1) / float(self.num2))
             self.str1 = "Amps"
             self.num4 =  math.sqrt(float(self.num1) * float(self.num2))
             self.str2 ="Volts"
        elif self.cb1 == "Amps" and self.cb2 == "Watts":
             self.num3 = float(self.num2) / float(self.num1) ** 2
             self.str1 = "Ohms"
             self.num4 = float(self.num2) / float(self.num1)
             self.str = "Volts"
        elif self.cb1 == "Amps" and self.cb2 == "Amps":
             self.num3 = 1
             self.str1 = "Amps"
             self.num4 = 1
             self.str2 = "Amps"
 
        elif self.cb1 == "Volts" and self.cb2 == "Volts":
             self.num3 = 1
             self.str1 = "Volts"
             self.num4 = 1
             self.str2 = "Volts"

        elif self.cb1 == "Amps" and self.cb2 == "Volts":
             self.num3 = float(self.num1) / float(self.num2)
             self.num4 = float(self.num1) * float(self.num2)
             self.str1 =  "Ohms"
             self.str2 = "Watts"
        else:
             self.num3 = self.num4

     
        self.lboxx1.insert(1, self.num3)
        self.lboxx1.insert(2, self.num4)
        self.lboxx2.insert(1, self.str1)
        self.lboxx2.insert(2, self.str2)
    

class dBm2Watts:
    def __init__(self, f6):
        self.f6 = f6
        self.num1 = tk.StringVar()
        self.lbox1 = tk.Listbox(self.f6)
        self.lbox2 = tk.Listbox(self.f6)
        
        self.create_widgets()
        
    def create_widgets(self):
      
        
        e3 = tk.Entry(self.f6, textvariable=self.num1, bg="yellow", justify="right", font=("Arial", 8))
        e3.grid(row=0, column=2)
        e3.focus()
        
        tk.Label(self.f6, text="dBm                              ", justify="left", font=("Arial", 8)).grid(row=0, column=3)
        
        btn2 = tk.Button(self.f6, text="Convert", command=self.dBmtoW)
        btn2.grid(column=1, row=1)
        
        btn3 = tk.Button(self.f6, text="Clear", command=self.clear_lbox1)
        btn3.grid(row=7, column=1)
        
        self.lbox1.grid(column=2, row=3)
        self.lbox2.grid(column=3, row=3)
        
      
        
                
      
        
    def dBmtoW(self):
        num11 = self.num1.get()
        num_222 = float(num11) / 20
        num_444 = 10 ** float(num_222)
        num_111 = float(num11) / 10
        num2 = 10 ** float(num_111)
        num3 = float(num2) / 1000
        num4 = float(num_444) * 0.2236
        num5 = float(num4) * 1.414
        num6 = float(num5) * 2
        
        self.lbox1.insert(1, num11)
        self.lbox1.insert(2, num2)
        self.lbox1.insert(3, num3)
        self.lbox1.insert(4, num4)
        self.lbox1.insert(5, num5)
        self.lbox1.insert(6, num6)
        
        self.lbox2.insert(1, "dBm")
        self.lbox2.insert(2, "mW")
        self.lbox2.insert(3, "W")
        self.lbox2.insert(4, "Volts RMS")
        self.lbox2.insert(5, "Volts Peak")
        self.lbox2.insert(6, "Volts PK-PK")
        
    def clear_lbox1(self):
        self.lbox1.delete(0, tk.END)
        self.lbox2.delete(0, tk.END)
        
class Vdiv:
    def __init__(self, f5):
        self.f5 = f5
        tk.Label(self.f5,text="Resistor Calculator").grid(row=0, column=0)
        
        self.num111 = tk.StringVar()
        self.num222 = tk.StringVar()
        self.vvv1 = tk.StringVar()
        self.lb7 = tk.Listbox(self.f5, height=20)
        self.lb9 = tk.Listbox(self.f5, height=20)
        
        self.create_widgets1()
        
        self.num1234 = tk.StringVar()
        self.num4567 = tk.StringVar()
        self.num7891 = tk.StringVar()
        self.num1112 = tk.StringVar()
        self.vvv2 = tk.StringVar()
        self.lb8 = tk.Listbox(self.f5, height=20)
        self.lb10 = tk.Listbox(self.f5, height=20)
        
        self.create_widgets2()
        
    def create_widgets1(self):
      
        
        tk.Label(self.f5, text="Input R1:").grid(row=1, column=0)
        tk.Label(self.f5, text="Input R2:").grid(row=2, column=0)
        tk.Label(self.f5, text="Vin for Vdiv").grid(row=3, column=0)
        
        tk.Entry(self.f5, textvariable=self.num111, bg="yellow").grid(row=1, column=1)
        tk.Entry(self.f5, textvariable=self.num222, bg="yellow").grid(row=2, column=1)
        tk.Entry(self.f5, textvariable=self.vvv1, bg="yellow").grid(row=3, column=1)
        
        self.lb7.grid(row=6, column=2)
        self.lb9.grid(row=6, column=1)
        
        tk.Button(self.f5, text="Calculate", command=self.generate).grid(row=6, column=0)
        tk.Button(self.f5, text="Clear", command=self.clearlist1).grid(row=7, column=0)
        
    def create_widgets2(self):
       
        tk.Label(self.f5, text="Input R1:").grid(row=1, column=4)
        tk.Label(self.f5, text="Input R2:").grid(row=2, column=4)
        tk.Label(self.f5, text="Input R3:").grid(row=3, column=4)
        tk.Label(self.f5, text="Input R4").grid(row=4, column=4)
        tk.Label(self.f5, text="Vin").grid(row=5, column=4)
        
        tk.Entry(self.f5, textvariable=self.num1234, bg="yellow").grid(row=1, column=5)
        tk.Entry(self.f5, textvariable=self.num4567, bg="yellow").grid(row=2, column=5)
        tk.Entry(self.f5, textvariable=self.num7891, bg="yellow").grid(row=3, column=5)
        tk.Entry(self.f5, textvariable=self.num1112, bg="yellow").grid(row=4, column=5)
        tk.Entry(self.f5, textvariable=self.vvv2, bg="yellow").grid(row=5, column=5)
        
        self.lb8.grid(row=6, column=7)
        self.lb10.grid(row=6, column=6)
        
        tk.Button(self.f5, text="Calculate 4 Resistor", command=self.gen2).grid(row=6, column=5)
        tk.Button(self.f5, text="Clear", command=self.clearlist2).grid(row=7, column=5)
    def generate(self):
        try:
            r1 = self.num111.get()
            r2 = self.num222.get()
            vv1 = self.vvv1.get()
            con1 = 1 / float(r1)  # seems to work better if done in steps
            con2 = 1 / float(r2)  # con is for conductance
            consum = float(con1) + float(con2)
            num333 = 1 / float(consum)
            num444 = float(r1) + float(r2)  # using float is obvious way
            result3 = float(r2) / float(num444)
            I2 = float(vv1) / float(num444)
            vdiv1 = float(I2) * float(r1)
            vdiv11 = float(I2) * float(r2)
            pwr1 = float(I2) * float(vv1)
            self.lb7.insert(1, r1)
            self.lb7.insert(2, r2)
            self.lb7.insert(3, vv1)
            self.lb7.insert(4, con1)
            self.lb7.insert(5, con2)
            self.lb7.insert(6, consum)
            self.lb7.insert(7, num333)
            self.lb7.insert(8, num444)
            self.lb7.insert(9, result3)
            self.lb7.insert(10, I2)
            self.lb7.insert(11, vdiv1)
            self.lb7.insert(12, vdiv11)
            self.lb7.insert(13, pwr1)
            self.lb9.insert(1, "R1")
            self.lb9.insert(2, "R2")
            self.lb9.insert(3, "Vin")
            self.lb9.insert(4, "1/R1")
            self.lb9.insert(5, "1/R2")
            self.lb9.insert(6, "1/R +1/R2")
            self.lb9.insert(7, "RT Parallel")
            self.lb9.insert(8, "Series R1 + R2")
            self.lb9.insert(9, "R2 / R1 + R2")
            self.lb9.insert(10, "I2 Vin / Rt Series")
            self.lb9.insert(11, "VR1")
            self.lb9.insert(12, "VR2")
            self.lb9.insert(13, "Power")
        except Exception as ex:
            print(ex)
            result = "error"

    
    def gen2(self):
        try:
            r01 = self.num1234.get()
            r02 = self.num4567.get()
            r03 = self.num7891.get()
            r04 = self.num1112.get()
            vv2 = self.vvv2.get()
            ccon1 = 1 / float(r01)  # seems to work better if done in steps
            ccon2 = 1 / float(r02)  # con is for conductance
            ccon3 = 1 / float(r03)  # con is for conductance
            ccon4 = 1 / float(r04)  # con is for conductance
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
            self.lb8.insert(1, r01)
            self.lb8.insert(2, r02)
            self.lb8.insert(3, r03)
            self.lb8.insert(4, r04)
            self.lb8.insert(5, vv2)
            self.lb8.insert(6, ccon1)
            self.lb8.insert(7, ccon2)
            self.lb8.insert(8, ccon3)
            self.lb8.insert(9, ccon4)
            self.lb8.insert(10, num333)
            self.lb8.insert(11, num444)
            self.lb8.insert(12, rtotal2)
            self.lb8.insert(13, I4)
            self.lb8.insert(14, num9999)
            self.lb8.insert(15, num8888)
            self.lb8.insert(16, num7777)
            self.lb8.insert(17, num6666)
            self.lb8.insert(18, pwr2)

            self.lb10.insert(1, "R1")
            self.lb10.insert(2, "R2")
            self.lb10.insert(3, "R3")
            self.lb10.insert(4, "R4")
            self.lb10.insert(5, "Vin")
            self.lb10.insert(6, "1/R1")
            self.lb10.insert(7, "1/R2")
            self.lb10.insert(8, "1/R3")
            self.lb10.insert(9, "1/R4")
            self.lb10.insert(10, "SUM INV R1-R4")
            self.lb10.insert(11, "RT Parallel")
            self.lb10.insert(12, "RT series")
            self.lb10.insert(13, "Current")
            self.lb10.insert(14, "VR1")
            self.lb10.insert(15, "VR2")
            self.lb10.insert(16, "VR3")
            self.lb10.insert(17, "VR4")
            self.lb10.insert(18, "Power")

        except Exception as ex:
            print(ex)
            result = "error"

    def clearlist1(self):
        self.lb7.delete(0, tk.END)
        self.lb9.delete(0, tk.END)
        
    def clearlist2(self):
        self.lb8.delete(0, tk.END)
        self.lb10.delete(0, tk.END)

class Res_Freq_Cap:
    def __init__(self):
       
        
        self.options2 = [" ", "kHz", "Mhz", "GHz", "Tera"]
        self.options = ["", "milli", "micro", "nano", "pico"]
        
        self.n = ttk.Combobox(self.r, values=self.options, font=("Courier", 18))
        self.n.set("micro")
        self.n.grid(row=2, column=1)
        
        self.n2 = ttk.Combobox(self.r, values=self.options2, font=("Courier", 18))
        self.n2.set("pico")
        self.n2.grid(row=8, column=1)
        
        self.l1 = tk.Label(self.r, text="Inductance Value", font=("Courier", 18))
        self.l1.grid(row=0, column=0)
        self.l = tk.Entry(self.r, bg="orange", font=("Courier", 18))
        self.l.grid(row=2, column=0)
        
        self.freq = tk.Label(self.r, text="Frequency", font=("Courier", 18))
        self.freq.grid(row=6, column=0)
        self.freq = tk.Entry(self.r, bg="cyan", font=("Courier", 18))
        self.freq.grid(row=8, column=0)
        
        self.calc_button = tk.Button(
            self.r,
            text="Next>>",
            font=("Courier", 18),
            command=self.combo_calc,
        )
        self.calc_button.grid(row=9, column=1)
    
    def combo_calc(self):
        l = self.l.get()
        freq = self.freq.get()
        n = self.n.get()
        n2 = self.n2.get()
        
        p = tk.Tk()
        p.title("JH Resonance Calc")
        p.geometry("400x150")
        
        try:
            if n == "as_is":
                a = l
            elif n == "milli":
                a = str(int(l) / 1000)
            elif n == "micro":
                a = str(int(l) / 1000000)
            elif n == "nano":
                a = str(int(l) / 1000000000)
            elif n == "pico":
                a = str(int(l) / 1000000000000)
            
            if n2 == " ":
                a2 = str(int(freq) * 1)
            elif n2 == "kHz":
                a2 = str(int(freq) / 1000)
            elif n2 == "MHz":
                a2 = str(int(freq) / 1000000)
            elif n2 == "GHz":
                a2 = str(int(cfreq) / 1000000000)
            elif n2 == " null":
                a2 = str(int(freq) / 1000000000000)
            else:
                return float(a), float(a2)
        except Exception:
            n == 1
            n2 == 1
        
        na = a
        na2 = a2
        
        ttrl = tk.Label(p, text="Engineering Notation Set", font=("Courier", 18))
        ttrl.grid(row=4, column=0)
        
        cap = tk.Button(
            p,
            text="Calculate Cap",
            bg="light blue",
            command=self.freq_calc,
            font=("Courier", 12),
        )
        cap.grid(row=8, column=0)
        
        na = tk.Label(p, text=na, font=("Courier", 18))
        na.grid(row=6, column=0)
        
        na2 = tk.Label(p, text=na2, font=("Courier", 18))
        na2.grid(row=7, column=0)
        
        return na, na2, a, a2
    
    def freq_calc(self):
        r = tk.Tk()
        r.geometry("400x150")
        r.title("---Frequency  Final Answer---")
        
        llfreq = float(ll) * float(freq)
        pii4 = 4 * (math.pi * math.pi)
        print(pii4)
        cap = 1 / float(pii4) * float(llfreq)
        print(cap)
        
        a4 = tk.Label(r, text=freq, font=("Courier", 18))
        a4.grid(row=6, column=4)
        
        a6 = tk.Label(r, text="Hz", font=("Courier", 18))
        a6.grid(row=6, column=5)
        
        a8 = tk.Label(r, text=kHz, font=("Courier", 18))
        a8.grid(row=7, column=4)
        
        a9 = tk.Label(r, text="kHz", font=("Courier", 18))
        a9.grid(row=7, column=5)
        
        a10 = tk.Label(r, text=Mhz, font=("Courier", 18))
        a10.grid(row=9, column=4)
        
        a11 = tk.Label(r, text="MHz", font=("Courier", 18))
        a11.grid(row=9, column=5)
        
        return a4, freq    
class RC_calc:
    def __init__(self):
      
        
        self.options = ["T", "G", "M", "k", "h", "da", " ", "d", "c", "m", "u", "n", "p"]
        
        self.n = ttk.Combobox(self.r, values=self.options, font=("Arial", 14))
        self.n.set(" ")
        self.n.grid(row=1, column=3)
        
        self.n2 = ttk.Combobox(self.r, values=self.options, font=("Arial", 14))
        self.n2.set("u")
        self.n2.grid(row=4, column=3)
        
        self.l1 = tk.Label(self.r, text="Resistance OHMS", font=("Arial", 14))
        self.l1.grid(row=0, column=2)
        
        self.l = tk.Entry(self.r, bg="cyan", font=("Arial", 14))
        self.l.grid(row=1, column=2)
        
        self.c1 = tk.Label(self.r, text="Capacitance FARADS", font=("Arial", 14))
        self.c1.grid(row=3, column=2)
        
        self.c = tk.Entry(self.r, bg="pink", font=("Arial", 14))
        self.c.grid(row=4, column=2)
        
        self.zz = tk.Label(self.r, text="----")
        self.zz.grid(row=0, column=0)
        
        self.unitlabel_l = tk.Label(self.r, text="Unit Value", font=("Arial Black", 10))
        self.unitlabel_l.grid(row=1, column=4)
        
        self.unitlabel_c = tk.Label(self.r, text="Unit Value", font=("Arial Black", 10))
        self.unitlabel_c.grid(row=4, column=4)
        
        self.calc_button = tk.Button(
            self.r,
            text="Calculate>>",
            bg="orange",
            font=("Arial Black", 12),
            command=self.eunc,
        )
        self.calc_button.grid(row=7, column=3)
    
    def eunc(self):
        l = self.l.get()
        c = self.c.get()
        n = self.n.get()
        n2 = self.n2.get()
        
        try:
            num = int(l)
            num2 = int(c)
            print(num, num2)
        except ValueError as ex:
            print(ex)
        
        if n == "T":
            a = str(int(l) * 10e12)
        elif n == "G":
            a = str(int(l) * 10e9)
        elif n == "M":
            a = str(int(l) * 10e6)
        elif n == "k":
            a = str(int(l) * 1000)
        elif n == "h":
            a = str(int(l) * 100)
        elif n == "da":
            a = str(int(l) * 10)
        elif n == " ":
            a2 = c
            a = l
        elif n == "d":
            a = str(int(l) / 10)
        elif n == "c":
            a = str(int(l) / 100)
        elif n == "m":
            a = str(int(l) / 1000)
        elif n == "u":
            a = str       

if __name__ == '__main__':
    app = ElectroPYApp()
   
