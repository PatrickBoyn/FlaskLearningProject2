# For learning how to use SQLite
import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = 'CREATE TABLE users (id int, username text, password text)'
cursor.execute(create_table)

print('Finished created the table.')

# Creates a new user.
user = (1, 'patrick', 'asdf')

# The question marks will be replaced by the user.
insert_query = 'INSERT INTO users VALUES (?, ?, ?)'

cursor.execute(insert_query, user)

users = [
    (2, 'bob', 'asdf'),
    (3, 'jane', 'asdf'),
    (4, 'george', 'asdf')
]

cursor.executemany(insert_query, users)

connection.commit()

connection.close()

print('Finished creating user.')
