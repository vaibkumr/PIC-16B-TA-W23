import sqlite3

def printall(cur):
    result = cur.execute("SELECT * FROM students")
    print("Printing all records...")
    records = result.fetchall()
    for record in records:
        print(record)

con = sqlite3.connect("university.db")
cur = con.cursor()
printall(cur)

# +++++++++++++++++++ Not a threat +++++++++++++++++++
# id = 3
# username = "Kai-Wei"
# grade = 10
# query = f"INSERT INTO students VALUES ({id}, '{username}', {grade});"
# print(f"Executing the query: {query}")
# cur.executescript(query)
# printall(cur)


# +++++++++++++++++++ Threat +++++++++++++++++++
# id = 4
# username = "Dr. Heinz Doofenshmirtz"
# grade = "0); drop table students; INSERT INTO students VALUES (100, evil, 1"

# query = f"INSERT INTO students VALUES ({id}, '{username}', {grade});"
# print(f"Executing the query: {query}")
# cur.executescript(query)
# printall(cur)


# +++++++++++++++++++ Threat Safe Code +++++++++++++++++++
id = 4
username = "Dr. Heinz Doofenshmirtz"
grade = "0); drop table students; INSERT INTO students VALUES (100, evil, 1"
query = f"INSERT INTO students VALUES ({id}, '{username}', {grade});"
cur.execute("INSERT INTO students VALUES (?, ?, ?);", (id, username, grade))
printall(cur)
