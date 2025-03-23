# Dictionary for metric prefixes
metric_prefixes = {
    "exa": {"symbol": "E", "factor": 10**18, "value": 1_000_000_000_000_000_000},
    "peta": {"symbol": "P", "factor": 10**15, "value": 1_000_000_000_000_000},
    "tera": {"symbol": "T", "factor": 10**12, "value": 1_000_000_000_000},
    "giga": {"symbol": "G", "factor": 10**9, "value": 1_000_000_000},
    "mega": {"symbol": "M", "factor": 10**6, "value": 1_000_000},
    "kilo": {"symbol": "k", "factor": 10**3, "value": 1_000},
    "hecto": {"symbol": "h", "factor": 10**2, "value": 100},
    "deca": {"symbol": "da", "factor": 10**1, "value": 10},
    "deci": {"symbol": "d", "factor": 10**-1, "value": 0.1},
    "centi": {"symbol": "c", "factor": 10**-2, "value": 0.01},
    "milli": {"symbol": "m", "factor": 10**-3, "value": 0.001},
    "micro": {"symbol": "u", "factor": 10**-6, "value": 0.000_001},
    "nano": {"symbol": "n", "factor": 10**-9, "value": 0.000_000_001},
    "pico": {"symbol": "p", "factor": 10**-12, "value": 0.000_000_000_001},
    "femto": {"symbol": "f", "factor": 10**-15, "value": 0.000_000_000_000_001},
    "atto": {"symbol": "a", "factor": 10**-18, "value": 0.000_000_000_000_000_001},
}

# Dictionary for length units
length_units = {
    "millimeters": {"symbol": "mm", "conversions": {"cm": 0.1, "m": 0.001, "km": 0.000001, "in": 0.03937, "ft": 0.003281, "yd": 0.001094, "mi": 6.21e-07}},
    "centimeters": {"symbol": "cm", "conversions": {"mm": 10, "m": 0.01, "km": 0.00001, "in": 0.393701, "ft": 0.032808, "yd": 0.010936, "mi": 0.000006}},
    "meters": {"symbol": "m", "conversions": {"mm": 1000, "cm": 100, "km": 0.001, "in": 39.37008, "ft": 3.28084, "yd": 1.093613, "mi": 0.000621}},
    "kilometers": {"symbol": "km", "conversions": {"mm": 1_000_000, "cm": 100_000, "m": 1000, "in": 39370.08, "ft": 3280.84, "yd": 1093.613, "mi": 0.621371}},
    "inches": {"symbol": "in", "conversions": {"mm": 25.4, "cm": 2.54, "m": 0.0254, "km": 0.000025, "ft": 0.083333, "yd": 0.027778, "mi": 0.000016}},
    "feet": {"symbol": "ft", "conversions": {"mm": 304.8, "cm": 30.48, "m": 0.3048, "km": 0.000305, "in": 12, "yd": 0.333333, "mi": 0.000189}},
    "yards": {"symbol": "yd", "conversions": {"mm": 914.4, "cm": 91.44, "m": 0.9144, "km": 0.000914, "in": 36, "ft": 3, "mi": 0.000568}},
    "miles": {"symbol": "mi", "conversions": {"mm": 1_609_344, "cm": 160_934.4, "m": 1609.344, "km": 1.609344, "in": 63360, "ft": 5280, "yd": 1760}},
}

# Dictionary for area units
area_units = {
    "millimeter_square": {"symbol": "mm2", "conversions": {"cm2": 0.01, "m2": 0.000001, "in2": 0.00155, "ft2": 0.000011, "yd2": 0.000001}},
    "centimeter_square": {"symbol": "cm2", "conversions": {"mm2": 100, "m2": 0.0001, "in2": 0.155, "ft2": 0.001076, "yd2": 0.00012}},
    "meter_square": {"symbol": "m2", "conversions": {"mm2": 1_000_000, "cm2": 10_000, "in2": 1550.003, "ft2": 10.76391, "yd2": 1.19599}},
    "inch_square": {"symbol": "in2", "conversions": {"mm2": 645.16, "cm2": 6.4516, "m2": 0.000645, "ft2": 0.006944, "yd2": 0.000772}},
    "foot_square": {"symbol": "ft2", "conversions": {"mm2": 92903, "cm2": 929.0304, "m2": 0.092903, "in2": 144, "yd2": 0.111111}},
    "yard_square": {"symbol": "yd2", "conversions": {"mm2": 836127, "cm2": 8361.274, "m2": 0.836127, "in2": 1296, "ft2": 9}},
}

