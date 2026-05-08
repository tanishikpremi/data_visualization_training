def calculate_si(principal,rate, time):
    si=principal * rate * time / 100
    amount=principal + si
    return (si,amount)
try:
    P=float(input("Enter Principal amount: "))
    R=float(input("Enter Rate of interest (%): "))
    T=float(input("Enter Time (in years): "))
    SI_v2,Total=calculate_si(P, R, T)
    print("\n----- Result -----")
    print(f'Simple Interest : {SI_v2:.2f}')
    print(f'Total Amount     : {Total:.2f}')
except ValueError:
    print(" Invalid input! Please enter numeric values only.")
