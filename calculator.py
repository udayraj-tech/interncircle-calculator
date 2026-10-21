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

def km_to_miles(km):
    return km * CONVERSION_FACTORS["km_to_miles"]

def kg_to_pounds(kg):
    return kg * CONVERSION_FACTORS["kg_to_pounds"]

def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

def main():
    while True:
        print("\n1) Add 2) Subtract 3) Multiply 4) Divide 5) Convert units 6) Quit")
        choice = input("Choose an option: ").strip()

        if choice == "6":
            print("Goodbye!")
            break

        if choice in ("1", "2", "3", "4"):
            a = read_number("First number: ")
            b = read_number("Second number: ")

            if choice == "1":
                print("Result:", add(a, b))
            elif choice == "2":
                print("Result:", subtract(a, b))
            elif choice == "3":
                print("Result:", multiply(a, b))
            elif choice == "4":
                print("Result:", divide(a, b))
        
        elif choice == "5":
            print("\n  A) km to miles  B) kg to pounds  C) Celsius to Fahrenheit")
            conv_choice = input("Choose conversion: ").strip().upper()
            if conv_choice == 'A':
                km = read_number("Kilometers: ")
                print(f"Result: {km_to_miles(km)} miles")
            elif conv_choice == 'B':
                kg = read_number("Kilograms: ")
                print(f"Result: {kg_to_pounds(kg)} pounds")
            elif conv_choice == 'C':
                c = read_number("Celsius: ")
                print(f"Result: {celsius_to_fahrenheit(c)} F")
            else:
                print("Invalid conversion option.")
        else:
            print("Please pick a number from 1 to 6.")

if __name__ == '__main__':
    main()