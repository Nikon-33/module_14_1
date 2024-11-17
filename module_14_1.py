import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NUll,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

# cursor.execute("DELETE FROM Users WHERE id > ?", ("0",))

for i in range(1, 11):
    age = 10 * i
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f'User{i}', f'example{i}@gmail.com', f'{age}', f'1000'))

for i in range(1, 10, 2):
    cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", ("500", f'{i}'))

for i in range(1, 11, 3):
    cursor.execute("DELETE FROM Users WHERE id = ?", (f'{i}',))

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
users = cursor.fetchall()

for user in users:
    username, email, age, balance = user
    print(f'Имя: {username} | Почта: {email}, | Возраст: {age}, | Баланс: {balance}')

connection.commit()
connection.close()
