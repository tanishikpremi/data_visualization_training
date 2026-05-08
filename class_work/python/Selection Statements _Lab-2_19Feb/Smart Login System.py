correct_username = "admin"
correct_password = "password123"
attempts = 0

while attempts < 3:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login successful!")
        break
    else:
        attempts += 1
        print("Invalid credentials.")

if attempts == 3:
    print("Account locked due to 3 failed attempts.")