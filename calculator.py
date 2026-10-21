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

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # Check for zero explicitly instead of letting Python raise an error
    if b == 0:
        return "Cannot divide by zero."
    return a / b

