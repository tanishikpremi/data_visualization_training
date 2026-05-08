
credit_score = int(input("Enter credit score: "))
monthly_income = float(input("Enter monthly income: ₹"))
existing_loan = float(input("Enter existing loan amount: ₹"))

print("\n--- Loan Status ---")

if credit_score < 600:
    print("Status: Reject")
    print("Reason: Credit score is below 600.")
elif 600 <= credit_score <= 750:
    print("Credit score needs further check...")
  
    if monthly_income < 30000 and existing_loan > 500000:
        print("Status: Reject")
        print("Reason: Income too low relative to existing debt.")
    else:
        print("Status: Approve")
else:
    print("Status: Approve")
    print("Reason: Excellent credit score (above 750).")