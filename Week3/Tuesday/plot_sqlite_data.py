import matplotlib.pyplot as plt
import sqlite3

con = sqlite3.connect("iris.db")
cur = con.cursor()

result = cur.execute("SELECT sepal_length FROM iris")
records = result.fetchall()
sepal_length = [int(r[0]) for r in records]
plt.plot(sepal_length)
plt.show()

con.close()