# Dictionary for volume units
volume_units = {
    "centimeter_cube": {"symbol": "cm3", "conversions": {"m3": 0.000001, "ltr": 0.001, "in3": 0.061024, "ft3": 0.000035, "US_gal": 0.000264, "Imp_gal": 0.00022, "US_brl": 0.000006}},
    "meter_cube": {"symbol": "m3", "conversions": {"cm3": 1_000_000, "ltr": 1000, "in3": 61024, "ft3": 35, "US_gal": 264, "Imp_gal": 220, "US_brl": 6.29}},
    "liter": {"symbol": "ltr", "conversions": {"cm3": 1000, "m3": 0.001, "in3": 61, "ft3": 0.035, "US_gal": 0.264201, "Imp_gal": 0.22, "US_brl": 0.00629}},
    "inch_cube": {"symbol": "in3", "conversions": {"cm3": 16.4, "m3": 0.000016, "ltr": 0.016387, "ft3": 0.000579, "US_gal": 0.004329, "Imp_gal": 0.003605, "US_brl": 0.000103}},
    "foot_cube": {"symbol": "ft3", "conversions": {"cm3": 28317, "m3": 0.028317, "ltr": 28.31685, "in3": 1728, "US_gal": 7.481333, "Imp_gal": 6.229712, "US_brl": 0.178127}},
    "US_gallons": {"symbol": "US_gal", "conversions": {"cm3": 3785, "m3": 0.003785, "ltr": 3.79, "in3": 231, "ft3": 0.13, "Imp_gal": 1, "US_brl": 0.832701}},
    "Imperial_gallons": {"symbol": "Imp_gal", "conversions": {"cm3": 4545, "m3": 0.004545, "ltr": 4.55, "in3": 277, "ft3": 0.16, "US_gal": 1.20, "US_brl": 1}},
    "US_barrel": {"symbol": "US_brl", "conversions": {"cm3": 158970, "m3": 0.15897, "ltr": 159, "in3": 9701, "ft3": 6, "US_gal": 42, "Imp_gal": 35}},
}

# Dictionary for mass units
mass_units = {
    "grams": {"symbol": "g", "conversions": {"kg": 0.001, "tonne": 0.000001, "shton": 0.000001, "Lton": 9.84e-07, "lb": 0.002205, "oz": 0.035273}},
    "kilograms": {"symbol": "kg", "conversions": {"g": 1000, "tonne": 0.001, "shton": 0.001102, "Lton": 0.000984, "lb": 2.204586, "oz": 35.27337}},
    "metric_tonnes": {"symbol": "tonne", "conversions": {"g": 1_000_000, "kg": 1000, "shton": 1.102293, "Lton": 0.984252, "lb": 2204.586, "oz": 35273.37}},
    "short_ton": {"symbol": "shton", "conversions": {"g": 907200, "kg": 907.2, "tonne": 0.9072, "Lton": 1, "lb": 2000, "oz": 32000}},
    "long_ton": {"symbol": "Lton", "conversions": {"g": 1016000, "kg": 1016, "tonne": 1.016, "shton": 1.119929, "lb": 2239.859, "oz": 35837.74}},
    "pounds": {"symbol": "lb", "conversions": {"g": 453.6, "kg": 0.4536, "tonne": 0.000454, "shton": 0.0005, "Lton": 0.000446, "oz": 16}},
    "ounces": {"symbol": "oz", "conversions": {"g": 28, "kg": 0.02835, "tonne": 0.000028, "shton": 0.000031, "Lton": 0.000028, "lb": 0.0625}},
}

# Dictionary for density units
density_units = {
    "grams_per_milliliter": {"symbol": "g/ml", "conversions": {"kg/m3": 1000, "lb/ft3": 62.42197, "lb/in3": 0.036127}},
    "kilograms_per_cubic_meter": {"symbol": "kg/m3", "conversions": {"g/ml": 0.001, "lb/ft3": 0.062422, "lb/in3": 0.000036}},
    "pounds_per_cubic_foot": {"symbol": "lb/ft3", "conversions": {"g/ml": 0.01602, "kg/m3": 16.02, "lb/in3": 0.000579}},
    "pounds_per_cubic_inch": {"symbol": "lb/in3", "conversions": {"g/ml": 27.68, "kg/m3": 27680, "lb/ft3": 1727.84}},
}

