data = ("hello", 10, "goodbye", "3", "goodnight", 5, 6.7, True)

user_input = input("Enter a value to append: ")

try:
    data.append(user_input)
except Exception:
    data = data + (user_input,)   # create new tuple

print(data)