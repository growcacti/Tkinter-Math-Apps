import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
import tkinter.font
import math
import subprocess
import os

from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
 
 
r = tk.Tk()
r.geometry('1200x800')
r.title("Electro PY Engineering Math App")
notebook = ttk.Notebook(r)
f0 = ttk.Frame(notebook)
notebook.grid(row=0, column=0)
def titlepage():
    t_str=""" Electro Py Engineering Caculation Program """
notebook.add(f0, text="MAIN")
f1 = ttk.Frame(notebook)
notebook.add(f1, text='Ohms Law')
def fontfamily():
    pass
def foo():
    pass
def codeview():
    import codeview
     
#------------------------------------------------
# TAB1 & 2 create
#------------------------------------------------
f2 = ttk.Frame(notebook)

notebook.add(f2, text='Sci_Calc')
def lc():
    import scicalc
    
def keypad():
    import keypad

#--------------------------------------------------------
# TAB 3 - 10 Create
#---------------------------------------------------------
f3 = ttk.Frame(notebook, height=100, width=200)
notebook.add(f3, text='Base # Converter')
f4 = ttk.Frame(notebook, height=100, width=100)
notebook.add(f4, text='Resonant Freq Calc')

f5 = ttk.Frame(notebook)
notebook.add(f5, text='Resistor Calc')
f6 = ttk.Frame(notebook)
notebook.add(f6, text='dBm2W&V')
f7 = ttk.Frame(notebook)
notebook.add(f7, text='7')
f8 = ttk.Frame(notebook)
notebook.add(f8, text='8')
f9 = ttk.Frame(notebook)
notebook.add(f9, text='9')
f10 = ttk.Frame(notebook)
notebook.add(f10, text='10')

f11 = ttk.Frame(notebook)
notebook.add(f11, text='11')

def command():
    pass
def mod1():
    import Ohms_Law_Singlecalc_v2
def mod2():
    import RPcalc

def mod3():
    import IPcalc

def mod4():
    import VPcalc
  
def lc_freq():
    import LC_Freq
btn1=tk.Button(f1, text='Ohms Law Calc', command=mod1).grid(column=0, row=3)
btn2=tk.Button(f1, text='Calc Resistance & Pwr', command=mod2).grid(column=0, row=4)
btn3=tk.Button(f1, text='Calc Current & Pwr', command=mod3).grid(column=0, row=5)
btn4=tk.Button(f1, text='Volts & Pwr', command=mod4).grid(column=0, row=6)
btn5=tk.Button(f1, text='b5', command=command).grid(column=0, row=7)
btn6=tk.Button(f1, text='b6', command=command).grid(column=0, row=8)
awg_str ="""  """
#--------------------------------------
#   TAB2 STUFF Sci Calc Eng, Info Label  
#--------------------------------------
f2btn = tk.Button(f2, text="load calculator", bg="pink" , command=lc)
f2btn.grid(row=2, column=2)
f3btn = tk.Button(f2, text="keyboard onscreen", bg="pink" , command=keypad)
f3btn.grid(row=3, column=2)

##txt_str= """''tera'   : (1000000000000, 10**12),
##'giga'   : (1000000000, 10**9),
##'mega'   : (1000000, 10**6),
##'kilo'   : (1000, 10**3),
##'hecta'  : (100, 10**2),
##'deca'   : (10, 10),
##'base'   : (1,1),
##'deci'   : (0.1, 10**-1),
##'centi'  : (0.01, 10**-2),
##'milli'  : (0.001, 10**-3),
##'micro'  : (0.000001, 10**-6),
##'nano'   : (0.000000001, 10**-9)
##'pico'   : (0.000000000001, 10**-12)
##
##"""
##tk.Label(f2, text=txt_str).grid(row=3, column=3)
#
#----------------------------------------------
#  TAB3  Number Base Converter
#----------------------------------------------

def bin2dec():
    import FBIN
    #subprocess.run("python3", "FBIN") 
def fromhex():
    import FHEX
def fromoct():
    import FOCT
def frombase():
    import DEC_2_36
def dectobin():
    import Dec2Bin
def infosec():
    import Info_Section
        
btn11=tk.Button(f3, text='Decimal to Base 2 to 36', command=frombase).grid(column=3, row=3)
btn22=tk.Button(f3, text='HEX to DEC BIN OCT', command=fromhex).grid(column=3, row=4)
btn33=tk.Button(f3, text='OCTAL TO DEC, HEX, BIN', command=fromoct).grid(column=3, row=5)
btn44=tk.Button(f3, text='BIN TO OCT, DEC, HEX', command=bin2dec).grid(column=3, row=6)
btn55=tk.Button(f3, text='DEC to BIN', command=dectobin).grid(column=3, row=7)
btn66=tk.Button(f3, text='INFO', command=infosec).grid(column=3, row=8)
tk.Label(f3, text="Base Converter").grid(column=3, row=1)


#--------------------------------------
#   TAB4 Resonant Frequency Calc
#--------------------------------------
def lc_freq():
    import LC_Freq

def lfreq():
    import Freq_L_find_C

def cfreq():
    import Freq_C_find_L

btn77 = tk.Button(f4, text="LC Resonant Freq Calc", command=lc_freq).grid(column=3, row=3)
btn78 = tk.Button(f4, text="Freq L Calc find C", command=lfreq).grid(column=3, row=4)
btn79 = tk.Button(f4, text="Freq C Calc find L", command=cfreq).grid(column=3, row=5)

if __name__ == '__main__':
    r.mainloop()


