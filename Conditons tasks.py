# Testing conditional programming, IF, ELIF and ELSE statements
letter = input("Choose a letter ")

if letter == "a":
    print("A is for apple")
elif letter == "b":
    print("B is for banana")
elif letter == "c":
    print("C is for cherry")
else:
    print("I don't know that letter")


letter = input("Choose a letter ")

if letter == "a":
    print("Your star sign is Aries.")
elif letter == "t":
    print("Your star sign is Taurus.")
elif letter == "g":
    print("Your star sign is Gemini.")
else:
    print("You were born on the month between July and February.")

# print("Choose a letter")
letter = input("Choose a letter ")
if letter == "a" or letter == "A":
    print("a is for apple")
elif letter == "b" or letter == "B":
    print("B is for banana")
elif letter == "c" or letter == "C":
    print("C is for cherry")
else:
    print("I don't know that letter")

# print("Choose a letter")
letter = input("Choose a letter ")
if letter == "a" or letter == "A":
    print("a is for apple")
elif letter == "b" or letter == "B":
   print("B is for banana")
elif letter == "c" or letter == "C":
   print("C is for cherry")
else:
   print("I don't know that letter")

user_integer = int(input("Enter a number:"))

if user_integer == 5:
    print("It's the number 5")
elif user_integer < 5:
    print("It's less than 5")
elif user_integer >= 5:
    print("More than or equal to 5")
else:
    print("Not number 5")

# Advanced challenge
# Simple test for birthday
birthday = input("Enter your birthday month: ")

if birthday == "December" or birthday == "december":
    print("Happy birthday!")
elif birthday == "November" or birthday == "november":
    print("It will be your birthday soon!")
else:
    print("It's not your birthday.")

# Error handling task and conditional color guessing
try: 
    colour = int(input("Guess my favourite colour: 1-4: "))
except:
    print("Please select a numeric value between 1-4.")
    quit()

if colour == 1:
    print("You have guessed Red")
elif colour == 2:
    print("You have guessed Blue")
elif colour == 3:
    print("You have guessed Green")
elif colour == 4:
    print("You have guessed Yellow")
else:
    print("Please select options 1-4")
# if the user enters an incorrect option what happens and make sure to validate the user input and prompt them to make another selection (else block)   

# While True loops 
while True:
    try:
        num1 = int(input("Pick a number: "))
        if num1 < 0:
            print("Try again, positive numbers only.")
            continue
        num2 = int(input("Pick another number: "))
        results = num1 + num2
        print(f"I will give you the sum of both numbers, which is {results}.")
        break
    except ValueError:
        print("That is not a valid number, please try again.")


# Creating a list of numbers provided by the user and the length of the list is determined by the user
while True:
    user_input = input("Enter a number or write done to stop. ").lower()
    list_of_values = []
    try:
        first_value = float(user_input)
        if first_value < 0:
            print("Try again, positive numbers only.")
            continue
        elif first_value is not None:
            additional_input = float(input("Enter another number or select done to stop."))
            list_of_values.append(first_value)
            if str(additional_input) == "done":
                break
        else:
            user_input == "done"
            break
            
        add_num = float(input("Pick another number: "))
        sum = add_num + list_of_values
        print(f"I will give you the sum of numbers, which is {sum}.")
        break
    except ValueError:
        print("That is not a valid number, please try again.")