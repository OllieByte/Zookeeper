
def choice():
    user_input = input("Enter a number here: ")

    while user_input != "exit":
        if user_input == "1":
            print("You entered 1")
            user_input = input("Enter a number here: ")

        elif user_input == "2":
            print("You entered 1")
            user_input = input("Enter a number here: ")
        else:
            user_input = input("Enter a number here: ")


print("Hello you should be prompted to enter a number.")
choice()