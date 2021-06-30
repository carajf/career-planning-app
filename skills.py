import sqlite3

userID = ""

skillTable = "skill_"+userID
usersTable = "users"

def create_table():
    with sqlite3.connect("Users.db") as db:
        cursor = db.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS '+skillTable+'('
                                                            'skillname VARCHAR(20) NOT NULL,'
                                                            'description TEXT NOT NULL,'
                                                            'inference INTEGER,'
                                                            'UNIQUE(skillname));')
    db.commit()


def enter_new_skill(skills):
    with sqlite3.connect("Users.db") as db:
        cursor = db.cursor()

    for skill in skills:
        cursor.execute(
            "INSERT OR REPLACE INTO "+skillTable+"(skillname, description, inference) VALUES (?, ?, ?)", [skill[0], skill[1], skill[2]])

    db.commit()

def delete_skill(skillname):
    with sqlite3.connect("Users.db") as db:
        cursor = db.cursor()

    delete_skill = ("DELETE FROM "+skillTable+" WHERE skillname = ?")
    cursor.execute(delete_skill, [skillname])
    db.commit()

def check_skills():
    with sqlite3.connect("Users.db") as db:
        cursor = db.cursor()
    find_skill = ("SELECT skillname FROM "+skillTable)
    cursor.execute(find_skill)
    results = cursor.fetchall()

    return results

def get_skill(skillname):
    with sqlite3.connect("Users.db") as db:
        cursor = db.cursor()

    find_skill = ("SELECT * FROM "+skillTable+" WHERE skillname = ?")
    cursor.execute(find_skill, [skillname])
    results = cursor.fetchall()

    return results

