data = ("hello", 10, "goodbye", "3", "goodnight", 5, 6.7, True)

user_input = input("Enter a value to append: ")

try:
    data.append(user_input)
except Exception as e:
    print("Attempted to append to a tuple.")
    print("Error message:", e)

print(data)