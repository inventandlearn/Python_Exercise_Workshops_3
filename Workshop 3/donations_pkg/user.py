def login(database, username, password):
    if (username in database and password == database[username]):
        print("Welcome back " + username + "!")
        return username
    elif (username in database and password != database[username]):
        print("Incorrect password for " + username + "!")
        return ""
    else:
        print("User not found. Please register!")
        return ""

def register(database, username):
    if (username in database):
        print("Username already registered")
        return ""
    else: 
        print("Username " + username + " has successfully been registered!")
        return username


