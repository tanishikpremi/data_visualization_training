# Q32. Write a Python program that validates user age for voting eligibility 
# and handles invalid numeric and non-numeric inputs gracefully.

def check_voting_eligibility(age_input):
    try:
        age = int(age_input)
        if age < 0:
            print("Age cannot be negative.")
        elif age >= 18:
            print("Eligible to vote.")
        else:
            print(f"Not eligible. Wait {18 - age} more year(s).")
    except ValueError:
        print("Invalid input! Please enter a valid numeric age.")

if __name__ == "__main__":
    inputs = ["20", "15", "-5", "twenty"]
    for i in inputs:
        print(f"Input: {i}")
        check_voting_eligibility(i)
        print()

# Expected Output:
# Input: 20
# Eligible to vote.
# 
# Input: 15
# Not eligible. Wait 3 more year(s).
# 
# Input: -5
# Age cannot be negative.
# 
# Input: twenty
# Invalid input! Please enter a valid numeric age.
