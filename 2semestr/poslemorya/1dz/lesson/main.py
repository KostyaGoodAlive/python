import sqlite3 


def create_table(name):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name VARCHAR NOT NULL , password VArCHAR NOT NULL)""")
    connection.commit()
    connection.close()


def add_data(name, password):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO users (name , password) VALUES (?,?); """,(name, password))
    connection.commit()
    connection.close()


connection = sqlite3.connect('database.db')
cursor = connection.cursor()
cursor.execute("""SELECT * FROM users; """)
connection.close()


