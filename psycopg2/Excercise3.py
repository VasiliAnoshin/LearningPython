import psycopg2

connection = psycopg2.connect('dbname=jane')

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS table2;')

cursor.execute('''
    CREATE TABLE table2 (
    id INTEGER PRIMARY KEY,
    completed BOOLEAN NOT NULL DEFAULT False
  );
''')

cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (1, True))

SQL = 'INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);'

data = {
  'id': 2,
  'completed': False
}
cursor.execute(SQL, data)

#3 Fetch results from your first created record to create a new record, slightly modified.
cursor.execute('SELECT * from table2;')
result = cursor.fetchone()
cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (result[0] + 50, result[1] == False))

#4 Fetch all of the rows from the table, and print each item line-by-line using a loop.
cursor.execute('SELECT * from table2;')
result = cursor.fetchall()
for x in result: 
    print(x)


connection.commit()
connection.close()
cursor.close()
