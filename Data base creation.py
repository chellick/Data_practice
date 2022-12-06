import sqlite3
conn = sqlite3.connect('Chinook_Sqlite.sqlite')
cursor = conn.cursor()


cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT 3")
results = cursor.fetchall()
results2 =  cursor.fetchall()

print(results)
print(results2)

conn.close()