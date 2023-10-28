import sqlite3 as sq

with sq.connect('super.db') as conn:
    cur = conn.cursor()
    # cur.execute('''DROP TABLE user ''')
    cur.execute('''CREATE TABLE IF NOT EXISTS user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    gender BOOLEAN NOT NULL,
    age INTEGER,
    title TEXT
    )''')
    # cur.execute('''INSERT INTO user (name,gender,age,title) VALUES ('baka',1,12,'gherfj')''')
    cur.execute('''UPDATE user SET name="бee" Where id==1''')
    cur.execute('''DELETE FROM user WHERE id==2''')
    cur.execute(''' SELECT * FROM user''')
    item=cur.fetchall()
    for i in item:
        print(i)