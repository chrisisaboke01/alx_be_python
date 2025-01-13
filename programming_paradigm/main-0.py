import sys
from bank_account import BankAccount

def main():
    # Initialize a bank account with a starting balance of 100
    account = BankAccount(100)

    # Check if sufficient command line arguments are provided
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Parse the command and parameters from the command line
    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    # Perform operations based on the command
    if command == "deposit" and amount is not None:
        try:
            account.deposit(amount)
            print(f"Deposited: ${amount:.2f}")
        except ValueError as e:
            print(f"Error: {e}")
    elif command == "withdraw" and amount is not None:
        try:
            if account.withdraw(amount):
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds.")
        except ValueError as e:
            print(f"Error: {e}")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command or parameters.")

if __name__ == "__main__":
    main()
