# 2(a)
values = [1, "hi", 3.14, True, None]

n = len(values)

if n < 5:
    print("Fewer than 5 elements")
elif 5 <= n <= 10:
    print("Between 5 and 10 elements (inclusive)")
else:
    print("More than 10 elements")