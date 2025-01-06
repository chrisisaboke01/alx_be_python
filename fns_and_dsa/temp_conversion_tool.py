# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main user interaction
def main():
    try:
        # Get user input for temperature
        temp_input = input("Enter the temperature to convert: ")

        # Validate if input is a valid numeric value
        if not temp_input.replace('.', '', 1).isdigit() or temp_input.count('.') > 1:
            raise ValueError("Invalid temperature. Please enter a numeric value.")

        temp = float(temp_input)  # Convert to float

        # Get the unit of the temperature
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "C":
            # Convert Celsius to Fahrenheit
            converted_temp = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {converted_temp:.1f}°F")  # Output with one decimal place
        elif unit == "F":
            # Convert Fahrenheit to Celsius
            converted_temp = convert_to_celsius(temp)
            print(f"{temp}°F is {converted_temp:.8f}°C")  # Output with full precision
        else:
            print("Invalid input for temperature unit. Please enter either 'C' or 'F'.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
