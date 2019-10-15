import sqlite3

database = "database.db"

def create_database():
    con = sqlite3.connect(database)
    cursor = con.cursor()
    sql = "drop table if exists publication"
    cursor.execute(sql)
    sql = "create table publication(title text, link text, author text, date text, responses integer, visits integer)"
    cursor.execute(sql)
    return con

def get_db_connection():
    con = sqlite3.connect(database)
    return con