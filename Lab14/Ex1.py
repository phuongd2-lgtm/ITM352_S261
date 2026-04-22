import matplotlib.pyplot as plt

# first set of values
x1 = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]

# second set of values
x2 = [1, 2, 3, 4, 5]
y2 = [1, 3, 5, 7, 9]

# line graph (first set)
plt.plot(x1, y1, label="Line 1")

# scatter plot (first set)
plt.scatter(x1, y1)

# second line graph
plt.plot(x2, y2, label="Line 2")

# title and labels
plt.title("Simple Visualization")
plt.xlabel("X Values")
plt.ylabel("Y Values")

# legend
plt.legend()

# show graph
plt.show()