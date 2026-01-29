# Objective: Count how many times 3 appears.
# Outcome: Prints "3 appears 2 times."

a_list = [1, 2, 3, 4, 3]
count_of_threes = 0

for number in a_list:
    if number == 3:
        count_of_threes += 1

print(f"3 appears {count_of_threes} times.")
