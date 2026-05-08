units = float(input("Enter units consumed: "))
is_senior = input("Are you a senior citizen? (yes/no): ").strip().lower()

bill = 0

if units <= 100:
    bill = units * 5
elif units <= 300:
    bill = (100 * 5) + ((units - 100) * 7)
else:
    bill = (100 * 5) + (200 * 7) + ((units - 300) * 10)

if is_senior == 'yes':
    bill -= bill * 0.10

print(f"Total Electricity Bill: ₹{bill:.2f}")