import sqlite3

con = sqlite3.connect("university.db")
cur = con.cursor()

cur.execute("""
    CREATE TABLE students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        grade INTEGER NOT NULL
    );""")

cur.execute("INSERT INTO students VALUES (1, 'Ryan', 9);")
cur.execute("INSERT INTO students VALUES (2, 'Joanna', 8);")

result = cur.execute("SELECT * FROM students WHERE grade = 9;")
record = result.fetchone()
print("Printing one record...")
print(record)


result = cur.execute("SELECT * FROM students")
print("Printing all records...")
records = result.fetchall()
for record in records:
    print(record)

con.commit()
con.close()