searchMe = [2, 5, 7, 11, 15, 22, 27, 30, 34, 41, 55, 57, 58, 60, 77]

x = int(input("Enter a number to search for: "))

found = False
for value in searchMe:
    if value == x:
        found = True
        break

if found:
    print(x, "is in the array.")
else:
    print(x, "is NOT in the array.")