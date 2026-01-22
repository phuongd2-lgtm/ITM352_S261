def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def get_operation():
    while True:
        op = input("Choose an operation (+, -, *, /): ").strip()
        if op in ["+", "-", "*", "/"]:
            return op
        print("Invalid operation. Try again.")

def calculate(a, b, op):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            return None
        return a / b

def main():
    print("Simple Calculator")
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    op = get_operation()

    result = calculate(num1, num2, op)

    if result is None:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"Result: {num1} {op} {num2} = {result}")

if __name__ == "__main__":
    main()