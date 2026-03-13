birth_year = 2006
closest_leap = 2006  # example
print(birth_year, ((birth_year % 4 == 0) and (birth_year % 100 != 0)) or (birth_year % 400 == 0))
print(closest_leap, ((closest_leap % 4 == 0) and (closest_leap % 100 != 0)) or (closest_leap % 400 == 0))


year = 2006

is_leap = ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)
print(is_leap)


 def isLeapYear(year):
    # Assumes year is a positive integer
    if year % 400 == 0:
        return "Leap year"
    if year % 100 == 0:
        return "Not a leap year"
    if year % 4 == 0:
        return "Leap year"
    return "Not a leap year"



