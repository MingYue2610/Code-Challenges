# Writing a program to tick items off a shopping list
shopping_list = ["apple", "banana", "rice", "pasta", "milk", "bread"]
print(shopping_list)
while shopping_list:
    choice = input("Check items off the shopping list, or '0' to exit: ").lower()
    
    if choice == '0':
        print("Exiting...")
        break
    elif choice in shopping_list:
        shopping_list.remove(choice)
        print(f"Removed: {choice}")
        print(shopping_list)
    else:
        print("Item not found in the list. Please try again.")

if not shopping_list:
    print("Your shopping list is now empty.")
