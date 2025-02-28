metric_measures = {
    "linear_measure": {
        "millimeter_to_centimeter": 10,
        "centimeter_to_decimeter": 10,
        "decimeter_to_meter": 10,
        "meter_to_dekameter": 10,
        "dekameter_to_hectometer": 10,
        "hectometer_to_kilometer": 10
    },
    "square_measure": {
        "sq_millimeter_to_sq_centimeter": 100,
        "sq_centimeter_to_sq_decimeter": 100,
        "sq_decimeter_to_sq_meter": 100,
        "sq_meter_to_sq_dekameter": 100,
        "sq_dekameter_to_sq_hectometer": 100,
        "sq_hectometer_to_sq_kilometer": 100
    },
    "liquid_measure": {
        "milliliter_to_centiliter": 10,
        "centiliter_to_deciliter": 10,
        "deciliter_to_liter": 10,
        "liter_to_dekaliter": 10,
        "dekaliter_to_hectoliter": 10,
        "hectoliter_to_kiloliter": 10
    },
    "weights": {
        "milligram_to_centigram": 10,
        "centigram_to_decigram": 10,
        "decigram_to_gram": 10,
        "gram_to_dekagram": 10,
        "dekagram_to_hectogram": 10,
        "hectogram_to_kilogram": 10,
        "kilogram_to_quintal": 100,
        "quintal_to_ton": 10
    },
    "cubic_measure": {
        "cu_millimeter_to_cu_centimeter": 1000,
        "cu_centimeter_to_cu_decimeter": 1000,
        "cu_decimeter_to_cu_meter": 1000
    },
    "metric_equivalents": {
        "sq_centimeter_to_square_inch": 0.1550,
        "square_inch_to_sq_centimeter": 6.452,
        "sq_decimeter_to_square_foot": 0.1076,
        "square_foot_to_sq_decimeter": 9.2903,
        "sq_meter_to_square_yard": 1.196,
        "square_yard_to_sq_meter": 0.8361,
        "acre_to_square_rod": 3.954,
        "square_rod_to_acre": 0.2529,
        "hectare_to_acre": 2.47,
        "acre_to_hectare": 0.4047
    }
}

# Example usage:
# Convert millimeters to centimeters
millimeters = 50
centimeters = millimeters / metric_measures["linear_measure"]["millimeter_to_centimeter"]
print(f"{millimeters} millimeters is {centimeters} centimeters.")
