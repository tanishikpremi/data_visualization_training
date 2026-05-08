
cart_value = float(input("Enter total cart value: ₹"))
membership = input("Enter membership (Silver/Gold/Platinum/None): ").lower()
festival = input("Is it festival season? (yes/no): ").lower()

member_discount = 0
festival_discount = 0


if membership == "platinum":
    member_discount = 15
elif membership == "gold":
    member_discount = 10
elif membership == "silver":
    member_discount = 5

# Assigning a dummy festival discount
if festival == "yes":
    festival_discount = 12


highest_discount = max(member_discount, festival_discount)

discount_amount = (highest_discount / 100) * cart_value
payable_amount = cart_value - discount_amount

print("\n--- Bill Details ---")
print("Highest Discount Applied:", highest_discount, "%")
print("Discount Amount: ₹", discount_amount)
print("Final Payable Amount: ₹", payable_amount)