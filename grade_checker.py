# Write a program that takes a score (integer) between 0 and 100 from the user and prints the corresponding grade based on the following scale
try:
    score = float(input("Enter your exam score. "))
    if score >=0 and score <25:
        print("You have achieve a grade D")
    elif score >= 25 and score < 50:
        print("You have achieve a grade C")
    elif score >= 50 and score < 75:
        print("You have achieve a grade B")
    elif score >= 75 and score <= 100:
        print("You have achieve a grade A")
    else:
        print("Please enter positive score.")
except:
    print("Please enter a numerical value between 0-100.")