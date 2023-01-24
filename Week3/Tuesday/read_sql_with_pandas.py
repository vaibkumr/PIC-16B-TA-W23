import pandas as pd
import sqlite3

db_file_path = "iris.db"
con = sqlite3.connect(db_file_path)


df = pd.read_sql('SELECT * FROM iris', con)
print(df)

con.close()
