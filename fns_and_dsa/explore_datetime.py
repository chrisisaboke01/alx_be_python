# explore_datetime.py

import datetime

# Part 1: Display the Current Date and Time
def display_current_datetime():
    # Get the current date and time
    current_date = datetime.datetime.now()
    # Print in the desired format: "YYYY-MM-DD HH:MM:SS"
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

# Part 2: Calculate a Future Date
def calculate_future_date():
    try:
        # Prompt the user for the number of days to add
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        # Get the current date and time
        current_date = datetime.datetime.now()
        # Add the specified number of days
        future_date = current_date + datetime.timedelta(days=days_to_add)
        # Print the future date in the format "YYYY-MM-DD"
        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    except ValueError:
        print("Invalid input. Please enter a valid integer for the number of days.")

# Main function to run the script
def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
