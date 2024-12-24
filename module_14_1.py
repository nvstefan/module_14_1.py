#Домашнее задание по теме
# "Создание БД, добавление, выбор и удаление элементов."

#Задача "Первые пользователи":

import sqlite3

# Подключение к базе данных
connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

# Создание таблицы Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL)
''')

# Заполнение таблицы 10-ю записями
users_data = [
    ('User1', 'example1@gmail.com', 10, 1000),
    ('User2', 'example2@gmail.com', 20, 1000),
    ('User3', 'example3@gmail.com', 30, 1000),
    ('User4', 'example4@gmail.com', 40, 1000),
    ('User5', 'example5@gmail.com', 50, 1000),
    ('User6', 'example6@gmail.com', 60, 1000),
    ('User7', 'example7@gmail.com', 70, 1000),
    ('User8', 'example8@gmail.com', 80, 1000),
    ('User9', 'example9@gmail.com', 90, 1000),
    ('User10', 'example10@gmail.com', 100, 1000)
]

cursor.executemany('''INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)''', users_data)

# Обновление баланса для каждой второй записи начиная с первой
cursor.execute('''
UPDATE Users
SET balance = 500
WHERE id % 2 == 1
''')

# Удаление каждой третьей записи начиная с первой
cursor.execute('''
DELETE FROM Users
WHERE id % 3 == 1
''')

# Выборка всех записей, кроме тех, у кого возраст 60
cursor.execute('''
SELECT username, email, age, balance
FROM Users
WHERE age != 60
''')

# Получаем все результаты выборки
results = cursor.fetchall()

# Выводим данные в нужном формате
for row in results:
    print(f'Имя: {row[0]} | Почта: {row[1]} | Возраст: {row[2]} | Баланс: {row[3]}')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()