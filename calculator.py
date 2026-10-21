# Store conversion factors in a dictionary so they can be changed in one place
CONVERSION_FACTORS = {
    "km_to_miles": 0.621371,
    "kg_to_pounds": 2.20462
}

def read_number(prompt):
    # Loop until float() succeeds to handle bad input without crashing
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number, for example 12 or 3.5.")