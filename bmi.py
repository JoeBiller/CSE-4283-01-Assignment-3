# Matthew Lane (ml2162) - CSE 4283-01: Assignment 3

# This function will check if the measurement provided
# is a string, then check if said string is a valid
# int above the provided floor.
def verify_measurement(measurement, name, floor):
    try:
        assert type(measurement) is str
        measurement = int(measurement)
        assert measurement >= floor
    except:
        return measurement, f"Please enter a valid number in {name} above {floor}."
    return measurement, None

# This function will convert a height in inches and
# weight in pounds into a BMI and BMI category.
def calculate_bmi(inches, pounds):
    # Convert weight in pounds to kilograms
    kilograms = pounds * 0.45

    # Convert inches to meters
    meters = inches * 0.025

    # Perform BMI calculation to one decimal place
    bmi = round(kilograms / (meters**2), 1)

    # Determine category
    category = ""
    if bmi < 18.5:
        category = "Underweight"
    if (bmi >= 18.5) and (bmi < 25):
        category = "Normal weight"
    if (bmi >= 25) and (bmi < 30):
        category = "Overweight"
    if bmi >= 30:
        category = "Obese"

    return bmi, category
