heart_rate_abnormal = input("Is heart rate abnormal? (yes/no): ").strip().lower() == 'yes'
severe_injury = input("Is there a severe injury? (yes/no): ").strip().lower() == 'yes'
age = int(input("Enter patient's age: "))

condition = "Normal"

if heart_rate_abnormal or severe_injury:
    condition = "Critical"
else:
    is_moderate = input("Is the condition moderate? (yes/no): ").strip().lower() == 'yes'
    if is_moderate:
        condition = "Moderate"

if age > 65 and condition == "Moderate":
    condition = "Critical"

print(f"Patient Priority: {condition}")