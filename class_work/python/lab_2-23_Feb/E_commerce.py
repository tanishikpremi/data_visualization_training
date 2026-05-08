def process_cart(cart):
    # Remove duplicate items
    unique_cart = list(set(cart))
    
    # Calculate initial total
    total = sum(unique_cart)
    
    # Apply 10% discount if total > 5000
    if total > 5000:
        total *= 0.90
        
    # Add GST 18%
    total *= 1.18
    
    print(f"Unique Items: {unique_cart}")
    print(f"Final Payable Amount: ₹{total:.2f}")

# Test
process_cart([1200, 2500, 1200, 3000, 500])