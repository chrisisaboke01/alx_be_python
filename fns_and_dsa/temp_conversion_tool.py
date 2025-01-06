# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    # Use the global conversion factor for Fahrenheit to Celsius
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    # Use the global conversion factor for Celsius to Fahrenheit
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main user interaction function
def main():
    try:
        # Prompt the user for temperature input
        temp_input = input("Enter the temperature to convert: ")

        # Check if the entered temperature is numeric and valid
        if not temp_input.replace('.', '', 1).isdigit() or temp_input.count('.') > 1:
            raise ValueError("Invalid temperature. Please enter a numeric value.")

        # Convert the input to float
        temp = float(temp_input)

        # Prompt the user for the unit (Celsius or Fahrenheit)
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Validate the unit input
        if unit not in ["C", "F"]:
            raise ValueError("Invalid temperature unit. Please enter either 'C' or 'F'.")

        # Perform conversion based on the unit
        if unit == "C":
            # Convert Celsius to Fahrenheit
            converted_temp = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {converted_temp:.1f}°F")  # Show the result with one decimal place
        elif unit == "F":
            # Convert Fahrenheit to Celsius
            converted_temp = convert_to_celsius(temp)
            print(f"{temp}°F is {converted_temp:.8f}°C")  # Show the result with full precision

    except ValueError as e:
        # Handle errors related to invalid input
        print(e)

# Ensure the script runs only when executed as a script (not imported)
if __name__ == "__main__":
    main()
