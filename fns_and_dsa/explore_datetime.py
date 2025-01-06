# Import necessary components from the datetime module
from datetime import datetime, timedelta

# Part 1: Function to display the current date and time
def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Print the current date and time in the format YYYY-MM-DD HH:MM:SS
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

# Part 2: Function to calculate a future date by adding specified days
def calculate_future_date(days_to_add):
    # Get the current date
    current_date = datetime.now()
    # Calculate the future date by adding the specified number of days
    future_date = current_date + timedelta(days=days_to_add)
    # Print the future date in the format YYYY-MM-DD
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

# Main function to handle user interaction
def main():
    # Part 1: Display current date and time
    display_current_datetime()

    # Part 2: Prompt the user to enter a number of days
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        # Call the function to calculate and display the future date
        calculate_future_date(days)
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")  # Improved error message

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
