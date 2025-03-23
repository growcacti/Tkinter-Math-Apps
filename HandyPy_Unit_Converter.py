import tkinter as tk
from tkinter import ttk

class UnitConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Converter")

        # Dictionaries for unit conversions
        self.length_units = {
            "millimeters": {"symbol": "mm", "conversions": {"centimeters": 0.1, "meters": 0.001, "kilometers": 0.000001, "inches": 0.03937, "feet": 0.003281, "yards": 0.001094, "miles": 6.21e-07}},
            "centimeters": {"symbol": "cm", "conversions": {"millimeters": 10, "meters": 0.01, "kilometers": 0.00001, "inches": 0.393701, "feet": 0.032808, "yards": 0.010936, "miles": 0.000006}},
            "meters": {"symbol": "m", "conversions": {"millimeters": 1000, "centimeters": 100, "kilometers": 0.001, "inches": 39.37008, "feet": 3.28084, "yards": 1.093613, "miles": 0.000621}},
            "kilometers": {"symbol": "km", "conversions": {"millimeters": 1_000_000, "centimeters": 100_000, "meters": 1000, "inches": 39370.08, "feet": 3280.84, "yards": 1093.613, "miles": 0.621371}},
            "inches": {"symbol": "in", "conversions": {"millimeters": 25.4, "centimeters": 2.54, "meters": 0.0254, "kilometers": 0.000025, "feet": 0.083333, "yards": 0.027778, "miles": 0.000016}},
            "feet": {"symbol": "ft", "conversions": {"millimeters": 304.8, "centimeters": 30.48, "meters": 0.3048, "kilometers": 0.000305, "inches": 12, "yards": 0.333333, "miles": 0.000189}},
            "yards": {"symbol": "yd", "conversions": {"millimeters": 914.4, "centimeters": 91.44, "meters": 0.9144, "kilometers": 0.000914, "inches": 36, "feet": 3, "miles": 0.000568}},
            "miles": {"symbol": "mi", "conversions": {"millimeters": 1_609_344, "centimeters": 160_934.4, "meters": 1609.344, "kilometers": 1.609344, "inches": 63360, "feet": 5280, "yards": 1760}},
        }

        self.area_units = {
            "millimeter_square": {"symbol": "mm2", "conversions": {"centimeter_square": 0.01, "meter_square": 0.000001, "inch_square": 0.00155, "foot_square": 0.000011, "yard_square": 0.000001}},
            "centimeter_square": {"symbol": "cm2", "conversions": {"millimeter_square": 100, "meter_square": 0.0001, "inch_square": 0.155, "foot_square": 0.001076, "yard_square": 0.00012}},
            "meter_square": {"symbol": "m2", "conversions": {"millimeter_square": 1_000_000, "centimeter_square": 10_000, "inch_square": 1550.003, "foot_square": 10.76391, "yard_square": 1.19599}},
            "inch_square": {"symbol": "in2", "conversions": {"millimeter_square": 645.16, "centimeter_square": 6.4516, "meter_square": 0.000645, "foot_square": 0.006944, "yard_square": 0.000772}},
            "foot_square": {"symbol": "ft2", "conversions": {"millimeter_square": 92903, "centimeter_square": 929.0304, "meter_square": 0.092903, "inch_square": 144, "yard_square": 0.111111}},
            "yard_square": {"symbol": "yd2", "conversions": {"millimeter_square": 836127, "centimeter_square": 8361.274, "meter_square": 0.836127, "inch_square": 1296, "foot_square": 9}},
        }

        self.volume_units = {
            "centimeter_cube": {"symbol": "cm3", "conversions": {"meter_cube": 0.000001, "liter": 0.001, "inch_cube": 0.061024, "foot_cube": 0.000035, "US_gallons": 0.000264, "Imperial_gallons": 0.00022, "US_barrel": 0.000006}},
            "meter_cube": {"symbol": "m3", "conversions": {"centimeter_cube": 1_000_000, "liter": 1000, "inch_cube": 61024, "foot_cube": 35, "US_gallons": 264, "Imperial_gallons": 220, "US_barrel": 6.29}},
            "liter": {"symbol": "ltr", "conversions": {"centimeter_cube": 1000, "meter_cube": 0.001, "inch_cube": 61, "foot_cube": 0.035, "US_gallons": 0.264201, "Imperial_gallons": 0.22, "US_barrel": 0.00629}},
            "inch_cube": {"symbol": "in3", "conversions": {"centimeter_cube": 16.4, "meter_cube": 0.000016, "liter": 0.016387, "foot_cube": 0.000579, "US_gallons": 0.004329, "Imperial_gallons": 0.003605, "US_barrel": 0.000103}},
            "foot_cube": {"symbol": "ft3", "conversions": {"centimeter_cube": 28317, "meter_cube": 0.028317, "liter": 28.31685, "inch_cube": 1728, "US_gallons": 7.481333, "Imperial_gallons": 6.229712, "US_barrel": 0.178127}},
            "US_gallons": {"symbol": "US_gal", "conversions": {"centimeter_cube": 3785, "meter_cube": 0.003785, "liter": 3.79, "inch_cube": 231, "foot_cube": 0.13, "Imperial_gallons": 1, "US_barrel": 0.832701}},
            "Imperial_gallons": {"symbol": "Imp_gal", "conversions": {"centimeter_cube": 4545, "meter_cube": 0.004545, "liter": 4.55, "inch_cube": 277, "foot_cube": 0.16, "US_gallons": 1.20, "US_barrel": 1}},
            "US_barrel": {"symbol": "US_brl", "conversions": {"centimeter_cube": 158970, "meter_cube": 0.15897, "liter": 159, "inch_cube": 9701, "foot_cube": 6, "US_gallons": 42, "Imperial_gallons": 35}},
        }

        self.mass_units = {
            "grams": {"symbol": "g", "conversions": {"kilograms": 0.001, "metric_tonnes": 0.000001, "short_ton": 0.000001, "long_ton": 9.84e-07, "pounds": 0.002205, "ounces": 0.035273}},
            "kilograms": {"symbol": "kg", "conversions": {"grams": 1000, "metric_tonnes": 0.001, "short_ton": 0.001102, "long_ton": 0.000984, "pounds": 2.204586, "ounces": 35.27337}},
            "metric_tonnes": {"symbol": "tonne", "conversions": {"grams": 1_000_000, "kilograms": 1000, "short_ton": 1.102293, "long_ton": 0.984252, "pounds": 2204.586, "ounces": 35273.37}},
            "short_ton": {"symbol": "shton", "conversions": {"grams": 907200, "kilograms": 907.2, "metric_tonnes": 0.9072, "long_ton": 1, "pounds": 2000, "ounces": 32000}},
            "long_ton": {"symbol": "Lton", "conversions": {"grams": 1016000, "kilograms": 1016, "metric_tonnes": 1.016, "short_ton": 1.119929, "pounds": 2239.859, "ounces": 35837.74}},
            "pounds": {"symbol": "lb", "conversions": {"grams": 453.6, "kilograms": 0.4536, "metric_tonnes": 0.000454, "short_ton": 0.0005, "long_ton": 0.000446, "ounces": 16}},
            "ounces": {"symbol": "oz", "conversions": {"grams": 28, "kilograms": 0.02835, "metric_tonnes": 0.000028, "short_ton": 0.000031, "long_ton": 0.000028, "pounds": 0.0625}},
        }

        self.normal_flow_units = {
            "normal_meter_cube_per_hour": {"symbol": "Nm3/hr", "conversions": {"standard_cubic_feet_per_hour": 35.31073, "standard_cubic_feet_per_minute": 0.588582}},
            "standard_cubic_feet_per_hour": {"symbol": "scfh", "conversions": {"normal_meter_cube_per_hour": 0.02832, "standard_cubic_feet_per_minute": 0.016669}},
            "standard_cubic_feet_per_minute": {"symbol": "scfm", "conversions": {"normal_meter_cube_per_hour": 1.699, "standard_cubic_feet_per_hour": 59.99294}},
        }

        self.mass_flow_units = {
            "kilogram_per_hour": {"symbol": "kg/h", "conversions": {"pound_per_hour": 2.204586, "kilogram_per_second": 0.000278, "ton_per_hour": 0.001}},
            "pound_per_hour": {"symbol": "lb/hour", "conversions": {"kilogram_per_hour": 0.4536, "kilogram_per_second": 0.000126, "ton_per_hour": 0.000454}},
            "kilogram_per_second": {"symbol": "kg/s", "conversions": {"kilogram_per_hour": 3600, "pound_per_hour": 7936.508, "ton_per_hour": 3.6}},
            "ton_per_hour": {"symbol": "t/h", "conversions": {"kilogram_per_hour": 1000, "pound_per_hour": 2204.586, "kilogram_per_second": 0.277778}},
        }

        self.high_pressure_units = {
            "bar": {"symbol": "bar", "conversions": {"pound_per_square_inch": 14.50326, "kilopascal": 100, "megapascal": 0.1, "kgf/cm2": 1.01968, "mm_Hg": 750.0188, "atm": 0.987167}},
            "pound_per_square_inch": {"symbol": "psi", "conversions": {"bar": 0.06895, "kilopascal": 6.895, "megapascal": 0.006895, "kgf/cm2": 0.070307, "mm_Hg": 51.71379, "atm": 0.068065}},
            "kilopascal": {"symbol": "kPa", "conversions": {"bar": 0.01, "pound_per_square_inch": 0.1450, "megapascal": 0.001, "kgf/cm2": 0.01020, "mm_Hg": 7.5002, "atm": 0.00987}},
            "megapascal": {"symbol": "MPa", "conversions": {"bar": 10, "pound_per_square_inch": 145.03, "kilopascal": 1000, "kgf/cm2": 10.1972, "mm_Hg": 7500.188, "atm": 9.87167}},
        }

        # Create a notebook
        self.notebook = ttk.Notebook(self.root)
        self.notebook.grid(row=0, column=0, padx=10, pady=10)

        # Create tabs for different unit types
        self.create_tab("Length", self.length_units)
        self.create_tab("Area", self.area_units)
        self.create_tab("Volume", self.volume_units)
        self.create_tab("Mass", self.mass_units)
        self.create_tab("Normal Flow", self.normal_flow_units)
        self.create_tab("Mass Flow", self.mass_flow_units)
        self.create_tab("High Pressure", self.high_pressure_units)

    def create_tab(self, title, units_dict):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text=title)

        label_value = tk.Label(frame, text="Value:")
        label_value.grid(row=0, column=0, padx=10, pady=10)

        entry_value = tk.Entry(frame)
        entry_value.grid(row=0, column=1, padx=10, pady=10)

        label_from = tk.Label(frame, text="From:")
        label_from.grid(row=1, column=0, padx=10, pady=10)

        combo_from = ttk.Combobox(frame, values=list(units_dict.keys()))
        combo_from.grid(row=1, column=1, padx=10, pady=10)
        combo_from.current(0)

        label_to = tk.Label(frame, text="To:")
        label_to.grid(row=2, column=0, padx=10, pady=10)

        combo_to = ttk.Combobox(frame, values=list(units_dict.keys()))
        combo_to.grid(row=2, column=1, padx=10, pady=10)
        combo_to.current(1)

        label_result = tk.Label(frame, text="Result:")
        label_result.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        button_convert = tk.Button(frame, text="Convert", command=lambda: self.convert(units_dict, entry_value, combo_from, combo_to, label_result))
        button_convert.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def convert(self, units_dict, entry_value, combo_from, combo_to, label_result):
        try:
            input_value = float(entry_value.get())
            from_unit = combo_from.get()
            to_unit = combo_to.get()
            if to_unit in units_dict[from_unit]["conversions"]:
                conversion_factor = units_dict[from_unit]["conversions"][to_unit]
                result = input_value * conversion_factor
                label_result.config(text=f"Result: {result:.4f} {to_unit}")
            else:
                label_result.config(text="Error: Invalid conversion")
        except ValueError:
            label_result.config(text="Error: Invalid input value")
        except Exception as e:
            label_result.config(text=f"Error: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = UnitConverter(root)
    root.mainloop()
