# Write a program that takes three numbers as input from the user and prints the biggest of the three
try:
    user_input = []
    for i in range(3):
         attempts = float(input("Enter a number: "))
         user_input.append(attempts)
except:
    print("Please try again with a numerical value.")
else:
    print("the biggest number is:", max(user_input))