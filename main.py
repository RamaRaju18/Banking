def account_no():
    acc = ("******")
    user = (int(input("Enter Your 6 Digit Account Number:")))
    Acc = str(user)
    if len(Acc) == len(acc):
        return user
    else:
        print("Enter Valid Account Number")
        return account_no()
def show_balance():
    print(f"Your Balance Is: Rs {balance:.2f}")
    return balance
def deposit():
    amount = float(input("Enter Your Amount:"))
    if amount < 0:
        print("Enter Valid Amount:")
        return 0
    else:
        print("Your Deposit Is Successfull")
        return amount
def withdraw():
    amount = float(input("Enter Your Amount:"))
    if amount > balance:
        print("Insufficient Funds")
        return 0
    elif amount < 0 :
        print("Enter Valid Amount")
        return 0
    else:
        print("Your Withdrawl Is Successfull")
        return amount
balance = 0
Banking = True
print(account_no())
while Banking:
        print("Banking")
        print("1.Balance Enquiry")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        Choice = int(input("Enter Your Number:"))
        if Choice == 1:
            balance = show_balance()
        elif Choice == 2:
            balance += deposit()
        elif Choice == 3:
            balance -= withdraw()
        elif Choice == 4:
            Banking = False
        else:
            print("Enter valid Number")
print("Thank You For Banking With Us")
