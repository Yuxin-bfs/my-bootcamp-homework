# Example 9: Skip numbers divisible by 3
# Objective: Use if inside for-else to skip certain numbers.
# Outcome: Prints numbers 1–10 except multiples of 3.

for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i)
else:
    print("Done")
