def deposit():
    print("Enter deposit amount")
    amt = float(input())
    if amt > 0:
        print(amt, " to be deposited")
        return amt
    else:
        print("amount must be greater than 0")
        return 0


def withdraw(current_balance):
    print("Enter withdrawal amount")
    amt = float(input())
    if amt < 0:
        print("amount must be greater than 0")
        return 0
    if amt <= current_balance:
        print(amt, " to be withdrawn")
        return amt
    else:
        print("not enough balance to withdraw ", amt)
        return 0


balance = 0

while True:
    print()
    print("""Enter 
    1 to deposit
    2 to withdraw
    3 to show balance 
    """)
    cmd = int(input())

    if cmd == 1:
        deposit_amount = deposit()
        balance = round(balance + deposit_amount, 2)
        print(deposit_amount, " deposited")
    elif cmd == 2:
        withdraw_amount = withdraw(balance)
        balance = round(balance - withdraw_amount, 2)
        print(withdraw_amount, " withdrawn")
    elif cmd == 3:
        print("Current balance is ", balance)
    else:
        print("Unknown command!")
