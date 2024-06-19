import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Получаем средний возраст пользователей для каждого возраста
cursor.execute('SELECT age, AVG(age) FROM Users GROUP BY age')
results = cursor.fetchall()

for row in results:
    print(row)

# Фильтруем группы по среднему возрасту больше 30
cursor.execute('SELECT age, AVG(age) FROM Users GROUP BY age HAVING AVG(age) > ?', (30,))
filtered_results = cursor.fetchall()
for row in filtered_results:
    print(row)

connection.close()
