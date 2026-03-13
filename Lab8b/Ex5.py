# Retrieving elements from a list
def get_element(my_list, index):
    if 0 <= index < len(my_list):
        return my_list[index]
    else:
        return "Index out of range"


my_list = [1, 2, 3, 4, 5]
print(get_element(my_list, 2))  
print(get_element(my_list, 5))  


# Program to remove any scores from a list that are below 50.

scores = [60, 45, 30, 85, 10, 90]

filtered_scores = []

for score in scores:
    if score >= 50:
        filtered_scores.append(score)

print(filtered_scores)

# Write code that will iterate through numbers from 1 to 10 and print
# the number if it is not equal to 5 (using continue) and stop the
# loop entirely and print a message when it reaches 8 (using break).

for x in range(1, 11):
    if x == 5:
        continue
    if x == 8:
        print("done!")
        break
    print(x)


    # Algorithm for multiplying two numbers by successive addition.

def multiply(x, y):
    product = 0
    for i in range(y):
        product += x
    return product

first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
prod = multiply(first, second)

print(f"The product of {first}, {second} is {prod}")