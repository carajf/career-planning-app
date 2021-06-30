import sqlite3


userID = ""
jobTable = "action_plan"
usersTable = "users"


def create_table():
    with sqlite3.connect("Users.db") as db:
        cursor = db.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS '+jobTable+'('
                                                            'task VARCHAR(20) NOT NULL,'
                                                            'category VARCHAR(20) NOT NULL,'
                                                            'progress VARCHAR(20),'
                                                            'duedate VARCHAR(20),'
                                                            'comments TEXT);')
    db.commit()


def save_table(table):
    with sqlite3.connect("Users.db") as db:
        cursor = db.cursor()

    cursor.execute("DELETE FROM "+jobTable+";")
    db.commit()

    for job in table:
        cursor.execute(
            "INSERT INTO "+jobTable+"(task, category, progress, duedate, comments) VALUES (?, ?, ?, ?, ?)", [job[0], job[1], job[2], job[3], job[4]])
        db.commit()

def load_table():
    with sqlite3.connect("Users.db") as db:
        cursor = db.cursor()
    cursor.execute("SELECT * FROM "+jobTable)
    return cursor.fetchall()

