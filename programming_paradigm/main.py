import sys
from robust_division_calculator import safe_divide

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    # Retrieve numerator and denominator from command-line arguments
    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Perform the division using the safe_divide function
    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
