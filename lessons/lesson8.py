import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error:
        print('ошибка на функции create conn')
    return conn


def update_name_age(conn, id, name, age):
    sql = ''' UPDATE student SET fullname=?,age=? WHERE id=?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (name, age, id))
        conn.commit()
    except Error:
        print('ошибка на функции update')


def create_student(conn, student):
    sql = '''INSERT INTO student (fullname,hobby,mark,age,is_working)
    VALUES (?,?,?,?,?)'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, student)
        conn.commit()
    except Error:
        print(Error, 'ошибка на функции create student')


def reed(conn):
    try:
        sql = '''SELECT * FROM student'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()

        for i in rows:
            print(i)
    except Error:
        print('ошибка на функции reed')


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error:
        print('ошибка на функции create conn')

def delete_student1(conn,id):
    sql='''DELETE FROM student WHERE id=?'''
    try:
        cursor=conn.cursor()
        cursor.execute(sql,(id))
        conn.commit()
    except Error:
        print(Error)

def delete_student(conn, id):
    sql = '''DELETE FROM student WHERE id=? '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql,(id,))
        conn.commit()
    except Error as e:
        print(e)

sql_table = '''CREATE TABLE student(
id INTEGER PRIMARY KEY AUTOINCREMENT,
fullname VARCHAR(100) NOT NULL,
hobby TEXT DEFAULT NULL,
mark INTEGER NOT NULL DEFAULT 0,
age DATE not null,
is_working BOOLEAN DEFAULT FALSE
);
'''

database = r'nasa2.db'

connection = create_connection(database)

if connection is not None:
    # create_table(connection, sql_table)
    # create_student(connection,('beka','',9,'2003-00-00',True))
    # create_student(connection,('beka','',9,'2003-00-00',True))
    # create_student(connection,('beka','',9,'2003-00-00',True))
    update_name_age(connection,2,'name','2045-06-06')
    update_name_age(connection,4,'Mark','4444-44-44')
    delete_student(connection,id=3)
    reed(connection)
    print('всё работает')
