# Example 8: Simple ATM withdrawal
# Objective: Deduct money using while-else.
# Outcome: Prints balance after withdrawals.


balance = 10000.0
withdraw = -1

print("Welcome to Simple ATM, your current balance is: £", balance)

while withdraw != 0:
    withdraw = float(input("Enter amount to withdraw: "))
    if withdraw == 0:
        pass
    elif withdraw < balance:
        balance -= withdraw
        print(f"Withdraw Successful! Your new balance is {balance}")
    else:
        print("Insufficient balance! ")
else:
    print("Thank you for using Simple ATM! Have a good day!")
