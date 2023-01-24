import pandas
import sqlite3

table_name = "iris"
db_file_path = "iris.db"
csv_file_path = "../../Week2/Thursday/data/IRIS.csv"

con = sqlite3.connect(db_file_path)

df = pandas.read_csv(csv_file_path)
df.to_sql(table_name, con, if_exists='append', index=False)

con.close()