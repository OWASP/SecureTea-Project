# from typing_extensions import Required
import mysql.connector
from mysql.connector import Error
import pandas


import sqlite3

net_sec = "PASSWD"


con = sqlite3.connect('example.db')
cur = con.cursor()

try:
    # Create table
    cur.execute('''CREATE TABLE users(username text, password text, logged_in text)''')
except sqlite3.OperationalError:
    print("Users table exists. Skipping creation")

# Insert a row of data
cur.execute("INSERT INTO users VALUES ('fox','foxyyy','false')")

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
for row in cur.execute('SELECT * FROM users ORDER BY username'):
        print(row)

user  = "fox"
passwd  = "foxyyy"

for c1 in cur.execute("SELECT EXISTS(SELECT * FROM users WHERE username='" + user + "' AND password='" + passwd + "')"):
    print(c1[0])
sql_query = "UPDATE users SET logged_in = 'true' WHERE username='" + user + "'"
cur.execute(sql_query)
for row in cur.execute('SELECT * FROM users ORDER BY username'):
        print(row)
con.close()
