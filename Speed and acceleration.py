conversion_dict = {
    "m/s² to g": 0.1019368,
    "m/s to km/h": 3.6,
    "km/h to m/s": 0.28,
    "km/s to mi/h": 2236.9,
    "ft/s to m/s": 0.3048,
    "mi/h to m/s": 0.447,
    "m/s to ft/s": 3.28,
    "km/s to m/s": 1000,
    "ft/min to m/s": 0.00508,
    "mi/h to ft/s": 1.47,
    "cm/s to m/s": 0.01, # ÷100
    "rpm to m/s": lambda r: 2 * (3.14159 * r / 30), # Formula involving radius r
    "gravity": 9.81, # m/s² for 1 g
}

# Example usage
def convert(value, from_unit, to_unit, radius=None):
    key = f"{from_unit} to {to_unit}"
    conversion_factor = conversion_dict.get(key)
    if callable(conversion_factor):  # Check if the conversion factor is a function
        return conversion_factor(radius) * value
    return value * conversion_factor

# Convert 1 m/s² to g
print(convert(1, "m/s²", "g"))  # Output: 0.1019368

# Convert 1 m/s to km/h
print(convert(1, "m/s", "km/h"))  # Output: 3.6

# Convert 1 rpm to m/s with radius 1
print(convert(1, "rpm", "m/s", radius=1))  # Output: 0.20943951023931953
