# Testing list and methods
films = [
    "Forrest Gump", 
    "Lord of the Rings", 
    "Avengers"]
print(films)

fruits = [
    "apple",
    "banana",
    "coconut",
    "orange",
    "grape",
    "pear",
    "strawberry",
    "cherry",
    "kiwi",
    "pineapple"
]
fruits.count("banana")
print(fruits.count("banana"))

string1 = "Hello world"
print(string1[4])

# list of movies task
favourite_movies = [] 
user_input = input("Enter your favourite movies. ")
favourite_movies.append(user_input)
print(favourite_movies)
total_movies = len(favourite_movies)
print(total_movies)
print(favourite_movies[1-3])

favourite_movies = []
while True:
    user_input = input("Enter your favorite movie (or type 'done' to finish): ")
    if user_input.lower() == 'done':
        break
    favourite_movies.append(user_input)
    print("Your favorite movies so far:", favourite_movies)
total_movies = len(favourite_movies)
print(f"\nYou have entered {total_movies} movies.")
print("Your complete list of favorite movies:", favourite_movies)

# Write program for 2 times table
for num in range (13):
    num = 2*num
    print(num)

times_table = int(input("What times would you like to be printed? "))
for times_table in range(1, 13):
    print(f"\n{times_table} Times Table:")
    for number in range (1,13):
        results = times_table * number
        print(f"{times_table} x {number} = {results}")

# For loops count control iteration
for num in range(5): this will loop 5 times
for num in range(1,11): this wil loop from 1, not including 11
for num in range(1,101,5): this will loop from 1, in increments of 5 but not including 101, up to 100 here 

# Creating a program that allows the user to have 3 tries at guessing the password "pineapple"
password = "pineapple"
attempts = 0
while attempts < 3:
    user_guess = input(f"Please guess the password. You have {3 - attempts} attempts remaining.\n").lower()
    if user_guess == password:
        print("You have guessed correctly!")
        break
    else:
        attempts += 1
        if attempts < 3:
            print(f"You have guessed incorrectly, please try again.")
        else:
            print("You have guessed incorrectly! You have used all your attempts.")
print("Hope you had fun.")

