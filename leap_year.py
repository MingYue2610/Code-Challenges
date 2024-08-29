# Write a program that takes a year as input from the user and determines if it is a leap year. A leap year is divisible by 4, but if it is divisible by 100, it should also be divisible by 400
year = int(input("Enter a year: "))

# Check if the year is a leap year
if (year % 4 == 0) or (year % 100 != 0 and year % 400 == 0):
    print("This is a leap year.")
else:
    print("This is not a leap year.")


    

 




