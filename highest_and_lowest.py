# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
# Example high_and_low("1 2 3 4 5")  # return "5 1"
# Example high_and_low("1 2 -3 4 5") # return "5 -3"
# Example high_and_low("1 9 3 4 -5") # return "9 -5"

# This function high_and_low takes a string of space-separated numbers as input, finds the highest and lowest numbers in that string, and returns a string containing these two numbers with the highest number first.
def high_and_low(numbers): 
    nums = sorted(numbers.split(), key=int) # Split() seprates each integer into a subset which will then be sorted in ascending order with key referring to them as integers and not string
    return '{} {}'.format(nums[-1], nums[0]) # .format() will use the braces {} as keyholder for our argument value of [-1] last integer of the list aka the highest and [0] being the the first and lowest number