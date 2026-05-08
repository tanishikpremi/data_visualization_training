def analyze_transactions(transactions):
    # Calculate total balance
    balance = sum(transactions)
    
    # Find largest withdrawal (most negative number)
    withdrawals = [t for t in transactions if t < 0]
    largest_withdrawal = min(withdrawals) if withdrawals else 0
    
    # Count number of deposits greater than 10,000
    large_deposits = sum(1 for t in transactions if t > 10000)
    
    print(f"Total Balance: ₹{balance}")
    print(f"Largest Withdrawal: ₹{abs(largest_withdrawal)}")
    print(f"Deposits > ₹10,000: {large_deposits}")

# Test
analyze_transactions([5000, -2000, 15000, -8000, 12000, -500])