import sqlite3

con = sqlite3.connect("product.db")
print("Database opened successfully")

con.execute(
  "create table Orders (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, product TEXT NOT NULL, price TEXT NOT NULL)"
)

print("Table created successfully")

con.close()
