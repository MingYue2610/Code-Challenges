# Write a program that takes a number as input from the user and prints whether the number is positive or negative or zero
try:
    user_input = float(input("Enter a numerical value. "))
    if user_input > 0:
        print("The number is positive.")
    elif user_input < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")
except:
    print("You must enter a numerical value.")