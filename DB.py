# Импортируем библиотеку, соответствующую типу нашей базы данных
import sqlite3

# Создаем соединение с нашей базой данных
# В нашем примере у нас это просто файл базы
conn = sqlite3.connect('databaseSqlite.db')

# Создаем курсор - это специальный объект который делает запросы и получает их результаты
cursor = conn.cursor()

print("Enter datas")
idd = input("id ")
names = input("name ")
surname = input("surname ")
age =int(input("age "))
logg = input("login ")
passw = input("passw ")


# Делаем INSERT запрос к базе данных, используя обычный SQL-синтаксис
cursor.execute("insert into users values ( '%d','%s','%s','%d', '%s','%s')" % \
                (idd, names, surname, age, logg, passw))

# Если мы не просто читаем, но и вносим изменения в базу данных - необходимо сохранить транзакцию
conn.commit()

# Проверяем результат
cursor.execute("SELECT surname FROM users ORDER BY surname LIMIT 3")
results = cursor.fetchall()
print(results)



