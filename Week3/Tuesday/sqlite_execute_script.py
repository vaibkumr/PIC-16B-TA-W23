import sqlite3

def printall(cur):
    result = cur.execute("SELECT * FROM students")
    print("Printing all records...")
    records = result.fetchall()
    for record in records:
        print(record)

con = sqlite3.connect("university.db")
cur = con.cursor()

script = """
    CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    gender TEXT NOT NULL
    );
    INSERT INTO students VALUES (1, 'Ryan', 'M');
    INSERT INTO students VALUES (2, 'Joanna', 'F');
"""

result = cur.executescript(script)
printall(cur)

con.commit()
con.close()