# Dictionary for volumetric liquid flow units
volumetric_flow_units = {
    "liter_per_second": {"symbol": "L/sec", "conversions": {"L/min": 60, "m3/hr": 3.6, "ft3/min": 2.119093, "ft3/hr": 127.1197, "gal/min": 15.85037, "US_brl/d": 543.4783}},
    "liter_per_minute": {"symbol": "L/min", "conversions": {"L/sec": 0.016666, "m3/hr": 0.06, "ft3/min": 0.035317, "ft3/hr": 2.118577, "gal/min": 0.264162, "US_brl/d": 9.057609}},
    "meter_cube_per_hour": {"symbol": "m3/hr", "conversions": {"L/sec": 0.277778, "L/min": 16.6667, "ft3/min": 0.588637, "ft3/hr": 35.31102, "gal/min": 4.40288, "US_brl/d": 150.9661}},
    "foot_cube_per_minute": {"symbol": "ft3/min", "conversions": {"L/sec": 0.4719, "L/min": 28.31513, "m3/hr": 1.69884, "ft3/hr": 60, "gal/min": 7.479791, "US_brl/d": 256.4674}},
    "foot_cube_per_hour": {"symbol": "ft3/hr", "conversions": {"L/sec": 0.007867, "L/min": 0.472015, "m3/hr": 0.02832, "ft3/min": 0.01667, "gal/min": 0.124689, "US_brl/d": 4.275326}},
    "us_gallons_per_minute": {"symbol": "gal/min", "conversions": {"L/sec": 0.06309, "L/min": 3.785551, "m3/hr": 0.227124, "ft3/min": 0.133694, "ft3/hr": 8.019983, "US_brl/d": 34.28804}},
    "us_barrels_per_day": {"symbol": "US_brl/d", "conversions": {"L/sec": 0.00184, "L/min": 0.110404, "m3/hr": 0.006624, "ft3/min": 0.003899, "ft3/hr": 0.2339, "gal/min": 0.029165}},
}

# Dictionary for normal meter cube per hour units
normal_flow_units = {
    "normal_meter_cube_per_hour": {"symbol": "Nm3/hr", "conversions": {"scfh": 35.31073, "scfm": 0.588582}},
    "standard_cubic_feet_per_hour": {"symbol": "scfh", "conversions": {"Nm3/hr": 0.02832, "scfm": 0.016669}},
    "standard_cubic_feet_per_minute": {"symbol": "scfm", "conversions": {"Nm3/hr": 1.699, "scfh": 59.99294}},
}

# Dictionary for mass flow units
mass_flow_units = {
    "kilogram_per_hour": {"symbol": "kg/h", "conversions": {"lb/hour": 2.204586, "kg/s": 0.000278, "t/h": 0.001}},
    "pound_per_hour": {"symbol": "lb/hour", "conversions": {"kg/h": 0.4536, "kg/s": 0.000126, "t/h": 0.000454}},
    "kilogram_per_second": {"symbol": "kg/s", "conversions": {"kg/h": 3600, "lb/hour": 7936.508, "t/h": 3.6}},
    "ton_per_hour": {"symbol": "t/h", "conversions": {"kg/h": 1000, "lb/hour": 2204.586, "kg/s": 0.277778}},
}

# Dictionary for high pressure units
high_pressure_units = {
    "bar": {"symbol": "bar", "conversions": {"psi": 14.50326, "kPa": 100, "MPa": 0.1, "kgf/cm2": 1.01968, "mm_Hg": 750.0188, "atm": 0.987167}},
    "pound_per_square_inch": {"symbol": "psi", "conversions": {"bar": 0.06895, "kPa": 6.895, "MPa": 0.006895, "kgf/cm2": 0.070307, "mm_Hg": 51.71379, "atm": 0.068065}},
    "kilopascal": {"symbol": "kPa", "conversions": {"bar": 0.01, "psi": 0.1450, "MPa": 0.001, "kgf/cm2": 0.01020, "mm_Hg": 7.5002, "atm": 0.00987}},
    "megapascal": {"symbol": "MPa", "conversions": {"bar": 10, "psi": 145.03,
