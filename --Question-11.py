# Q11: Prime Number

num = int(input("Enter a number: "))

if num == 1:
    print("It's not a prime number.")

if num > 1:
    for i in range(2, num):
        if num % 2 == 0:
            print("It is not a prime number.")
            break
    else:
        print("It is a prime number.")
