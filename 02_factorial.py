num = int(input("Enter a non-negative integer: "))
factorial = 1

for n in range(1, num + 1):
    factorial = factorial * n
print(f"The factorial is {factorial}")
