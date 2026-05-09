# Q36. Create an ATM simulation program that repeatedly asks for PIN 
# validation and locks the account after three invalid attempts.

def atm_simulation():
    correct_pin = "1234"
    attempts = 0
    # Simulating inputs: wrong, wrong, correct
    simulated_inputs = ["1111", "2222", "1234"]
    
    for pin in simulated_inputs:
        attempts += 1
        print(f"Attempt {attempts}: Entered PIN '****'")
        if pin == correct_pin:
            print("Access Granted. Welcome!")
            return
        else:
            print("Invalid PIN.")
            
        if attempts == 3:
            print("Account Locked due to 3 invalid attempts.")

if __name__ == "__main__":
    atm_simulation()

# Expected Output:
# Attempt 1: Entered PIN '****'
# Invalid PIN.
# Attempt 2: Entered PIN '****'
# Invalid PIN.
# Attempt 3: Entered PIN '****'
# Access Granted. Welcome!
