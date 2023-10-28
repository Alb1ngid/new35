# база данных
# sql
# СУБД-сис управления базами данных
#
# oracle Mysql posgreSQL, NOsql
# sqlite3
# CRUD-create reed update delete

# import sqlite3
#
# db = sqlite3.connect('nasa.db')
#
# c = db.cursor()
#
# c.execute('''CREATE TABLE IF NOT EXISTS user(
# name TEXT,
# age DATE,
# hobby TEXT
# ) ''')
#
# c.execute('''INSERT INTO user VALUES('BEKA','2023-10-2','ertgfvbtfv') ''')
# c.execute('''UPDATE user SET name='Бека' WHERE rowid>1 ''')
# c.execute('''DELETE FROM user WHERE rowid>3''')
# c.execute('''SELECT rowid,* FROM user ''')
# item = c.fetchall()
# for i in item:
#     print(i)
#
# db.commit()
# db.close()
