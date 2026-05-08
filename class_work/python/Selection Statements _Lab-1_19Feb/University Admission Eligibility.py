
percent_12th = float(input("Enter 12th grade percentage: "))
studied_math = input("Did you study Mathematics? (yes/no): ").lower()
entrance_score = float(input("Enter entrance exam score: "))


is_eligible = True

print("\n--- Eligibility Status ---")

if percent_12th < 75:
    print("Rejection Reason: Minimum 75% in 12th grade is required.")
    is_eligible = False

if studied_math != "yes":
    print("Rejection Reason: Must have studied Mathematics.")
    is_eligible = False

if entrance_score < 80:
    print("Rejection Reason: Entrance exam score is below 80.")
    is_eligible = False


if is_eligible:
    print("Congratulations! You are fully eligible for admission.")