import sqlite3

conn = sqlite3.connect("ecom.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL,
    quantity INTEGER
)
""")

cursor.executemany("INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)", [
    ("Laptop", 1000.0, 10),
    ("Phone", 500.0, 20),
    ("Tablet", 750.0, 15)
])

conn.commit()
conn.close()
print("✅ Table created and data inserted.")
