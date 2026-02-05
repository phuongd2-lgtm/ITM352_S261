def midpoint(num1, num2):
    """Calculate the midpoint between two numbers."""
    mid = (num1 + num2) / 2
    return mid

def sqrt(number):
    """Calculate the square root of a number."""
    if number < 0:
        return None
    return number ** 0.5

def exponent(base,exp):
    """Calculate the exponentiation of a base to a given exponent."""
    result = base ** exp
    rounded_result = round(result, 2)
    return rounded_result

def max(a, b):
    """Return the larger of two numbers."""
    result = a if a > b else b
    return result

def min(a, b):
    """Return the smaller of two numbers."""
    result = a if a < b else b
    return result

def describe_function(x, y, func):
    """Return a sentence showing the function name and its result on x and y."""
    result = func(x, y)
    message = f"The function {func.__name__} {x},{y} = {result}"
    return message




