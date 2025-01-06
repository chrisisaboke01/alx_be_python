# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main program for user interaction
def main():
    try:
        # Prompt the user to enter a temperature
        temperature = input("Enter the temperature to convert: ")
        
        # Validate numeric input
        if not temperature.replace('.', '', 1).lstrip('-').isdigit():
            raise ValueError("Invalid temperature. Please enter a numeric value.")

        # Convert input to float
        temperature = float(temperature)
        
        # Prompt the user to specify the temperature unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Perform conversion based on the unit
        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature:.1f}\u00b0C is {converted_temp:.1f}\u00b0F")
        elif unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature:.1f}\u00b0F is {converted_temp:.1f}\u00b0C")
        else:
            # Raise an error if the unit is invalid
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as e:
        # Handle invalid input errors
        print(e)

# Execute the main program
if __name__ == "__main__":
    main()
