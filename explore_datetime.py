# explore_datetime.py
import datetime

# Part 1: Display the Current Date and Time
def display_current_datetime():
    # Get the current date and time
    current_date = datetime.datetime.now()
    
    # Format and print the current date and time
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

# Part 2: Calculate a Future Date
def calculate_future_date():
    # Ask the user for the number of days to add
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    
    # Get the current date and calculate the future date
    current_date = datetime.datetime.now()
    future_date = current_date + datetime.timedelta(days=number_of_days)
    
    # Print the future date in the format "YYYY-MM-DD"
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

# Main execution
if __name__ == "__main__":
    # Display current date and time
    display_current_datetime()
    
    # Calculate future date
    calculate_future_date()
