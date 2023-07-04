import sqlite3

con = sqlite3.connect('emaildb.sqlite')
db = con.cursor()

db.execute('DROP TABLE IF EXISTS Counts')
db.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')

fname = input('nome do arquivo: ')
if len(fname) < 1:
    fname = 'mbox-short.txt'
fh = open(fname)

for line in fh:
    if not line.startswith('From: '):
        continue
    words = line.split()
    email = words[1]

    # essa linha é como se eu tivesse abrindo o arquivo na linha desejada, sem ela o retorno de fetchone será sempre None
    db.execute('SELECT count FROM Counts WHERE email = ?', (email,))

    # retorna apenas uma linha da tabela (a primeira) em formato de tupla!
    row = db.fetchone()

    # '(email,)' é uma tupla de um elemento
    # Contagem de cada email no arquivo
    if row is None:
        db.execute('INSERT INTO Counts (email, count) VALUES (?, 1)', (email,))
    else:
        db.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))
    con.commit()

# SELECT retorna um iterável
sqlstr = db.execute('SELECT * FROM Counts ORDER BY count DESC')

for row in sqlstr:
    print(row)

db.close()
