# Q7: Is a number is positive or negative
def check_positive(num):
    if num == 0:
        print(f"{num} is neither positive nor negative.")
    elif num > 0:
        print(f"{num} is positive number.")
    else:
        print(f"{num} is negative number.")


check_positive(-12)
check_positive(12)
