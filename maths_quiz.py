# Writing a program to perform multiple arithmetic operations from the user input with a score tracker
print("Welcome to the Maths Quiz!")
print("Please select an option...")
print("1 - Addition")
print("2 - Multiplcation")
print("3 - Subtraction")
print("4 - Division")
print("5 - Check score")
print("0 - Exit")

try:
    score = 0
    while True:
        user = int(input("Enter a number between 0 and 5: ")) # ask the user to input a integer between 0-5
        if user == 1:   # if 1 is selected, prompt the addition question
            while True: #this will loop the question until the user gets it right
                addition = int(input("What is 3+5? "))
                if addition == 8:
                    print("That is correct.")
                    score += 1
                    break
                else:
                    print("Try again.")

        elif user == 2:
            while True:
                multiplication = int(input("What is 2x3? "))
                if multiplication == 6:
                    print("That is correct.")
                    score += 1
                    break
                else:
                    print("Try again.")
        elif user == 3:
            while True:
                subtraction = int(input("What is 10-3? "))
                if subtraction == 7:
                    print("That is correct.")
                    score += 1
                    break
                else:
                    print("Try again.")
        elif user == 4:
            while True:
                division = int(input("What is 42/7? "))
                if division == 6:
                    print("That is correct.")
                    score += 1
                    break
                else:
                    print("Try again.")
        elif user == 5:
            print("Current score:",score)
        elif user < 0 or user > 5:
            print("Please try again, choose an number between 0 and 5.")
        else:
            user == 0
            print("Exiting.")
            break
except ValueError:
    print("Incorrect input, choose an number between 0 and 5.")
print(f"Session has ended, your final score was {score}.")