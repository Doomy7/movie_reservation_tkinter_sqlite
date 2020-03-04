import sqlite3

def get_movies():
    conn = sqlite3.connect('cinema.db')
    # create cursor
    c = conn.cursor()
    c.execute("SELECT * FROM movies")
    records = c.fetchall()
    return records

def reserveDB(f_name, l_name, age, phone, email, radio):
    conn = sqlite3.connect('cinema.db')
    c = conn.cursor()
    query = ''' INSERT INTO user(first_name,last_name,age,phone, email) VALUES(?, ?, ?, ?, ?) '''
    c.execute(query, [f_name.get(), l_name.get(), age.get(), phone.get(), email.get()])
    conn.commit()
    query = '''Select id from user where email = ? '''
    print(email.get())
    c.execute(query, [email.get()])
    records = c.fetchall()

    if int(age.get()) > 18:
        modifier = 1
    else:
        modifier = 0.5
    query = ''' INSERT INTO reservations VALUES(?, ?, ?) '''
    c.execute(query, [records[0][0], radio.get(), modifier])
    conn.commit()

def reservation(f_name, l_name, age, phone, email, radio):
    if f_name is None or l_name is None or age is None or phone is None or email is None or radio is None:
        pass
    else:
        reserveDB(f_name, l_name, age, phone, email, radio)
