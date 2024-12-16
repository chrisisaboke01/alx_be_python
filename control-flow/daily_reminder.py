# daily_reminder.py

# Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match-case to handle different priorities
match priority:
    case "high":
        priority_message = "high priority task"
    case "medium":
        priority_message = "medium priority task"
    case "low":
        priority_message = "low priority task"
    case _:
        priority_message = "unknown priority task"

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    time_message = "that requires immediate attention today!"
else:
    time_message = "Consider completing it when you have free time."

# Provide the customized reminder
print(f"Reminder: '{task}' is a {priority_message} {time_message}")
