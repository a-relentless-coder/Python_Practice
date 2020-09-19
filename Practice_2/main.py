## Odd or even
number = int(input("Enter a number: "))
num = number % 2
if num < 0:
    print("This number is an odd number.")
else:
    print("This number is a even number.")