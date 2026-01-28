# The Rules of FizzBuzz
# You need to print numbers from 1 to 100, but with three "replacement" rules:
# If a number is divisible by 3, print "Fizz" instead of the number.
# If a number is divisible by 5, print "Buzz" instead of the number.
# If a number is divisible by BOTH 3 and 5, print "FizzBuzz".

for num in range(1, 101):
    if num % (3 * 5) == 0:  # other way: if num % 3 == 0 and num % 5 == 0
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)


username = input("Enter your name: ")
password = input("Enter your password: ")

if username == "admin" and password == "1234":
    print("Access granted")
else:
    print("Access denied")
