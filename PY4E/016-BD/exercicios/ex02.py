import sqlite3
import re

conn = sqlite3.connect('orgdb.sqlite')
db = conn.cursor()

# deletando a tabela e criando uma nova a cada execução
db.execute('DROP TABLE IF EXISTS Counts')
db.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

# abrindo o arquivo
fname = input('Enter file name: ')
if (len(fname) < 1):
    fname = 'mbox.txt'
fh = open(fname)

for line in fh:
    if not line.startswith('From: '):
        continue
    line = line.strip()
    email = re.search(r'^From: .+@(.+)$', line)
    org = email.group(1)

    # 'abrindo o arquivo de banco de dados'
    db.execute('SELECT count FROM Counts WHERE org = ? ', (org,))

    # fetchone retorna uma linha (row) com várias tabelas (tupla)
    row = db.fetchone()

    if row is None:
        db.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        db.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
    # o 'commit()' fora do loop pode agilizar o processo
    conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in db.execute(sqlstr):
    print(row)

db.close()