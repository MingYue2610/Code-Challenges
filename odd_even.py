# Write a program that takes an integer from the user and prints whether the number is odd or even
try:
    user_input = int(input("Enter an integer: "))
    if user_input == 0:
        print("The number is even.")
    elif user_input % 2 == 0:
        print("The number you have entered is even.")
    else:
        print("The number you have entered is odd.")
except:
    print("Enter a positive integer value.")
