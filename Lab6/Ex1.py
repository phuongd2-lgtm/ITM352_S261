result = motions = ("happy", "sad", "fear", "surprise")
emotions = ("happy", "sad", "fear", "surprise")

# Write code that uses a conditional expression (do not use an if-statement or ternarry expression  ) to
# print "true" if the last element is "happy" and there are more than 3 elements in the tuple, or "false" if it it not.
result = emotions[-1] == "happy" and len(emotions) > 3
if(result):
    print("true")
else:
    print("false")




# 1(a)
emotions = ("happy", "sad", "fear", "surprise")

# Prints True/False using a boolean expression (no if, no ternary)
print(emotions[-1] == "happy" and len(emotions) > 3)
