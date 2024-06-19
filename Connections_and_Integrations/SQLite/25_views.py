import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

try:
    # Создаем представление для активных пользователей
    cursor.execute('CREATE VIEW IF NOT EXISTS ActiveUsers AS SELECT * FROM Users WHERE is_active = 1')

    # Выбираем активных пользователей
    cursor.execute('SELECT * FROM ActiveUsers')
    active_users = cursor.fetchall()

    # Выводим результаты
    for user in active_users:
        print(user)
except sqlite3.Error as e:
    print(f"An error occurred: {e}")
finally:
    # Закрываем соединение
    connection.close()
