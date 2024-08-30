# Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. 
# However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.
# Your task is to write a function maskify, which changes all but the last four characters into '#'.

user_data = input("Sensitive data is shown here")
def maskify(user_data):
    # Check if the input string length is less than or equal to 4, return it unchanged
    if len(user_data) <= 4:
        return user_data
    
    # Replace all characters except the last four with '#'
    masked_string = '#' * (len(user_data) - 4) + user_data[-4:]
    
    return masked_string
print(maskify(user_data))
    