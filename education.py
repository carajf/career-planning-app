import sqlite3

userID = ""

eduTable = "edu_"+userID
usersTable = "users"

def create_table():
    with sqlite3.connect("Users.db") as db:
        cursor = db.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS '+eduTable+'('
                                                            'educationname VARCHAR(20) NOT NULL,'
                                                            'educationlvl VARCHAR(20) NOT NULL,'
                                                            'location VARCHAR(20) NOT NULL,'
                                                            'qualdate VARCHAR(20) NOT NULL,'
                                                            'UNIQUE(educationname));')
    db.commit()


def enter_new_edu(education):
    with sqlite3.connect("Users.db") as db:
        cursor = db.cursor()

    for edu in education:
        cursor.execute(
            "INSERT OR REPLACE INTO "+eduTable+"(educationname, educationlvl, location, qualdate) VALUES (?, ?, ?, ?)", [edu[0], edu[1], edu[2], edu[3]])

    db.commit()


def delete_edu(eduname):
    with sqlite3.connect("Users.db") as db:
        cursor = db.cursor()

    delete_edu = ("DELETE FROM "+eduTable+" WHERE educationname = ?")
    cursor.execute(delete_edu, [eduname])
    db.commit()

def check_edu():
    with sqlite3.connect("Users.db") as db:
        cursor = db.cursor()
    find_edu = ("SELECT educationname FROM "+eduTable)
    cursor.execute(find_edu)
    results = cursor.fetchall()

    return results

def get_education(eduname):
    with sqlite3.connect("Users.db") as db:
        cursor = db.cursor()

    find_education = ("SELECT * FROM "+eduTable+" WHERE educationname = ?")
    cursor.execute(find_education, [eduname])
    results = cursor.fetchall()

    return results


# def welcome_skills(userid):
#     global userID
#     userID = userid
#     print("Welcome! Do you want to create new skill or view existing skills?")
#     answer = input("1. view skill\n"
#                    "2. new skill\n"
#                    "3. quit\n")
#     if answer == "1":
#         check_skills()
#     elif answer == "2":
#         enter_new_skill()
#     elif answer == "3":
#         print("Bye!")
#         return False
#
