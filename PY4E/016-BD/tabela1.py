import sqlite3

conexao = sqlite3.connect('music.sqlite')
cursor = conexao.cursor()

# deletar a tabela se ela já existir (só para não dar erro no segundo comando)
cursor.execute('DROP TABLE IF EXISTS Tracks')

# cria a tabela 'Tracks' com as colunas 'title' e 'plays', cada uma com seu tipo de dado
cursor.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')

cursor.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('Thunderstruck', 20))
cursor.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('My Way', 15))

# commit() é para atualizar o arquivo
conexao.commit()

print('Tracks: ')
cursor.execute('SELECT title, plays FROM Tracks')
for row in cursor:
    print(row)

cursor.execute('DELETE FROM Tracks WHERE plays < 100')
conexao.commit()

# nada
print('Tracks: ')
cursor.execute('SELECT * FROM Tracks')
for row in cursor:
    print(row)

cursor.close()