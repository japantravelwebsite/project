import pandas as pd
import sqlite3


# Read csv file.
df = pd.read_csv("data.csv")

# Connect to (create) database.
database = "db.sqlite3"
conn = sqlite3.connect(database)
dtype={
    "number": "IntegerField",
    "content": "CharField",
    "location": "CharField", 
    "people": "CharField"
}
df.to_sql(name='users_book', con=conn, if_exists='replace', dtype=dtype, index=True, index_label="id")
conn.close()