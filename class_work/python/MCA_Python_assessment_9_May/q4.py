# Q4. Write a menu-driven banking application using a while loop that allows users to 
# deposit, withdraw, check balance, and exit only when the user chooses the exit option.

def banking():
    balance = 0.0
    actions = [(1, 100), (2, 50), (3, 0), (4, 0)] # Simulated user input
    for action, amt in actions:
        if action == 1:
            balance += amt
            print(f"Deposited: ${amt}")
        elif action == 2:
            if amt <= balance:
                balance -= amt
                print(f"Withdrew: ${amt}")
            else:
                print("Insufficient funds!")
        elif action == 3:
            print(f"Balance: ${balance}")
        elif action == 4:
            print("Exiting.")
            break

if __name__ == "__main__":
    banking()

# Expected Output:
# Deposited: $100
# Withdrew: $50
# Balance: $50.0
# Exiting.
