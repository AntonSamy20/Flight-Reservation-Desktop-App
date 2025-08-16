import sqlite3
def get_connection():
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    return conn, cursor

def create_user_table():
    con, cursor = get_connection()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL) 
    """)
    con.commit()
    con.close()
    
def create_flights_table():
    con, cursor = get_connection()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS flights (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        passenger_name TEXT NOT NULL,
        flight_number TEXT NOT NULL,
        departure TEXT NOT NULL,
        destination TEXT NOT NULL,
        date DATE NOT NULL,
        seat_number TEXT NOT NULL)
    """)
    con.commit()
    con.close()
    
def add_user(username, password):
    try:
        con, cursor = get_connection()
        if not check_user(username, password):
            cursor.execute("INSERT INTO users (username,password) values (?,?)",(username, password))
            con.commit()
            con.close()
            return True
        else:
            con.close()
            return False 
    except sqlite3.IntegrityError:
        return False

def check_user(username, password):
    con, cursor = get_connection()
    cursor.execute("SELECT * from users where username = ? and password = ?",(username,password))
    user = cursor.fetchone()
    con.close()
    return user is not None

    

