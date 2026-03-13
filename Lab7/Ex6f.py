data = ("hello", 10, "goodbye", "3", "goodnight", 5, 6.7, True)

user_input = input("Enter a value to append: ")

data_list = list(data)
data_list.append(user_input)

data = tuple(data_list)   # convert back to tuple

print(data)