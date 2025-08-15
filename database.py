import sqlite3
con = sqlite3.connect("flights.db")
cursor = con.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS flights (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        passenger_name TEXT NOT NULL,
        flight_number INT NOT NULL,
        departure TEXT NOT NULL,
        destination TEXT NOT NULL,
        date DATE NOT NULL,
        seat_number INT NOT NULL
    )
""")
con.commit()
con.close()
