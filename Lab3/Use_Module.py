# Name: Phuong Duong
#Date: Jan 29, 2026

import HandyMath
from HandyMath import max, min


def main():
    """Ask the user for two numbers and display results using HandyMath functions."""

    # Ask the user for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Calculate results
    mid = HandyMath.midpoint(num1, num2)

    # "square root of the square of one number" (using num1)
    sqrt_of_square = HandyMath.sqrt(num1 ** 2)

    power_result = HandyMath.exponent(num1, num2)
    bigger = HandyMath.max(num1, num2)
    smaller = HandyMath.min(num1, num2)

    # Print results using f-strings
    print(f"\nMidpoint of {num1} and {num2} is {mid}")
    print(f"Square root of {num1} squared is {sqrt_of_square}")
    print(f"{num1} raised to the power of {num2} is {power_result}")
    print(f"Max of {num1} and {num2} is {bigger}")
    print(f"Min of {num1} and {num2} is {smaller}")

    # Extra credit
    print("\n--- Extra Credit ---")
    print(HandyMath.describe_function(num1, num2, HandyMath.min))
    print(HandyMath.describe_function(num1, num2, HandyMath.max))
    print(HandyMath.describe_function(num1, num2, HandyMath.exponent))

main()
