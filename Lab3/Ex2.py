# Create a function called midpoint

def midpoint(num1, num2):
    """Calculate the midpoint between two numbers."""
    mid = (num1 + num2) / 2
    return midpoint

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = midpoint(num1, num2)
print(f"The midpoint between {num1} and {num2} is {result}.") 