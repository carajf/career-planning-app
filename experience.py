import sqlite3

userID = ""

workTable = "work_"+userID

def create_table():
    with sqlite3.connect("Users.db") as db:
        cursor = db.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS '+workTable+'('
                                                            'jobtitle VARCHAR(20) NOT NULL,'
                                                            'jobdesc TEXT NOT NULL,'
                                                            'salary VARCHAR(20) NOT NULL,'
                                                            'startdate VARCHAR(20) NOT NULL,'
                                                            'enddate VARCHAR(20) NOT NULL,'
                                                            'location VARCHAR(20) NOT NULL,'
                                                            'UNIQUE(jobtitle));')
    db.commit()


def enter_new_work(work_exp):
    with sqlite3.connect("Users.db") as db:
        cursor = db.cursor()

    for work in work_exp:
        cursor.execute(
            "INSERT OR REPLACE INTO "+workTable+"(jobtitle, jobdesc, salary, startdate, enddate, location) VALUES (?, ?, ?, ?, ?, ?)", [work[0], work[1], work[2], work[3], work[4], work[5]])

    db.commit()


def delete_work(job_title):
    with sqlite3.connect("Users.db") as db:
        cursor = db.cursor()

    delete_works = ("DELETE FROM "+workTable+" WHERE jobtitle = ?")
    cursor.execute(delete_works, [job_title])


def check_work_exp():
    with sqlite3.connect("Users.db") as db:
        cursor = db.cursor()
    find_work = ("SELECT jobtitle FROM "+workTable)
    cursor.execute(find_work)
    results = cursor.fetchall()

    return results

def get_exp(jobtitle):
    with sqlite3.connect("Users.db") as db:
        cursor = db.cursor()

    find_exp = ("SELECT * FROM "+workTable+" WHERE jobtitle = ?")
    cursor.execute(find_exp, [jobtitle])
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
