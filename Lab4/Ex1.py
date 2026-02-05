#Name: Phuong Duong
#Date: Jan 30, 2026

# 1) Input three strings
first = input("Enter first name: ")
middle = input("Enter middle initial: ")
last = input("Enter last name: ")

# A) Using + concatenation operator
full_plus = first + " " + middle + " " + last
print("Using +:", full_plus)

# B) Using an f-string
full_f = f"{first} {middle} {last}"
print("Using f-string:", full_f)

# C) Using the % operator
full_percent = "%s %s %s" % (first, middle, last)
print("Using %:", full_percent)

# D) Using format() method
full_format = "{} {} {}".format(first, middle, last)
print("Using format():", full_format)

# E) Using join() method
parts = [first, middle, last]
full_join = " ".join(parts)
print("Using join():", full_join)

# F) Using format() with unpacking the list
full_unpack = "{} {} {}".format(*parts)
print("Using format() + unpacking:", full_unpack)
