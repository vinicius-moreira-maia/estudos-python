import sqlite3

con = sqlite3.connect('ex01.sqlite')
db = con.cursor()

db.execute('DROP TABLE IF EXISTS Ages')

db.execute('CREATE TABLE Ages (name VARCHAR(128), age INTEGER)')

db.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Dara', 28))
db.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Tianqi', 31))
db.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Samara', 30))
db.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Forgan', 38))
db.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Zenub', 33))

con.commit()

row = db.execute('SELECT hex(name || age) AS X FROM Ages ORDER BY X LIMIT 1')

for i in row:
    print(i)

db.close()