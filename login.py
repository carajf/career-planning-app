# MODULE CREATED TO MANAGE USERS IN USERS DATABASE
# HOW TO USE:
# in the main program "import login as login"
# to use any function type login.[name_of_function]([parameters])
# example login.enter_new_user("John", "JJ_Joker", "123456") -> Creates user with name John, username JJ_Joker and
# password 123456


import sqlite3

quitApp = False

usersTable = "users"


def create_table():
    with sqlite3.connect("Users.db") as db:
        cursor = db.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS '''+usersTable+'''(
    userID INTEGER PRIMARY KEY,
    username VARCHAR(20) NOT NULL, 
    firstname VARCHAR(20) NOT NULL,
    password VARCHAR(20) NOT NULL,
    UNIQUE(firstname),
    UNIQUE(password));
    ''')
    db.commit()


# Create new user, just call from different function including name, username and password for the new entry
def enter_new_user(firstname, username, password):
    with sqlite3.connect("Users.db") as db:
        cursor = db.cursor()

    sql = ("INSERT OR REPLACE INTO users(username, firstname, password) VALUES(?, ?, ?)")
    cursor.execute(sql, [username, firstname, password])
    db.commit()


# log the user in, it will check if password and username match any combination recorded in database (Users.db)
def login(username, password):
    with sqlite3.connect("Users.db") as db:
        cursor = db.cursor()
    fund_user = ("SELECT * FROM "+usersTable+" WHERE firstname = ? AND password = ?")
    cursor.execute(fund_user, [username, password])
    results = cursor.fetchall()

    if results:
        return True
    else:
        return False


# delete user from the database (password is required to authorise deletion)
def delete_user(username, password):
    with sqlite3.connect("Users.db") as db:
        cursor = db.cursor()
    delete_user = ("DELETE FROM "+usersTable+" WHERE firstname = ? AND password = ?")
    cursor.execute(delete_user, [username, password])
    db.commit()
    print("User "+username+" has been removed")


# Get the list of all users in the database
def get_usr_list():
    with sqlite3.connect("Users.db") as db:
        cursor = db.cursor()

    listUsers = ("SELECT firstname FROM "+usersTable)
    cursor.execute(listUsers)
    results = cursor.fetchall()
    return results

# get single user data
def get_user(userID):
    with sqlite3.connect("Users.db") as db:
        cursor = db.cursor()

    cursor.execute("SELECT * FROM "+usersTable+" WHERE firstname = ?", [userID])
    return cursor.fetchall()


# Funciton used for debugging, can be called to test all below fuctions
# def welcome():
#     global quitApp
#     print("Welcome! Do you want to log in or register?")
#     answer = input("1. existing user\n"
#                    "2. new user\n"
#                    "3. delete user\n"
#                    "4. quit\n")
#     if answer == "1":
#         username = input("Username please: ")
#         password = input("Pass: ")
#         print(login(username, password))
#
#     elif answer == "2":
#         username = input("username? \n")
#         password = input("password? \n")
#         firstname = input("first name? \n")
#         enter_new_user(firstname, username, password)
#     elif answer == "3":
#         username = input("Username please: ")
#         password = input("Pass: ")
#         delete_user(username, password)
#     elif answer == "4":
#         print("Bye!")
#         quit()
#
#
# welcome()