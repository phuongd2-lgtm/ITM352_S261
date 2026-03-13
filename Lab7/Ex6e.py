data = ("hello", 10, "goodbye", "3", "goodnight", 5, 6.7, True)

user_input = input("Enter a value to append: ")

data = (*data, user_input)

print(data)