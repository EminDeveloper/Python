import sqlite3

# Устанавливаем соединение с базой данных
with sqlite3.connect('my_database.db') as connection:
    cursor = connection.cursor()

    try:
        # Начинаем транзакцию автоматически
        with connection:
            # Выполняем операции
            cursor.execute('INSERT INTO Users (username, email) VALUES (?, ?)', ('user3', 'user3@example.com'))
            cursor.execute('INSERT INTO Users (username, email) VALUES (?, ?)', ('user4', 'user4@example.com'))

    except:
        # Ошибки будут приводить к автоматическому откату транзакции
        pass
