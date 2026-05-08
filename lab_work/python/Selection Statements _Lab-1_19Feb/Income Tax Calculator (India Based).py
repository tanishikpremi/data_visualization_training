
age = int(input("Enter your age: "))
income = float(input("Enter your annual income: ₹"))

tax = 0
exemption_limit = 250000


if age >= 60:
    exemption_limit = 300000

if income <= exemption_limit:
    tax = 0
elif income <= 500000:
    tax = (income - exemption_limit) * 0.05
elif income <= 1000000:
    # Tax for the 5% slab + 20% for the rest
    tax_slab_1 = (500000 - exemption_limit) * 0.05
    tax = tax_slab_1 + (income - 500000) * 0.20
else:
    # Tax for 5% slab + 20% slab + 30% for the rest
    tax_slab_1 = (500000 - exemption_limit) * 0.05
    tax_slab_2 = 500000 * 0.20  # 20% on the 5L to 10L bracket
    tax = tax_slab_1 + tax_slab_2 + (income - 1000000) * 0.30

print("Total Income Tax Payable: ₹", tax)