username = "student"
password = "python123"
entered_username = input("Enter your username: ")
entered_password = input("Enter your password: ")

# Check login using comparison operators and control flow
if entered_username == username and entered_password == password:
    print("Login successful!")

    score = int(input("Enter your exam score: "))
    bonus = 5

    final_score = score + bonus

    print("Your score after bonus is:", final_score)

    # Control flow with comparison operators
    if final_score >= 70:
        print("Grade: A")
    elif final_score >= 50:
        print("Grade: Pass")
    else:
        print("Grade: Fail")

else:
    print("Incorrect username or password.")