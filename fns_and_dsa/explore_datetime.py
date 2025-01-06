# explore_datetime.py

import datetime

# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.datetime.now()  # Get current date and time
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

# Part 2: Calculate a Future Date
def calculate_future_date():
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.datetime.now()  # Get current date and time
        future_date = current_date + datetime.timedelta(days=days_to_add)
        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    except ValueError:
        print("Invalid input. Please enter a valid integer for the number of days.")

# Main function to execute the script
def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
