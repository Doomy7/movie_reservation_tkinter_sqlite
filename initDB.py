import sqlite3
import os

def create():
    conn = sqlite3.connect('cinema.db')

    # create cursor
    c = conn.cursor()

    # create table
    c.execute("""CREATE TABLE user (
         id integer primary key autoincrement,
         first_name text,
         last_name text,
         age integer,
         phone text,
         email integer
     )
     """)

    c.execute("""CREATE TABLE movies (
             movie_id integer primary key autoincrement,
             movie_name text,
             price float,
             date text
         )
         """)

    c.execute("""CREATE TABLE reservations(
         user_id integer,
         movie_id integer,
         discount float,
         foreign key (user_id) references user(id),
         foreign key (movie_id) references movies(movie_id)
    )
    """)
    query = ''' INSERT INTO movies(movie_name,price,date) VALUES(?, ?, ?) '''
    c.execute(query, ['Smyrna',99.0,'25 Aug 1922'])
    c.execute(query, ['Roman Empire',50.0,'6 Aug 476'])
    c.execute(query, ['Avengers',10.0,'4 Apr 2020'])
    conn.commit()
    return conn

def start():
    if not os.path.isfile("cinema.db"):
        conn = create()
    else:
        conn = sqlite3.connect('cinema.db')
