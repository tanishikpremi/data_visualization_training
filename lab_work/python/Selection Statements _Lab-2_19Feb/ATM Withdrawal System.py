account_balance = 100000 
atm_cash_available = 200000 
withdrawal_amount = float(input("Enter amount to withdraw: "))

if withdrawal_amount > 50000:
    print("Transaction failed: Daily withdrawal limit is ₹50,000.")
elif withdrawal_amount > account_balance:
    print("Transaction failed: Insufficient account balance.")
elif withdrawal_amount > atm_cash_available:
    print("Transaction failed: ATM does not have enough cash.")
else:
    account_balance -= withdrawal_amount
    print(f"Transaction successful. Please collect ₹{withdrawal_amount:.2f}.")