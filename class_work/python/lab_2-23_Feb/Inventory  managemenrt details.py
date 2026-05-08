def manage_inventory(stock):
    # Remove items with 0 stock
    active_stock = [s for s in stock if s > 0]
    
    # Add restock (add 50 units) to items below 10
    restocked = [s + 50 if s < 10 else s for s in active_stock]
    
    # Find total inventory count
    total_inventory = sum(restocked)
    
    print(f"Updated Stock List: {restocked}")
    print(f"Total Inventory Count: {total_inventory}")

# Test
manage_inventory([5, 0, 25, 8, 0, 100])