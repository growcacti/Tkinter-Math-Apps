conversion_data = {
    "Square Measure": {
        "sq_centimeter": {"sq_inch": 0.1550},
        "sq_inch": {"sq_centimeter": 6.452},
        "sq_decimeter": {"sq_foot": 0.1076},
        "sq_foot": {"sq_decimeter": 9.2903},
        "sq_meter": {"sq_yard": 1.196},
        "sq_yard": {"sq_meter": 0.8361},
        "acre": {"sq_rod": 3954},
        "sq_rod": {"acre": 0.2529},
        "hectare": {"acre": 2.47},
        "acre_to_hectare": {"hectare": 0.4047},
        "sq_kilometer": {"sq_mile": 0.386},
        "sq_mile": {"sq_kilometer": 2.59}
    },
    "Weights": {
        "gram": {"ounce": 0.03527},
        "ounce": {"gram": 28.35},
        "kilogram": {"pound": 2.2046},
        "pound": {"kilogram": 0.4536},
        "metric_ton": {"english_ton": 1.1023},
        "english_ton": {"metric_ton": 0.9027}
    },
    "Approximate Equivalents": {
        "decimeter": {"inch": 4},
        "liter": {"quart_fl": 1.06, "quart_dry": 0.9},
        "meter": {"yard": 1.1},
        "kilometer": {"mile": 0.625},
        "hectoliter": {"bushel": 2.625},
        "hectare": {"acre": 2.5},
        "kilogram": {"pound": 2.2},
        "cubic_meter": {"cord": 0.25},
        "metric_ton": {"english_ton": 1.1}
    },
    "Linear Measure": {
        "centimeter": {"inch": 0.3937},
        "inch": {"centimeter": 2.54},
        "decimeter": {"inch": 3.937},
        "foot": {"decimeter": 3.048},
        "meter": {"inch": 39.37, "yard": 1.0936},
        "yard": {"meter": 0.9144},
        "dekameter": {"rod": 1.9884},
        "rod": {"dekameter": 0.5029},
        "kilometer": {"mile": 0.62137},
        "mile": {"kilometer": 1.6093}
    },
    "Measure of Volume": {
        "cu_centimeter": {"cu_inch": 0.061},
        "cu_inch": {"cu_centimeter": 16.39},
        "cu_decimeter": {"cu_foot": 0.0353},
        "cu_foot": {"cu_decimeter": 28.347},
        "cubic_meter": {"cubic_yard": 1.308},
        "cubic_yard": {"cubic_meter": 0.7646},
        "stere": {"cord": 0.2759},
        "cord": {"stere": 3.624},
        "liter": {"quart_dry": 0.908, "quart_liquid": 1.0567},
        "quart_dry": {"liter": 1.101},
        "quart_liquid": {"liter": 0.9463},
        "dekaliter": {"gallon": 2.6417},
        "gallon": {"dekaliter": 0.3785},
        "peck": {"dekaliter": 0.881},
        "hectoliter": {"bushel": 2.8375},
        "bushel": {"hectoliter": 0.3524}
    },
    "Temperature Conversion": {
        "celsius_to_fahrenheit": lambda c: (c * 9/5) + 32,
        "fahrenheit_to_celsius": lambda f: (f - 32) * 5/9,
        "celsius_to_kelvin": lambda c: c + 273.15,
        "kelvin_to_celsius": lambda k: k - 273.15,
        "fahrenheit_to_kelvin": lambda f: (f - 32) * 5/9 + 273.15,
        "kelvin_to_fahrenheit": lambda k: (k - 273.15) * 9/5 + 32
    }
}
