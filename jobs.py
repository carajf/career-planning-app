import sqlite3

userID = ""

jobTable = "job_"+userID
usersTable = "users"

def create_table():
    with sqlite3.connect("Users.db") as db:
        cursor = db.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS '+jobTable+'('
                                                            'jobtitle VARCHAR(20) NOT NULL,'
                                                            'description TEXT NOT NULL,'
                                                            'company VARCHAR(20),'
                                                            'postdate VARCHAR(20),'
                                                            'deadline VARCHAR(20),'
                                                            'salary VARCHAR(20),'
                                                            'location VARCHAR(20),'
                                                            'skills TEXT,'
                                                            'url TEXT,'
                                                            'UNIQUE(jobtitle));')
    db.commit()


def enter_new_job(job):
    with sqlite3.connect("Users.db") as db:
        cursor = db.cursor()
    cursor.execute(
        "INSERT OR REPLACE INTO "+jobTable+"(jobtitle, description, company, postdate, deadline, salary, location, skills, url) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", [job[0], job[1], job[2], job[3], job[4], job[5], job[6], job[7], job[8]])

    db.commit()


def delete_job(jobtitle):
    with sqlite3.connect("Users.db") as db:
        cursor = db.cursor()

    delete_jobs = ("DELETE FROM "+jobTable+" WHERE jobtitle = ?")
    cursor.execute(delete_jobs, [jobtitle])
    db.commit()


def check_jobs():
    with sqlite3.connect("Users.db") as db:
        cursor = db.cursor()
    find_jobs = ("SELECT jobtitle, company, location, salary, skills, postdate, deadline FROM "+jobTable)
    cursor.execute(find_jobs)
    results = cursor.fetchall()

    return results


def get_job(jobtitle):
    with sqlite3.connect("Users.db") as db:
        cursor = db.cursor()

    find_job = ("SELECT * FROM "+jobTable+" WHERE jobtitle = ?")
    cursor.execute(find_job, [jobtitle])
    results = cursor.fetchall()

    return len(results), results


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
