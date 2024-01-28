from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register

database = {"admin":"password123"}
donations = []
authorized_user = ""


show_homepage()
if (authorized_user == ""):
    print("You must be logged in to donate!")
else:
    print("Logged in as: " + authorized_user)
while True:
    user_choice = input("Choose an option: ")
    if (user_choice == "1"):
        print("")
        username = input("Enter username: ")
        password = input("Enter password: ")
        print("")
        authorized_user = login(database, username, password)
        show_homepage()
        if (authorized_user == ""):
            print("You must be logged in to donate!")
        else:
            print("Logged in as: " + (authorized_user))
    elif (user_choice == "2"):
        print("")
        username = input("Enter username: ")
        password = input("Enter password: ")
        print("")
        authorized_user = register(database, username)
        if (authorized_user == ""):
            print("You must be logged in to donate!")
        elif (authorized_user != ""):
            database[username] = password
        show_homepage()
    elif (user_choice == "3"):
        if (authorized_user == ""):
            print("You are not logged in!")
        else:
            donation = donate(authorized_user)
            donations.append(donation)
            show_homepage()
            print("Logged in as: " + (authorized_user))
    elif (user_choice == "4"):
        show_donations(donations)
        show_homepage()
        print("Logged in as: " + (authorized_user))
    elif (user_choice == "5"):
        print("Leaving DonateMe...")
        print("Goodbye!")
        print("")
        exit()

