import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Нахождение максимального возраста
cursor.execute('SELECT MAX(age) FROM Users')
max_age = cursor.fetchone()[0]

print('Максимальный возраст среди пользователей:', max_age)
connection.close()
