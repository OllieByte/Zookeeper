from animals import animals

def intro():
    print("""I love animals!
Let's check on the animals...
The deer looks fine.
The bat looks happy.
The lion looks healthy.""")

def choice():
    user_input = input("Please enter the number of the habitat you would like to view: ")

    while user_input != "exit":

        if user_input == "0":
            animals[0]()  # Camel
            user_input = input("Please enter the number of the habitat you would like to view: ")

        elif user_input == '1':
            animals[1]()  # Lion
            user_input = input("Please enter the number of the habitat you would like to view: ")

        elif user_input == '2':
            animals[2]()  # Deer
            user_input = input("Please enter the number of the habitat you would like to view: ")

        elif user_input == '3':
            animals[3]()  # Goose
            user_input = input("Please enter the number of the habitat you would like to view: ")

        elif user_input == '4':
            animals[4]()  # Bat
            user_input = input("Please enter the number of the habitat you would like to view: ")

        elif user_input == '5':
            animals[5]()  # Rabbit
            user_input = input("Please enter the number of the habitat you would like to view: ")

        else:
            user_input = input("Please enter the number of the habitat you would like to view: ")
    print("See you later!")

animals = [animals.camel, animals.lion, animals.deer, animals.goose, animals.bat, animals.rabbit]

choice()

