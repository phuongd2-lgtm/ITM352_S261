# 3(b) test cases: [hits, spins, expected]
test_cases = [
    [10, 0,  "Get going!"],      # spins == 0

    [0,  10, "Get going!"],      # ratio == 0 -> else branch

    [1,  10, "On your way!"],    # ratio = 0.1 (>0 but <0.25)

    [3,  10, "Almost there!"],   # ratio = 0.3 (>=0.25 but <0.5)

    [5,  10, "You win!"],        # ratio = 0.5 and hits < spins

    [10, 10, "Almost there!"],   # ratio = 1.0 but hits < spins is False, so not "You win!"
]


test_cases = [
    [10, 0],    # spins = 0 → "Get going!"
    [0, 10],    # ratio = 0 → "Get going!"
    [1, 10],    # ratio = 0.1 → "On your way!"
    [3, 10],    # ratio = 0.3 → "Almost there!"
    [5, 10],    # ratio = 0.5 and hits < spins → "You win!"
    [10, 10]    # ratio = 1.0 but hits < spins is False → "Almost there!"
]

for hits, spins in test_cases:
    print(hits, spins, determine_progress1(hits, spins))


    def determine_progress3(hits, spins):
    if spins == 0:
        return "Get going!"

    ratio = hits / spins

    if ratio <= 0:
        return "Get going!"
    elif ratio < 0.25:
        return "On your way!"
    elif ratio < 0.5:
        return "Almost there!"
    elif hits < spins:
        return "You win!"
    else:
        return "Almost there!"

