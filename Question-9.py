# Q9: Leap Year
year = int(input("Enter the year: "))

if (year % 400 == 0) and (year % 100 == 0):
    print(f"{year} is a Leap Year.")
elif (year % 4 == 0) and year % 100 != 0:
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} is not a Leap Year.")
