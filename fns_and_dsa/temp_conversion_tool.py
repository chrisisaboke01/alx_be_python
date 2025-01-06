# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  # (5/9) to convert Fahrenheit to Celsius
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  # (9/5) to convert Celsius to Fahrenheit
FAHRENHEIT_TO_CELSIUS_OFFSET = 32  # Offset for Fahrenheit to Celsius conversion
CELSIUS_TO_FAHRENHEIT_OFFSET = 32  # Offset for Celsius to Fahrenheit conversion

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    # Use the global conversion factor and offset to convert
    celsius = (fahrenheit - CELSIUS_TO_FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    # Use the global conversion factor and offset to convert
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + CELSIUS_TO_FAHRENHEIT_OFFSET
    return fahrenheit

# Main function to handle user interaction
def main():
    try:
        # Prompt the user for the temperature and the unit
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Check for valid input and perform conversion
        if unit == 'F':
            result = convert_to_celsius(temperature)
            print(f"{temperature}°F is {result:.2f}°C")
        elif unit == 'C':
            result = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {result:.2f}°F")
        else:
            print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        # Handle non-numeric temperature input
        print("Invalid temperature. Please enter a numeric value.")

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
