cost_price=float(input("Enter the cost price: "))
if cost_price <= 0:
    print("Invalid cost price")
    exit()
else:
    selling_price=float(input("Enter the selling price: "))
    if selling_price <= 0:
        print("Invalid selling price")
        exit()
    elif selling_price > cost_price:
        profit=selling_price - cost_price
        print("Profit =",profit)
    elif cost_price > selling_price:
        loss=cost_price - selling_price
        print("Loss =",loss)
    else:
        print("No profit,No loss")
