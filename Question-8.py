# Q8: Is a number is even or odd

def check_even_odd(num):
    if num==0:
        print("0 is neither even nor odd.")
    elif num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")


check_even_odd(12)
check_even_odd(3)
check_even_odd(0)
check_even_odd(4)